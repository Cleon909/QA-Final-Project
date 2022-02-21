#!/bin/bash


python3 -m venv venv
. ./../venv/bin/activate
pip install -r requirements.txt
python3 create.py

sudo tee /etc/systemd/system/QAapplication.service << EOF > /dev/null
[Unit]
Description=QA Project Webb App

[Service]
User=jenkins
WorkingDirectory=/home/jenkins/.jenkins/workspace/deployment_test
ExecStart=/home/jenkins/.jenkins/workspace/web_app_test/venv/bin/python3 /home/jenkins/.jenkins/workspace/web_app_test/app.py

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable QAapplication.service
sudo systemctl restart QAapplication.service
export DATABASE_URI
export SECRET_KEY
