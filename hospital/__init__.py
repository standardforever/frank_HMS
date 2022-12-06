from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from decouple import config


# create flask app
app = Flask(__name__)

# configure the SQLITE database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE')

# create the extension
db = SQLAlchemy(app)
db.init_app(app)


from hospital.admin import routes
