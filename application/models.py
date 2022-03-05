from application import db

class Academics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    current_institution = db.Column(db.String(30), default='Unknown')
    field_of_study = db.Column(db.String(30), default='Unknown') # this line could be moved to a seperate table
    Authors = db.relationship('Authors', backref = 'academicbr')

    def __init__(self, name, current_insitution, field_of_study):
        self.name = name
        self.current_institution = current_insitution
        self.field_of_study = field_of_study

class Papers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year_published = db.Column(db.Integer)
    field_of_study = db.Column(db.String(50), default='Unkown') # this line could be moved to a seperate table
    Authors = db.relationship('Authors', backref = 'Papersbr')

    def __init__(self, title, year_published, field_of_study):
        self.title = title
        self.year_published = year_published
        self.field_of_study = field_of_study

class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    academic_id = db.Column(db.Integer, db.ForeignKey('Academics.id'), nullable=False) 
    paper_id = db.Column(db.Integer, db.ForeignKey('Papers.id'), nullable=False) 

    def __init__(self, academic_id, paper_id):
        self.academic_id = academic_id
        self.paper_id = paper_id

