from flask import url_for
from flask_testing import TestCase
from application import app, db
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
        db.session.add(academic1, paper1)
        db.session.commit()
        author1 = Authors(academic1.id, paper1.id)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestDelete(TestBase):
    
    def test_delete_academic(self):
        response = self.client.post(url_for('delete_academic'),
        data = dict(id=1,academic_id=1),
        follow_redirects=True)


