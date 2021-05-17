import unittest, os
from app import app, db, User

class scoreModelTest(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        db.create_all()
        user1 = User(username="Testcase", password="kasjdnfkasj", email="example@gmail.com", hydrogenResults = 50, heliumResults= 50, carbonResults=50, nitrogenResults=50, oxygenResults=50, ironResults=50)
        db.session.add(user1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_result(self):
        user1 = User.query.filter_by(username="Testcase").first()
        self.assertFalse(user1.hydrogenResults == 10)
        self.assertFalse(user1.heliumResults == 10)
        self.assertFalse(user1.carbonResults == 10)
        self.assertFalse(user1.nitrogenResults == 10)
        self.assertFalse(user1.oxygenResults == 10)
        self.assertFalse(user1.ironResults == 10)
        self.assertTrue(user1.hydrogenResults == 50)
        self.assertTrue(user1.heliumResults == 50)
        self.assertTrue(user1.carbonResults == 50)
        self.assertTrue(user1.nitrogenResults == 50)
        self.assertTrue(user1.oxygenResults == 50)
        self.assertTrue(user1.ironResults == 50)


if __name__=='__main__':
    unittest.main(verbosity = 2)