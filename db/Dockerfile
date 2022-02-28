FROM python:3.10
copy . .
RUN pip install -r requirements.txt
ENV DATABASE_URI=$DATABASE_URI
ENTRYPOINT ["python3", "create.py"]
