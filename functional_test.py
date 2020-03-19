# functional_test.py
import unittest

from selenium import webdriver

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_and_retrieve_a_list(self):
        self.browser.get('http://localhost:8000/froyo')
        self.assertIn('Froyo', self.browser.title)
        self.fail('Finish the Test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
