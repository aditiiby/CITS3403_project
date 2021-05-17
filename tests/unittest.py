import unittest, os
from app import app, db, User


class UserModelCase(unittest.TestCase):

  def setUp(self):
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI']=\
        'sqlite:///'+os.path.join(basedir,'test.db')
    self.app = app.test_client()#creates a virtual test environment
    db.create_all()
    s1 = User(username='TestCase', password = 'TestPassword', email = 'testcase@gmail.com')
    s2 = User(username='UnitCase', password = 'UnitPassword', email = 'otherdude@gmail.com')
    db.session.add(s1)
    db.session.add(s2)
    db.session.commit()

  def tearDown(self):
    db.session.remove()
    db.drop_all()

  def test_user(self):
    s = User.query.filter_by(username='TestCase')
    self.assertFalse(s.email('testcase@gmail.com'))
    self.assertTrue(s.email('otherdude@gmail.com'))



