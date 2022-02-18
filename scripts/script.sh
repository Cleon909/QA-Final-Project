#!/bin/bash
pwd
python3 -m venv venv
. ./../venv/bin/activate
pip install -r requirements.txt
export DATABASE_URI
export SECRET_KEY
python3 create.py
sudo tee /etc/systemd/system/QAapplication.service << EOF > /dev/null
[Unit]
Description=QA Project Webb App

[Service]
User=jenkins
WorkingDirectory=/home/jenkins/.jenkins/workspace/deployment_test
ExecStart=/usr/bin/python3 /home/jenkins/.jenkins/workspace.deployment_test/app.py

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable app.py
sudo systemctl1 restart app.py
