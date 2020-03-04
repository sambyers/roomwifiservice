from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length
from config import meraki_org

class AddUserForm(FlaskForm):
    email = StringField('email')
    hotelid = SelectField('hotelid', choices = [(meraki_org, meraki_org)])
    roomid = SelectField('roomid', coerce=str)
    ssid = StringField('ssid')
    psk = StringField('psk')
    submit = SubmitField('Submit')

class DeleteUserForm(FlaskForm):
    email = StringField('email')
    submit = SubmitField('Delete')

class RegisterUserForm(FlaskForm):
    email = StringField('email')
    ssid = StringField('ssid')
    psk = StringField('psk')
    submit = SubmitField('Submit')