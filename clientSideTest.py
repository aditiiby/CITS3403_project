import unittest, os, time 
from unittest.case import SkipTest
from app import app, db, User
from selenium import webdriver
import time


class scoreModelTest(unittest.TestCase):
    driver = None
    def setUp(self):
        self.driver = webdriver.chrome(executable_path = "./")
        if not self.driver:
            self.SkipTest("An error occured when opening the browser")
        else:
            db.init_app(app)
            db.create_all()

            user1 = User(username="Testcase", password="kasjdnfkasj", email="example@gmail.com", hydrogenResults = 50, heliumResults= 50, carbonResults=50, nitrogenResults=50, oxygenResults=50, ironResults=50)
            db.session.add(user1)
            db.session.commit()
            self.driver.maximize_window()
            self.driver.get('http://127.0.0.1:5000/')


    def tearDown(self):
        if self.driver:
            self.driver.close()
            db.session.query(User).delete()
            db.session.remove()
            db.drop_all()

    def test_result(self):
        user1 = User.query.filter_by(username="Testcase").first()
        self.assertEqual(user1.email, 'example@gmail.com', msg= 'emails add up')
        self.driver.implicitly_wait(5)
        username_send = self.driver.find_element_by_id("username")
        username_send.send_keys('UserTester')
        password_send = self.driver.find_element_by_id("password")
        password_send.send_keys('TestPassword')
        email_send = self.driver.find_element_by_id("email")
        email_send.send_keys('Test@gmail.com')
        time.sleep(1)
        self.driver.implicitly_wait(5)
        submit = self.driver.find_element_by_id("submit")
        submit.click()


if __name__=='__main__':
    unittest.main(verbosity = 2)

        

