from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange
from application.models import Academics, Papers


class SearchDatabaseForm(FlaskForm):
    
    name = SelectField('Name', choices = [])
    title = SelectField('Title of Paper', choices = [])
    submit = SubmitField('Press to submit')


class UpdateAcademicForm(FlaskForm):

    academic_object = SelectField('Academic to Update', choices = [], coerce=int) # should return id of academic object
    name = StringField('Name', validators = [Length(max = 50)])
    current_instition = StringField('Current Insitution', validators = [Length(max = 30)])
    field_of_study = StringField('Field of Study', validators = [Length(max = 30)])
    submit = SubmitField('Press to submit')

    #maybe add a method to validate that details haven't been changed the same as another academic?

class UpdatePaperForm(FlaskForm):
    
    paper_object = SelectField('Paper to update', choices = [], coerce = int) 
    title = StringField('Title of Paper', validators = [Length(max = 30)])
    year_published = IntegerField('Year of Publication', validators = [NumberRange(min = 1457, max = 2023)])
    field_of_study = StringField('Field of Study', validators = [Length(max = 30)])
    submit = SubmitField('')

class AddAcademicForm(FlaskForm):
    
    name = StringField('Name', validators = [DataRequired(), Length(max = 50)])
    current_instition = StringField('Current Insitution', validators = [Length(max = 30)])
    field_of_study = StringField('Field of Study', validators = [Length(max = 30)])
    submit = SubmitField('')

class AddPaperForm(FlaskForm):
    
    title = StringField('Title of Paper', validators = [Length(max = 30), DataRequired()])
    year_published = IntegerField('Year of Publication', validators = [NumberRange(min = 1457, max = 2023)])
    field_of_study = StringField('Field of Study', validators = [Length(max = 30)])
    authors = SelectField('Authors', choices = [], coerce=int) #should return id of academic object
    submit = SubmitField('')

class DeleteAcademicForm(FlaskForm):
    #work out here how to allow for partial seraches in each of the fields
    academic_object = SelectField('Academic to Update', choices = [], coerce=int) # should return id of academic object
    name = StringField('Name', validators = [DataRequired(), Length(max = 50)])
    id = IntegerField('ID', validators = [])
    submit = SubmitField('')

class DeletePaperForm(FlaskForm):
     
     paper_object = SelectField('Paper to update', choices = [], coerce = int) # should retutn id of paper object
     title = StringField('Title of Paper', validators = [Length(max = 30), DataRequired()])
     id = SelectField('Paper ID')
     submit = SubmitField('')
