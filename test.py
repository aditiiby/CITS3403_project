import unittest, os
from app import app, db, User

class scoreModelTest(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
        db.create_all()
        user1 = User(username="Testcase", password="kasjdnfkasj", email="example@gmail.com", carbonResults=50)
        db.session.add(user1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_result(self):
        user1 = User.query.filter_by(username="Testcase").first()
        self.assertFalse(user1.carbonResults == 10)
        self.assertTrue(user1.carbonResults == 60)

if __name__=='__main__':
    unittest.main(verbosity = 2)