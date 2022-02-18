#!/bin/bash
cd ..
pwd
python3 -m venv venv
source venv/scripts/activate
pip install -r requirements.txt
export DATABASE_URI
export SECRET_KEY
python3 create.py
python3 app.py
