FROM python:3.10
copy . .
RUN pip install -r requirements.txt
RUN python3 create.db
ENTRYPOINT ["puthon3", "app.py"]
