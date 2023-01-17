from wtforms import Form, BooleanField, StringField, PasswordField, validators


""" Registration Form """
class RegistrationForm(Form):
    # name = StringField('Name', [validators.Length(min=4, max=25)])
    # username = StringField('Username', [validators.Length(min=4, max=25)])
    first_name = StringField('Firstname', [validators.Length(min=4, max=25)])
    last_name = StringField('Lastname', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email()])
    address = StringField('Address', [validators.Length(min=4, max=40)])
    phone = StringField('Phone', [validators.Length(min=4, max=25)])
    
    # profile = db.Column(db.String(180), unique=False, nullable=False, default='profile.jpg')
    user_type = StringField('Usertype', [validators.Length(min=2, max=25)])
    user_role = StringField('Userrole', [validators.Length(min=2, max=25)])


""" Login Form"""
class LoginForm(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField("Login Password", [validators.DataRequired()])