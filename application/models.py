#define classes for database
from dataclasses import field
from re import L
from QA_final_project import db #not sure if this import is correct


class Academics(db.model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.column(db.String(30), nullable=False)
    current_insitution = db.Column(db.String(30), default='Unkown')
    field_of_study = db.Column(db.String(30), default='Unkown') # this line could be moved to a seperate table
    authors = db.relatioship('authors', backref = 'academicbr')

    def __init__(self, first_name, last_name, current_insitution = None, field_of_study = None)
        self.first_name = first_name
        self.last_name = last_name
        self.current_insitution = current_insitution
        self.field_of_study = field_of_study

class Papers(db.model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    date_published = db.Column(db.Integer)
    impact = db.Column(db.Integer, default=0)
    field_of_study = db.Column(db.String(50), default='Unkown') # this line could be moved to a seperate table
    authors = db.relationship('authors', backref = 'papersbr')

    def __init__(self, title, date_published, impact, field_of_study):
        self.title = title
        self.date_published = date_published
        self.impact = impact
        self.field_of_study = field_of_study

class Authors(db.model):
    academic_id = db.Column('academics_id', db.Integer, db.Foreignkey('academics.id'), nullable=False) 
    paper_id = db.Column('students.id', db.Integer, db.Foreignkey('papers.id', nullable=False)) 

    def __init__(self, academic_id, paper_id):
        self.academic_id = academic_id
        self.paper_id = paper_id

