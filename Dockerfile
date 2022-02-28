FROM python:3.10
copy . .
RUN pip install -r requirements.txt
ENV DATABASE_URI=$DATABASE_URI
RUN python3 create.py
ENTRYPOINT ["python3", "app.py"]
