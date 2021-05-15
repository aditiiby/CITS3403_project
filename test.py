import unittest

from app import User


class UserModelTest(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username ='james123', password="james123")
        self.assertFalse(u.login('josh'))
        self.assertTrue(u.login('james123'))

if __name__=='__main__':
    unittest.main(verbosity = 2)