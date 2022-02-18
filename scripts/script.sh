#!/bin/bash
pwd
python3 -m venv venv
. ./../venv/bin/activate
pip install -r requirements.txt
export DATABASE_URI
export SECRET_KEY
python3 create.py
python3 app.py
