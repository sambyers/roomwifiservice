from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from secrets import token_bytes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mock.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = token_bytes()
db = SQLAlchemy(app)
csrf = CSRFProtect(app)
meraki_org = 'YOUR MERAKI ORG'