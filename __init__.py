from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db" #this will be changed to a cloud hosted server eventually
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'Environment_Variable' #this will be changed as well
db = SQLAlchemy(app)

from application import routes
