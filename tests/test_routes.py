from flask_testing import TestCase
from application import app, db, routes
from application.models import Academics, Papers, Authors

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
            # SECRET_KEY='Secret key'
            DEBUG=True,
            WTF_CSRF_ENABLES=False
            )
        return app
    
    def setUp(self):
        db.drop_all()
        db.create_all()
        academic1 = Academics('An Academic', 'An Institution', 'A Field of Study')
        paper1 = Papers('A Paper', '2000', 'Another field of study')
        author1 = Authors(1, 1)
        db.session.add(academic1)
        db.session.add(paper1)
        db.session.add(author1)
        db.session.commit()
      

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestDelete(TestBase):
    
    def test_delete_academic(self):
        #test deletes the academic object created in setUp() and checks no objects are found
        response = self.client.post('/delete_academic',
        data = {'name' : 1})
        self.assertEqual(response.status_code, 200)
        assert len(Academics.query.all()) == 0
        assert len(Authors.query.all()) == 0
    
    def test_delete_paper(self):
        #test deletes the paper and author objects created in setUp() and checks no objects are found
        response = self.client.post('/delete_paper',
        data = {'title': 1})
        self.assertEqual(response.status_code, 200)
        assert len(Papers.query.all()) == 0
        assert len(Authors.query.all()) == 0

class TestCreate(TestBase):

    def test_create_academic(self):
        #tests that an academic is created with the correct attributes for the object
        response = self.client.post('/add_academic',
        data = {'name':'Another Academic', 'current_institution':'Another Institution', 'field_of_study':'Another Field of Study'})
        self.assertEqual(response.status_code, 200)
        test = Academics.query.filter_by(id=2).first()
        assert test.name == 'Another Academic'
        assert test.current_institution == 'Another Institution'
        assert test.field_of_study == 'Another Field of Study'
    
    def test_create_paper(self):
        #tests that a paper is created with the correct attributes and is also linked to the right author
        response = self.client.post('/add_paper',
        data = {'title':'Another Paper', 'year_published':2000, 'field_of_study':'Another Field of Study', 'authors1': 1, 'no_of_authors': '1'})
        test = Papers.query.filter_by(id=2).first()
        self.assertEqual(response.status_code, 200)
        assert test.title == 'Another Paper'
        assert test.year_published == 2000
        assert test.field_of_study == 'Another Field of Study'
        auth = Authors.query.filter_by(id=2).first()
        assert auth.academic_id == 1
        assert auth.paper_id == 2