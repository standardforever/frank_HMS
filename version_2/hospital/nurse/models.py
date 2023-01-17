from hospital import db, app
from datetime import datetime
from hospital.patient.models import Patient
from hospital.admin.models import User


class NurseReport(db.Model):
    """Table for Nurse Report"""
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    entry = db.Column(db.Text, default=None)
    temperature = db.Column(db.Integer, default=None)
    weight = db.Column(db.Integer, default=None)
    blood_pressure = db.Column(db.Integer, default=None)
    # next_appointment = db.Column(db.String(80), nullable=False)
    nurse_id = db.Column(db.String(80), db.ForeignKey('user.id'), nullable=False)
    patient_id = db.Column(db.String(80), db.ForeignKey('patient.id'), nullable=False)


with app.app_context():   # all database operations under with
    db.create_all() 