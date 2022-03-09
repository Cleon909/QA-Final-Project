from selenium import webdriver
from flask_testing import LiveServerTestCase
from application import app, db, models
from flask import url_for
from urllib.request import urlopen
  

class TestBase(LiveServerTestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = "sqlite:///test.db",
            DEBUG=True,
            TESTING=True
        )
        return app
    
    def setUp(self):
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        db.create_all()
        self.driver.get(f'http:..localhost:5000/')
    
    def teardown(self):
        self.driver.quit()
        db.drop_all()

    def test_server_is_up(self):
        response = urlopen(f'http://localhost:5000')
        self.assertEqual(response.code, 200)


class TestCreateAcademic(TestBase):
    def test_create(self):
        self.driver.get(f'http://localhost:5000/add_academic')
        input_box1 = self.driver.find_element_by_xpath('//*[@id="name"]')
        input_box1.send.keys('Adam')
        input_box1 = self.driver.find_element_by_xpath('//*[@id="current_institution"]')
        input_box1.send.keys('Uni')
        input_box1 = self.driver.find_element_by_xpath('//*[@id="field_of_study"]')
        input_box1.send.keys('Science')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        acad = models.Academics.query.filter_by(name='Adam').first()
        self.assertEqual(acad.name, 'Adam')
        self.assertEqual(acad.current_institution, 'Uni')
        self.assertEqual(acad.field_of_study, 'Science')
    
    


