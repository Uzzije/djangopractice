import unittest
from selenium import webdriver
from django.test import LiveServerTestCase
import django
django.setup()
from webtest import TestApp
from django_webtest import WebTest

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        #learn how to set up for funcitonal Test.
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_case(self):
        #New user is excited about creating a blog post so they come to our website
        self.browser.get(self.live_server_url + '/first_blog')
        #They are new so they have to aregister
        #They notice that there is a Sign up button
        self.assertIn('Blog Home', self.browser.title)
        sign_up_button = self.browser.find_element_by_name('sign_up')
        self.assertEqual(sign_up_button.get_attribute('name'), 'Sign Up')
        #They click the Sign up button and it redirects them to a home page

if __name__ == '__main__':
    unittest.main(warnings='ignore')





