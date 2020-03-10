from secrets import token_urlsafe
from flask import render_template, url_for, request, redirect, jsonify
from sqlalchemy import exc
from flask_wtf.csrf import CSRFError
from forms import AddUserForm, DeleteUserForm, RegisterUserForm
from config import app, db, csrf, meraki_org
from models import User, datetime
from wifi import provision, deprovision, get_org_network_names
from datetime import datetime


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/adduser', methods=['GET', 'POST'])
def adduser():
    form = AddUserForm()
    form.roomid.choices = [(name, name) for name in get_org_network_names(meraki_org)]

    if request.method == 'GET':
        return render_template('adduser.html', form=form)
    elif request.method == 'POST':
        new_user = User(email=form.email.data,
                            hotelid=form.hotelid.data,
                            roomid=form.roomid.data,
                            ssid=form.ssid.data,
                            psk=form.psk.data,
                            token=token_urlsafe())
        db.session.add(new_user)
        try:
            db.session.commit()
        except exc.IntegrityError as e:
            db.session.rollback()
            return render_template('adduserfail.html', error=e), 400
        if new_user.ssid and new_user.psk:
            wifiprov = provision(form.hotelid.data, form.roomid.data, form.ssid.data, form.psk.data)

            if isinstance(wifiprov, Exception):
                return render_template('wififail.html', error=wifiprov), 400
            elif wifiprov['name'] == form.ssid.data and wifiprov['psk'] == form.psk.data:
                new_user.wifiprovisioned = True
                db.session.commit()
            return redirect( url_for('users'))
        return redirect( url_for('register', token=new_user.token))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterUserForm()
    token = request.args.get('token')
    if request.method == 'GET' and token:
        user = db.session.query(User).filter(User.token == token).first()

        if user:
            if user.token == token and user.timestamp > datetime.utcnow():
                return render_template('register.html', user=user, form=form)
            else:
                return render_template('401.html'), 401
        else:
            return render_template('404.html'), 404
    
    elif request.method == 'POST':
        if token:
            user = db.session.query(User).filter(User.token == token).first()
            if user:
                if user.token == token and user.timestamp > datetime.utcnow():
                    try:
                        user.ssid = form.ssid.data
                        user.psk = form.psk.data
                        db.session.commit()
                    except exc.IntegrityError as e:
                        db.session.rollback()
                        return render_template('adduserfail.html', error=e), 400

                    wifiprov = provision(user.hotelid, user.roomid, form.ssid.data, form.psk.data)

                    if isinstance(wifiprov, Exception):
                        return render_template('wififail.html', error=wifiprov), 400
                    elif wifiprov['name'] == form.ssid.data and wifiprov['psk'] == form.psk.data:
                        user.wifiprovisioned = True
                        db.session.commit()
                        return render_template('thankyou.html')
            else:
                return render_template('404.html'), 404
        else:
            return render_template('401.html'), 401
    else:
        return render_template('404.html'), 404

@app.route('/users', methods=['GET', 'POST'])
def users():
    form = DeleteUserForm()
    if request.method == 'GET':
        users = User.query.all()
        return render_template('users.html', users=users, form=form)
    elif request.method == 'POST':
        del_user = User.query.get(form.email.data)
        if del_user.wifiprovisioned:
            wifideprov = deprovision(del_user.hotelid, del_user.roomid)
        db.session.delete(del_user)
        db.session.commit()
        return redirect(url_for('users'))

@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 403

@app.route('/api/adduser', methods=['POST'])
@csrf.exempt
def api_adduser():
    req_key = request.headers.get('x-api-key')
    req_data = request.get_json()
    if req_data and req_key == 'b20f7b36d7430b19326e6bc27c3c31df3ecb0a42fc3a45a48567d527eff03388': # Fake API key for testing. Use your own method for authenticating API requests.
        token = token_urlsafe()
        new_user = User(email=req_data['email'],
                            hotelid=req_data['hotelid'],
                            roomid=req_data['roomid'],
                            token=token)
        db.session.add(new_user)
        try:
            db.session.commit()
        except exc.IntegrityError as e:
            db.session.rollback()
            return 'Adding user failed. Are you adding a duplicate user?', 400
        return jsonify(magiclink=f"https://example.com?token={token}"), 200
    return 'No request data', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)