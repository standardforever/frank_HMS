from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


# create flask app
app = Flask(__name__)

# configure the SQLITE database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'DHADISFN24'

bcrypt = Bcrypt(app)

# create the extension
db = SQLAlchemy(app)
from hospital.nurse import models
db.init_app(app)
# with app.app_context():   # all database operations under with
#     db.create_all() 


from hospital.admin import routes
from hospital.patient import routes
from hospital.nurse import routes
from hospital.doctor import routes