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
        self.assertIn('The Good Place', self.browser.title)

        self.browser.get('http://localhost:8000/froyo/ingredients')
        self.assertIn('Ingredients', self.browser.title)
        detail = self.browser.find_element_by_id('list')
        self.assertEqual(detail.get_attribute('innerHTML'), 'Ingredients - List')
        detail = self.browser.find_element_by_id('detail')
        self.assertEqual(detail.get_attribute('innerHTML'), 'Ingredients - Detail')
        detail = self.browser.find_element_by_id('update')
        self.assertEqual(detail.get_attribute('innerHTML'), 'Ingredients - Update')
        detail = self.browser.find_element_by_id('create')
        self.assertEqual(detail.get_attribute('innerHTML'), 'Ingredients - Create')
        self.browser.get('http://localhost:8000/froyo/ingredients/list')
        self.assertIn('Ingredients - List', self.browser.title)
        self.browser.get('http://localhost:8000/froyo/ingredients/detail')
        self.assertIn('Ingredients - Detail', self.browser.title)
        self.browser.get('http://localhost:8000/froyo/ingredients/update')
        self.assertIn('Ingredients - Update', self.browser.title)
        self.browser.get('http://localhost:8000/froyo/ingredients/create')
        self.assertIn('Ingredients - Create', self.browser.title)

        self.browser.get('http://localhost:8000/froyo/recipes')
        self.assertIn('Recipes', self.browser.title)
        detail = self.browser.find_element_by_id('list')
        self.assertEqual(detail.get_attribute('innerHTML'), 'Recipes - List')
        detail = self.browser.find_element_by_id('detail')
        self.assertEqual(detail.get_attribute('innerHTML'), 'Recipes - Detail')
        detail = self.browser.find_element_by_id('update')
        self.assertEqual(detail.get_attribute('innerHTML'), 'Recipes - Update')
        detail = self.browser.find_element_by_id('create')
        self.assertEqual(detail.get_attribute('innerHTML'), 'Recipes - Create')
        self.browser.get('http://localhost:8000/froyo/recipes/list')
        self.assertIn('Recipes - List', self.browser.title)
        self.browser.get('http://localhost:8000/froyo/recipes/detail')
        self.assertIn('Recipes - Detail', self.browser.title)
        self.browser.get('http://localhost:8000/froyo/recipes/update')
        self.assertIn('Recipes - Update', self.browser.title)
        self.browser.get('http://localhost:8000/froyo/recipes/create')
        self.assertIn('Recipes - Create', self.browser.title)

        self.browser.get('http://localhost:8000/froyo/orders')
        self.assertIn('Orders', self.browser.title)
        detail = self.browser.find_element_by_id('list')
        self.assertEqual(detail.get_attribute('innerHTML'), 'Orders - List')
        detail = self.browser.find_element_by_id('detail')
        self.assertEqual(detail.get_attribute('innerHTML'), 'Orders - Detail')
        detail = self.browser.find_element_by_id('update')
        self.assertEqual(detail.get_attribute('innerHTML'), 'Orders - Update')
        detail = self.browser.find_element_by_id('create')
        self.assertEqual(detail.get_attribute('innerHTML'), 'Orders - Create')
        self.browser.get('http://localhost:8000/froyo/orders/list')
        self.assertIn('Orders - List', self.browser.title)
        self.browser.get('http://localhost:8000/froyo/orders/detail')
        self.assertIn('Orders - Detail', self.browser.title)
        self.browser.get('http://localhost:8000/froyo/orders/update')
        self.assertIn('Orders - Update', self.browser.title)
        self.browser.get('http://localhost:8000/froyo/orders/create')
        self.assertIn('Orders - Create', self.browser.title)
        
        self.fail('Finish the Test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
