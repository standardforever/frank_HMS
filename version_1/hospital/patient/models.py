from hospital import db, app
from datetime import datetime

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    phoneNumber = db.Column(db.String(80), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    sex = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    state = db.Column(db.String(80), nullable=False)
    emergencyName = db.Column(db.String(80), nullable=False)
    emergencyContact = db.Column(db.String(120), nullable=False)
    relationship = db.Column(db.String(80), nullable=False)

    doctor_report = db.relationship("DoctorReport",
                              backref="patient",
                              cascade="all, delete, delete-orphan")
    nurse_report = db.relationship("NurseReport",
                              backref="patient",
                              cascade="all, delete, delete-orphan")

    def __repr__(self):
        return  '<User %r>' % self.first_name



with app.app_context():   # all database operations under with
    db.create_all() 


