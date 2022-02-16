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
        academic1 = Academics('Academic A', 'Institution A', 'Field of Study A')
        academic2 = Academics('Academic B', 'Institution B', 'Field of Study B')
        academic3 = Academics('Academic C', 'Institution C', 'Field of Study C')
        academic4 = Academics('Academic D', 'Institution D', 'Field of Study D')
        paper1 = Papers('A Paper', '2000', 'Another field of study')
        author1 = Authors(1, 1)
        db.session.add(academic1)
        db.session.add(academic2)
        db.session.add(academic3)
        db.session.add(academic4)
        db.session.add(paper1)
        db.session.add(author1)
        db.session.commit()
      

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestPostResponse(TestBase):
    
    def test_delete_academic(self):
        #test deletes the academic object created in setUp() and checks no objects are found
        response = self.client.post('/delete_academic',
        data = {'name' : 1})
        self.assertEqual(response.status_code, 200)
        assert len(Academics.query.all()) == 3
        assert len(Authors.query.all()) == 0
    
    def test_delete_paper(self):
        #test deletes the paper and author objects created in setUp() and checks no objects are found
        response = self.client.post('/delete_paper',
        data = {'title': 1})
        self.assertEqual(response.status_code, 200)
        assert len(Papers.query.all()) == 0
        assert len(Authors.query.all()) == 0

    def test_create_academic(self):
        #tests that an academic is created with the correct attributes for the object
        response = self.client.post('/add_academic',
        data = {'name':'Another Academic', 'current_institution':'Another Institution', 'field_of_study':'Another Field of Study'})
        self.assertEqual(response.status_code, 200)
        test = Academics.query.filter_by(id=5).first()
        assert test.name == 'Another Academic'
        assert test.current_institution == 'Another Institution'
        assert test.field_of_study == 'Another Field of Study'
    
    def test_create_paper(self):
        #tests that a paper is created with the correct attributes and is also linked to the right author
        response = self.client.post('/add_paper',
        data = {'title':'Another Paper', 'year_published':2000, 'field_of_study':'Another Field of Study', 'authors1': 1, 'no_of_authors': '2', 'authors2': 2})
        test = Papers.query.filter_by(id=2).first()
        self.assertEqual(response.status_code, 200)
        assert test.title == 'Another Paper'
        assert test.year_published == 2000
        assert test.field_of_study == 'Another Field of Study'
        auth1 = Authors.query.filter_by(id=2).first()
        auth2 = Authors.query.filter_by(id=3).first()
        assert auth1.academic_id == 1
        assert auth1.paper_id == 2
        assert auth2.academic_id == 2
        assert auth2.paper_id == 2

    def test_update_academic(self):
        #tests that updates to the academic field are saved into database
        response = self.client.post('/update_academic',
        data = {'academic_object': 1, 'name':'Different Name', 'current_institution':'Different Institution', 'field_of_study':'Different FOD'})
        self.assertEqual(response.status_code, 200)
        acad = Academics.query.filter_by(id=1).first()
        assert acad.name == 'Different Name'
        assert acad.current_institution == 'Different Institution'
        assert acad.field_of_study == 'Different FOD'

    def test_update_paper(self):
        #tests that updates to papers fields and linked authors are saved into database
        response = self.client.post('/update_paper',
        data = {'paper_object': '1', 'title':'Different Title', 'year_published':'1900', 'field_of_study':'Different FOD', 'no_of_authors':'2', 'author1':'3', 'author2':'4'})
        self.assertEqual(response.status_code, 200)
        pap = Papers.query.filter_by(id=1).first()
        assert pap.title == 'Different Title'
        assert pap.year_published == 1900
        assert pap.field_of_study == 'Different FOD'
        auth1 = Authors.query.filter_by(id=2).first()
        auth2 = Authors.query.filter_by(id=3).first()
        assert auth1.academic_id == 3
        assert auth1.paper_id == 1
        assert auth2.academic_id == 4
        assert auth2.paper_id == 1

    def test_index_page(self):
        #tests that attributes in the searched objects are included in response data from home page
        response = self.client.post('/',
        data = { 'name':1, 'title':1 })
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Academic A', response.data)
        self.assertIn(b'Institution A', response.data)
        self.assertIn(b'Field of Study A', response.data)
        self.assertIn(b'A Paper', response.data)
        self.assertIn(b'2000', response.data)
        self.assertIn(b'Another field of study', response.data)

class TestGetResponse(TestBase):

    def test_index_get(self):
        #tests response and makes sure a string is inicluded from both the layour and block body
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Nonsense Academic Database', response.data)
        self.assertIn(b'Search for Academic', response.data)
    
    def test_update_academic_get(self):
        #tests response and makes sure a string is inicluded from both the layour and block body 
        response = self.client.get('/update_academic')
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Nonsense Academic Database', response.data)
        self.assertIn(b'Choose Academic to Amend', response.data)

    def test_update_paper_get(self):
        #tests response and makes sure a string is inicluded from both the layour and block body 
        response = self.client.get('/update_paper')
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Nonsense Academic Database', response.data)
        self.assertIn(b'Choose Paper to Amend', response.data)

    def test_add_academic_get(self):
        #tests response and makes sure a string is inicluded from both the layour and block body 
        response = self.client.get('/add_academic')
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Nonsense Academic Database', response.data)
        self.assertIn(b'Add an Academic', response.data)

    def test_add_paper_get(self):
        #tests response and makes sure a string is inicluded from both the layour and block body 
        response = self.client.get('/add_academic')
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Nonsense Academic Database', response.data)
        self.assertIn(b'Add a Paper', response.data)
    
    def test_delete_academic_get(self):
        #tests response and makes sure a string is inicluded from both the layour and block body 
        response = self.client.get('/delete_academic')
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Nonsense Academic Database', response.data)
        self.assertIn(b'Delete an Academic', response.data)

    def test_del_paper_get(self):
        #tests response and makes sure a string is inicluded from both the layour and block body 
        response = self.client.get('/delete_paper')
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Nonsense Academic Database', response.data)
        self.assertIn(b'Delete a Paper', response.data)