from config import db
from datetime import datetime, timedelta

class User(db.Model):
    email = db.Column(db.String(128), primary_key=True)
    token = db.Column(db.String(43), unique=True, nullable=False)
    hotelid = db.Column(db.String(10), nullable=False)
    roomid = db.Column(db.String(10), unique=True, nullable=False)
    ssid = db.Column(db.String(32), nullable=False)
    psk = db.Column(db.String(63), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow() + timedelta(hours=1))
    wifiprovisioned = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return '{}'.format(self.email)