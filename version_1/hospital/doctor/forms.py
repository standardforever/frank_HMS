from wtforms import Form, TextAreaField, StringField, validators

class DoctorForm(Form):
    entry = TextAreaField('Entry', [validators.DataRequired()])
    diagnosis = StringField('Diagnosis')
    recommendation = StringField('Recommendation')
    prescription = TextAreaField('Prescription')
    lab = TextAreaField("Lab")
