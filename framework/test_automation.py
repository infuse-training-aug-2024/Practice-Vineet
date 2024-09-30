import unittest
import json
from DriverClass import DriverClass
from framework import Framework

class TestSwagLabs(unittest.TestCase):
    base_url = 'https://www.saucedemo.com/'

    def initialize_test(self):
        return Framework(browser='chrome')
    
    def setUp(self):
        self.framework = self.initialize_test()
        self.load_config()
    
    def tearDown(self):
        self.framework.close_browser()
    
    def load_config(self):
        with open('config.json') as config_file:
            config = json.load(config_file)
            self.username = config['username']
            self.password = config['password']

    def login(self):
        self.framework.open_url(self.base_url)
        self.framework.input_text({'by': 'id', 'value': 'user-name'}, self.username)
        self.framework.input_text({'by': 'id', 'value': 'password'}, self.password)
        self.framework.click_element({'by': 'id', 'value': 'login-button'})
        return self.framework.is_element_displayed({'by': 'class_name', 'value': 'inventory_item'})

    def test_login(self):
        login_success = self.login()
        self.assertTrue(login_success, 'Login failed')

    def test_sorting_by_price_high_to_low(self):
        self.assertTrue(self.login())
        self.framework.select_dropdown_option_by_visible_text({'by': 'class_name', 'value': 'product_sort_container'}, 'Price (high to low)')
        prices_elements = self.framework.find_elements({'by': 'class_name', 'value': 'inventory_item_price'})
        prices = [float(price.text.replace('$', '')) for price in prices_elements]
        self.assertTrue(prices == sorted(prices, reverse=True), 'Failed to sort from high to low')

    def test_sorting_by_price_low_to_high(self):
        self.assertTrue(self.login())
        self.framework.select_dropdown_option_by_visible_text({'by': 'class_name', 'value': 'product_sort_container'}, 'Price (low to high)')
        prices_elements = self.framework.find_elements({'by': 'class_name', 'value': 'inventory_item_price'})
        prices = [float(price.text.replace('$', '')) for price in prices_elements]
        self.assertTrue(prices == sorted(prices), 'Failed to sort from low to high')

    def test_add_product_to_cart(self):
        self.assertTrue(self.login())
        product_name = self.framework.get_element_text({'by': 'class_name', 'value': 'inventory_item_name'})
        self.framework.click_element({'by': 'css_selector', 'value': '.inventory_item:first-child button'})
        self.framework.click_element({'by': 'class_name', 'value': 'shopping_cart_link'})
        cart_product_name = self.framework.get_element_text({'by': 'class_name', 'value': 'inventory_item_name'})
        self.assertEqual(product_name, cart_product_name, 'Failed to add product to cart')

    def test_logout(self):
        self.assertTrue(self.login())
        self.framework.click_element({'by': 'id', 'value': 'react-burger-menu-btn'})
        self.framework.click_element({'by': 'id', 'value': 'logout_sidebar_link'})
        login_present = self.framework.is_element_displayed({'by': 'id', 'value': 'login-button'})
        self.assertTrue(login_present, 'Failed to logout')
    
    def test_checkout(self):
        self.assertTrue(self.login())
        self.framework.click_element({'by': 'css_selector', 'value': '.inventory_item:first-child button'})
        self.framework.click_element({'by': 'class_name', 'value': 'shopping_cart_link'})
        self.framework.click_element({'by': 'class_name', 'value': 'checkout_button'})
        self.framework.input_text({'by': 'id', 'value': 'first-name'}, 'John')
        self.framework.input_text({'by': 'id', 'value': 'last-name'}, 'Doe')
        self.framework.input_text({'by': 'id', 'value': 'postal-code'}, '000000')
        self.framework.click_element({'by': 'id', 'value': 'continue'})
        self.framework.click_element({'by': 'id', 'value': 'finish'})
        complete_msg = self.framework.get_element_text({'by': 'class_name', 'value': 'complete-header'})
        self.assertEqual(complete_msg, 'Thank you for your order!', 'Failed to checkout')

if __name__ == '__main__':
    unittest.main()
