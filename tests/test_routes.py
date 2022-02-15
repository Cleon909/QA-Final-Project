from flask import url_for
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
        #test deletes the academic and paper objects created in setUp() and checks no objects are found
        response = self.client.post(url_for('delete_academic'),
        data = dict(a_to_del = Academics.query.filter_by(id=1).all(), 
        pap_to_del = Authors.query.filter_by(paper_id=1).all()),
        follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        assert len(Academics.query.all()) == 0
        assert len(Authors.query.all()) ==0
    
    def test_delete_paper(self):
        #test deletes the academic and author objects created in setUp() and checks no objects are found
        response = self.client.post(url_for('delete_paper'),
        data = dict(p_to_del = Papers.query.filter_by(id=1).all(), 
        auth_to_del = Authors.query.filter_by(paper_id=1).all()),
        follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        assert len(Papers.query.all()) == 0
        assert len(Authors.query.all()) ==0


