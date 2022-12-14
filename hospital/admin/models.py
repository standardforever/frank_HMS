from hospital import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phoneNumber = db.Column(db.String(80), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    sex = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    address = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    state = db.Column(db.String(80), nullable=False)
    weight = db.Column(db.Numeric, nullable=False)
    height = db.Column(db.Numeric, nullable=False)
    medication = db.Column(db.Boolean, nullable=False)
    message = db.Column(db.Text, nullable=False)
    emergencyName = db.Column(db.String(80), nullable=False)
    emergencyContact = db.Column(db.String(120), nullable=False)
    relationship = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return  '<User %r>' % self.name
