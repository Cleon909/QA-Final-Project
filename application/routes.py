# methods and routing
from flask import render_template, url_for, redirect, request, Flask
from app import app, db
from application.models import Academics, Papers, Authors
from application.forms import SearchDatabaseForm, UpdateAcademicForm, UpdatePaperForm, AddAcademicForm, AddPaperForm, DeleteAcademicForm, DeletePaperForm 


#this prepopulates the database with some data to look at

academic1 = Academics('Bob Dole', 'University of Bradford', 'Metaphysics')
db.session.add(academic1)
academic2 = Academics('Gisela Joseph','Zombie College', 'Magic History' )
db.session.add(academic2)
academic3 = Academics('Durga Van As', 'Unseen University', 'Foreign Life Gardening')
db.session.add(academic3)
academic4 = Academics('Nerva Augustus', 'University of Ithica', 'Hermetic Semiosis')
db.session.add(academic4)
academic5 = Academics('Antoninus Pius', 'GURPS Illuminati University', 'Illumanti History')
db.session.add(academic5)
academic6 = Academics('Narciso Baumann', 'Unseen University', 'English Literature')
db.session.add(academic6)
academic7 = Academics('Trajan Augustus', 'University of Bradford', 'Dutch Ethnic Etymology')
db.session.add(academic7)
academic8 = Academics('Captain Ahab','Zombie College', 'Hermetic Semiosis')
db.session.add(academic8)
academic9 = Academics('Luke Skywalker','Zombie College','Metaphysics')
db.session.add(academic9)
academic10 = Academics('Darth Vader', 'GURPS Illuminati University', 'Dutch Ethnic Etymology')
db.session.add(academic10)
academic11 = Academics('Luitenent Starbuck', 'Unseen University', 'Illumanti History')
db.session.add(academic11)
academic12 = Academics('Marcus Aurelius', 'University of Bradford', 'Hermetic Semiosis')
db.session.add(academic12)
academic13 = Academics('Hadrian Augustus', 'GURPS Illuminati University', 'Dutch Ethnic Etymology')
db.session.add(academic13)
academic14 = Academics('Hector Salamancis', 'Unseen University', 'Foreign Life Gardening')
db.session.add(academic14)
academic15 = Academics('Noble Johnson', 'Starfleet Academy', 'English Literature')
db.session.add(academic15)
academic16 = Academics('Augustus Ceaser', 'University of Ithica', 'Dutch Ethnic Etymology')
db.session.add(academic16)
academic17 = Academics('Heracleus Ceaser','Zombie College', 'Illumanti History')
db.session.add(academic17)
academic18 = Academics('Count Belisarius', 'Unseen University', 'Magic History')
db.session.add(academic18)
academic19 = Academics('Cyrus The Great', 'Starfleet Academy', 'South Carribean Semiotics')
db.session.add(academic19)
academic20 = Academics('Scipio Africanus', 'University of Ithica', 'Foreign Life Gardening')
db.session.add(academic20)

paper1 = Papers('Nihilism and dialectic appropriation', 1985, 'Advanced Semiotics')
db.session.add(paper1)
paper2 = Papers('Marxist capitalism in the works of Gaiman', 2020, 'The Occult')
db.session.add(paper2)
paper3 = Papers('Postpatriarchial libertarianism in the works of Glass', 2010, 'Compter Science and Etymology')
db.session.add(paper3)
paper4 = Papers('Postpatriarchial libertarianism in the works of Glass', 1999, 'Music and the Movement of the Spheres')
db.session.add(paper4)
paper5 = Papers('Reinventing Constructivism: Modernism in the works of Eco', 2018, 'Semiotics and history of Evolution')
db.session.add(paper5)
paper6 = Papers('A Biography of Eric "Eazy-E" Wright', 1998, 'Biography as the Expression of Power')
db.session.add(paper6)
paper7 = Papers('The Principle Knowledge That God Is Omniscience', 2022, 'Mathematics of the Celestial Heavens')
db.session.add(paper7)
paper8 = Papers('An Introduction to the Analysis of Theological Task', 2020, 'Ancient Astronauts')
db.session.add(paper8)
paper9 = Papers('Precapitalist constructivist theory and postdeconstructive appropriation', 2006, 'Creationist Cosmologies')
db.session.add(paper9)
paper10 = Papers('Precapitalist dematerialism and constructivism', 1970, 'The Occult')
db.session.add(paper10)
paper11= Papers('Sartreist absurdity in the works of Gaiman', 1696, 'Advanced Semiotics')
db.session.add(paper11)
paper12 = Papers('Examining the QCD Law in Models of Monopoles: Firewalls', 1066, 'Creationist Cosmologies') 
db.session.add(paper12)
paper13 = Papers('Reflexive tactics for algebra, revisited', 1453, 'Ancient Astronauts')
db.session.add(paper13)
paper14 = Papers('Evolution of SASyLF 2008-2021', 453, 'Biography as the Expression of Power')
db.session.add(paper14)
paper15 = Papers('Bunched Fuzz: Sensitivity for Vector Metrics', 2001, 'Biography as the Expression of Power')
db.session.add(paper15)
paper16 = Papers('Worlds of the Phaedo and the Term', 1875, 'Biography as the Expression of Power')
db.session.add(paper16)
paper17 = Papers('Dark Spirituality as a Symbol Female', 1930, 'Creationist Cosmologies')
db.session.add(paper17)
paper18 = Papers('Which can Jump Highe, a Car Flea of a Dog Flea?', 2010, 'Music and the Movement of the Spheres')
db.session.add(paper18)
paper19 = Papers('Do Woodpeckers get Headaches?', 2006, 'Mathematics of the Celestial Heavens')
db.session.add(paper19)
paper20 = Papers('The propulsion Paramters of Penguin Poop', 2008, 'Ancient Astronauts')
db.session.add(paper20)
bridge1 = Authors(academic1.id, paper7.id)
db.session.add(bridge1)
bridge2 = Authors(academic2.id, paper7.id)
db.session.add(bridge2)
bridge3 = Authors(academic3.id, paper5.id)
db.session.add(bridge3)
bridge4 = Authors(academic4.id, paper3.id)
db.session.add(bridge4)
bridge5 = Authors(academic5.id, paper19.id)
db.session.add(bridge5)
bridge6 = Authors(academic6.id, paper9.id)
db.session.add(bridge6)
bridge7 = Authors(academic7.id, paper8.id)
db.session.add(bridge7)
bridge8 = Authors(academic8.id, paper4.id)
db.session.add(bridge8)
bridge9 = Authors(academic9.id, paper20.id)
db.session.add(bridge9)
bridge10 = Authors(academic10.id, paper19.id)
db.session.add(bridge10)
bridge11 = Authors(academic11.id, paper18.id)
db.session.add(bridge11)
bridge12 = Authors(academic12.id, paper17.id) 
db.session.add(bridge12)
bridge13 = Authors(academic13.id, paper16.id)
db.session.add(bridge13)
bridge14 = Authors(academic14.id, paper15.id)
db.session.add(bridge14)
bridge15 = Authors(academic15.id, paper14.id)
db.session.add(bridge15)
bridge16 = Authors(academic16.id, paper13.id)
db.session.add(bridge16)
bridge17 = Authors(academic17.id, paper12.id)
db.session.add(bridge17)
bridge18 = Authors(academic12.id, paper11.id)
db.session.add(bridge18)
bridge19 = Authors(academic19.id, paper10.id)
db.session.add(bridge19)
bridge20 = Authors(academic20.id, paper9.id)
db.session.add(bridge20)
bridge21 = Authors(academic2.id, paper8.id)
db.session.add(bridge21)
bridge22 = Authors(academic18.id, paper7.id)
db.session.add(bridge22)
bridge23 = Authors(academic4.id, paper6.id)
db.session.add(bridge23)
bridge24 = Authors(academic7.id, paper5.id)
db.session.add(bridge24)
bridge25 = Authors(academic12.id, paper4.id)
db.session.add(bridge25)
bridge26 = Authors(academic20.id, paper3.id)
db.session.add(bridge26)
bridge27 = Authors(academic1.id, paper2.id)
db.session.add(bridge27)
bridge28 = Authors(academic4.id, paper1.id)
db.session.add(bridge28)
db.session.commit()



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

