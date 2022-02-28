FROM python:3.10
copy . .
RUN pip install -r requirements.txt
ENV DATABASE_URI=DATABASE_URI
ENV SECRET_KEY=SECRET_KEY
ENTRYPOINT ["python3", "app.py"]
