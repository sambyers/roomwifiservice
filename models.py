from config import db, token_expiration
from datetime import datetime, timedelta

class User(db.Model):
    email = db.Column(db.String(128), primary_key=True, nullable=False)
    token = db.Column(db.String(43), unique=True, nullable=False)
    hotelid = db.Column(db.String(10), nullable=False)
    roomid = db.Column(db.String(10), unique=True, nullable=False)
    ssid = db.Column(db.String(32))
    psk = db.Column(db.String(63))
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow() + timedelta(hours=token_expiration))
    wifiprovisioned = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return '{}'.format(self.email)