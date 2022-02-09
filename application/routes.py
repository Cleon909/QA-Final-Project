# methods and routing
from flask import Flask
from QA_final_project import app, db
from models import Academcs, Papers, Authors


app = Flask(__name__)

@app.route('/')
@app.route('/')
def home():
    return

@app.route('/update')
def update():
    return

@app.route('/add')
def add():
    return

@app.route('/delete')
def add():
    return

@app.route('/about')
def about():
    return

