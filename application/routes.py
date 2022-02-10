# methods and routing
from flask import render_template, url_for, redirect, request, Flask
from QA_final_project import app, db
from models import Academics, Papers, Authors
from forms import SearchDatabaseForm, UpdateAcademicForm, UpdatePaperForm, AddAcademicForm, AddPaperForm, DeleteAcademicForm, DeletePaperForm 

app = Flask(__name__)


@app.route('/', methods = ['GET'])
@app.route('/home', methods = ['GET'])
def index():
    form = SearchDatabaseForm()
    total_number = {'number_of_academics': Academics.query.all.count(),
    'number_of_papers': Papers.query.count()}
    #here put a method to use each field to further filter the results
    academic_search_result = Academics.query.all()
    paper_search_result = Papers.query.all()
    academics_ = Academics.query.all()
    for academic in academics_:
        form.name.choices.append(
            (academic.id, f"{academic.name}")
        )
    for academic in academics_:
        form.current_institution.choices.append(
            (academic.id, f"{academic.current_institution}")
        )
    for academic in academics_:
        form.field_of_study.choices.append(
            (academic.id, f"{academic.field_of_study}")
        )
    papers_ = Papers.query.all()
    for paper in papers_:
        form.title.choices.append(
            (paper.id, f"{paper.title}")
        )
    for paper in papers_:
        form.year_published.choices.append(
            (paper.id, f"{paper.year_published}")
        )
    for paper in papers_:
        form.title.impact.append(
            (paper.id, f"{paper.impact}")
        )
    for paper in papers_:
        form.title.field_of_study.append(
            (paper.id, f"{paper.field_of_study}")
        )
    return render_template('index.html', form=form, total_number=total_number, academic_search_result=academic_search_result, paper_search_result=paper_search_result )

@app.route('/update_academic', methods = ['GET, POST'])
def update_academic():
    form = UpdateAcademicForm
    list_of_academics = []
    if form.academic_object.data == None:
        list_of_academics = Academics.query.all()
    else:
        Academics.query.filter_by(id=form.academic_object.data).all() #this hopefully will filter by what is entered into field
    #methods here will post from update fields
    if len(list_of_academics) == 1:
        return
        #then the fields to update will appear and will post to the list_of_academics[0] object. 
    return

@app.route('/update_paper', methods = ['GET, POST'])
def update_paper():
    form = UpdatePaperForm
    list_of_papers = []
    if form.paper_object.data == None:
        list_of_papers = Papers.query.all()
    else:
        Papers.query.filter_by(id=form.paper_object.data).all()
    if len(list_of_papers) == 1:
        return
        #code here to amend the object
    return


@app.route('/add_academic')
def add_academic():
    form = AddAcademicForm()
    name = form.name.data
    current_institution = form.current_instition.data
    field_of_study = form.field_of_study.data
    academic = Academics(name, current_institution, field_of_study)
    db.session.add(academic)
    db.session.commit()
    return (url_for('index'))

@app.route('/add_paper')
def add_paper():
    form = AddPaperForm()
    title = form.title.data
    date_published = form.date_published.data
    field_of_study = form.field_of_study.data
    authors = None # this should feed into a method that should add lines ot the child database , with the same paper_id and a new entry for each academic id
    paper = Papers(title, date_published, field_of_study)
    db.session.add(paper) #work out how to add authors to child table
    db.commit()
    return

@app.route('/delete_academic')
def delete_academic():
    form = DeleteAcademicForm()
    list_of_academics = []
    if form.academic_object.data == None:
        list_of_objects = Academics.query.all()
    else:
        list_of_objects = Academics.query.filter_by(id=form.academic.data)
    # method to delete here
    return

@app.route('/delete_paper')
def delete_paper():
    form = DeletePaperForm()
    list_of_papers = []
    if form.paper_object.data == None:
        list_of_papers = Papers.query.all()
    else:
        list_of_papers = Papers.query.filter_by(id=form.paper_object.data).all()
    # method to delete
    return

@app.route('/about')
def about():
    return

