#!/bin/bash
cd ..
python venv venv
source venv/scripts/activate
pip install -r requirements.txt
python create.py
python -m pytest

export DATABASE_URI