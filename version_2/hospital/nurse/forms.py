from wtforms import Form, TextAreaField, StringField, IntegerField, validators


""" Nurse Form """
class NurseForm(Form):
    entry = TextAreaField('Entry', [validators.DataRequired()])
    temperature = IntegerField('Temperature')
    weight = IntegerField('Weight')
    blood_pressure = IntegerField('blood_pressure')
    