#code to run the webapp and crate connection to the database
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db" #this will be changed to a cloud hosted server eventually
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#app.config['SECRET_KEY'] = 'Environment_Variable' #this will be changed as well
db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0')

from application import routes

    