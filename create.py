#code to create db and schema and to fill it with some data
from app import db, app 
from application.models import Academics, Papers, Authors

db.create_all()


