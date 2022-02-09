#define classes for database
from QA_final_project import db #not sure if this import is correct


class Academics(db.model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.column(db.String(30), nullable=False)
    current_insitution = db.Column(db.String(30))
    field_of_study = db.Column(db.String(30)) # this line could be moved to a seperate table
    authors = db.relatioship('authors', backref = 'academicbr')

class Papers(db.model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    date_published = db.Column(db.Date)
    impact = db.Column(db.Integer, default=0)
    field_of_study = db.Column(db.String(50)) # this line could be moved to a seperate table
    authors = db.relationship('authors', backref = 'papersbr')

class Authors(db.model):
    academic_id = db.Column('academics_id', db.Integer, db.Foreignkey('academics.id'), nullable=False) 
    paper_id = db.Column('students.id', db.Integer, db.Foreignkey('papers.id', nullable=False)) 
