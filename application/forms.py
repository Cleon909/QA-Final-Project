from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange
from models import Academics, Papers, Authors


class SearchDatabaseForm(FlaskForm):
    
    first_name = SelectField('First name', choices = [])
    last_name = SelectField('Last name', choices = [])
    current_instition = SelectField('Current Insitution', choices = [])
    field_of_study = SelectField('Field of Study', choices = [])
    submit = SubmitField('')
    title = SelectField('Title of Paper', choices = [])
    year_published = SelectField('Year of Publication', choices = [], coerce = int)
    impact = SelectField('Impact Factor(0 <> 20)', choices = [], coerce = int)
    field_of_study = SelectField('Field of Study', choices = [])

class UpdateAcademicForm(FlaskForm):

    academic_object = SelectField('Academic to Update', choices = [], coerce=int) # should return id of academic object
    first_name = StringField('First name', validators = [Length(max = 30)])
    last_name = StringField('Last name', validators = [Length(max = 30)])
    current_instition = StringField('Current Insitution', validators = [Length(max = 30)])
    field_of_study = StringField('Field of Study', validators = [Length(max = 30)])
    submit = SubmitField('')

    #maybe add a method to validate that details haven't been changed the same as another academic?

class UpdatePaperForm(FlaskForm):
    
    paper_object = SelectField('Paper to update', choices = [], coerce = int) 
    title = StringField('Title of Paper', validators = [Length(max = 30)])
    year_published = IntegerField('Year of Publication', validators = [NumberRange(min = 1457, max = 2023)])
    impact = IntegerField('Impact Factor(0 <> 20)', validators = [NumberRange(min = 0, max = 20)])
    field_of_study = StringField('Field of Study', validators = [Length(max = 30)])
    submit = SubmitField('')

class AddAcademicForm(FlaskForm):
    
    first_name = StringField('First name', validators = [DataRequired(), Length(max = 30)])
    last_name = StringField('Last name', validators = [DataRequired(), Length(max = 30)])
    current_instition = StringField('Current Insitution', validators = [Length(max = 30)])
    field_of_study = StringField('Field of Study', validators = [Length(max = 30)])
    submit = SubmitField('')

class AddPaperForm(FlaskForm):
    
    title = StringField('Title of Paper', validators = [Length(max = 30), DataRequired()])
    year_published = IntegerField('Year of Publication', validators = [NumberRange(min = 1457, max = 2023)])
    impact = IntegerField('Impact Factor(0 <> 20)', validators = [NumberRange(min = 0, max = 20)])
    field_of_study = StringField('Field of Study', validators = [Length(max = 30)])
    authors = SelectField('Authors', choices = [], coerce=int) #should return id of academic object
    submit = SubmitField('')

class DeleteAcademicForm(FlaskForm):
    #work out here how to allow for partial seraches in each of the fields
    academic_object = SelectField('Academic to Update', choices = [], coerce=int) # should return id of academic object
    first_name = StringField('First name', validators = [DataRequired(), Length(max = 30)])
    last_name = StringField('Last name', validators = [DataRequired(), Length(max = 30)])
    id = IntegerField('ID', validators = [])
    submit = SubmitField('')

class DeletePaperForm(FlaskForm):
     
     paper_object = SelectField('Paper to update', choices = [], coerce = int) # should retutn id of paper object
     title = StringField('Title of Paper', validators = [Length(max = 30), DataRequired()])
     id = SelectField('Paper ID')
     submit = SubmitField('')
