from hospital import db, app

from datetime import datetime

""" Table for User Credientail """
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.Text, nullable=False)
    phone = db.Column(db.String(30), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(180), unique=False, nullable=False)
    profile = db.Column(db.String(180), unique=False, nullable=False, default='profile.jpg')
    user_type = db.Column(db.String(20), nullable=False)
    user_role = db.Column(db.String(80), nullable=False)
    # reg_no = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


with app.app_context():   # all database operations under with
    db.create_all() 