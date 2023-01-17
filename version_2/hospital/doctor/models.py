from hospital import app, db
from datetime import datetime

class DoctorReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    entry = db.Column(db.Text, default=None)
    diagnosis = db.Column(db.Text, default=None)
    recommendation = db.Column(db.Text, default=None)
    prescription = db.Column(db.Text, default=None)
    lab = db.Column(db.Text, default=None)
    date = db.Column(db.Date)
    doctor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)

with app.app_context():   # all database operations under with
    db.create_all()