from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange
from application.models import Academics, Papers


class SearchDatabaseForm(FlaskForm):
    
    name = SelectField('Name', choices = [])
    title = SelectField('Title of Paper', choices = [])
    submit = SubmitField('Press to submit')


class UpdateAcademicForm(FlaskForm):

    academic_object = SelectField('Academic to Update', choices = []) # should return id of academic object
    
    name = StringField('Name', validators = [Length(max = 50)])
    current_institution = StringField('Current Insitution', validators = [Length(max = 30)])
    field_of_study = StringField('Field of Study', validators = [Length(max = 30)])
    submit = SubmitField('Press to submit')

    #maybe add a method to validate that details haven't been changed the same as another academic?

class UpdatePaperForm(FlaskForm):
    
    paper_object = SelectField('Paper to update', choices = [], coerce = int) 
    title = StringField('Title of Paper')
    year_published = SelectField('Year of Publication', choices = [i for i in range(1453, 2023)])
    field_of_study = StringField('Field of Study', validators = [Length(max = 30)])
    no_of_authors = SelectField('Number of Authors', choices = [1,2,3,4])
    author1 = SelectField('Author', choices =[])
    author2 = SelectField('Author', choices =[])
    author3 = SelectField('Author', choices =[])
    author4 = SelectField('Author', choices =[])
    submit = SubmitField('Press to Submit')

class AddAcademicForm(FlaskForm):
    
    name = StringField('Name', validators = [DataRequired(), Length(max = 50)])
    current_institution = StringField('Current Insitution', validators = [Length(max = 30)])
    field_of_study = StringField('Field of Study', validators = [Length(max = 30)])
    submit = SubmitField('Press to add academic')

class AddPaperForm(FlaskForm):

    title = StringField('Title of Paper', validators = [Length(max = 30), DataRequired()])
    year_published = SelectField('Year of Publication', choices = [i for i in range (1453, 2023)])
    field_of_study = StringField('Field of Study', validators = [Length(max = 30)])
    no_of_authors = SelectField('Number of Authors', choices = [1,2,3,4])
    authors1 = SelectField('Authors', choices = [])
    authors2 = SelectField('Authors', choices = [])
    authors3= SelectField('Authors', choices = [])
    authors4= SelectField('Authors', choices = [])
    submit = SubmitField('Press to add paper')

class DeleteAcademicForm(FlaskForm):
    name = SelectField('Academic to Delete', choices = [])
    submit = SubmitField('Press to delete')

class DeletePaperForm(FlaskForm):
     
     title = SelectField('Paper to delete', choices = []) 
     submit = SubmitField('Press to delete')
