#!/bin/bash
pwd
python3 -m venv venv
. ./../venv/bin/activate
pip install -r requirements.txt
pip freeze
python3 create.py
python3 -m pytest

sudo tee /etc/systemd/system/QAapplication.service << EOF > /dev/null
[Unit]
Description=QA Project Webb App

[Service]
User=jenkins
Environment=SECRET_KEY='abcd'
Environment=DATABASE_URI='sqlite:///data.db'
WorkingDirectory=/home/jenkins/.jenkins/workspace/deployment_test
ExecStart=/usr/bin/python3 /home/jenkins/.jenkins/workspace/deployment_test/app.py

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable QAapplication.service
sudo systemctl restart QAapplication.service
export DATABASE_URI
export SECRET_KEY
