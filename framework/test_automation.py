import unittest
import json
import os
from framework import Framework
from selenium.common.exceptions import WebDriverException, TimeoutException, NoSuchElementException

class TestSwagLabs(unittest.TestCase):
    base_url = 'https://www.saucedemo.com/'

    def initialize_test(self):
        try:
            return Framework(browser='chrome')
        except WebDriverException as e:
            self.fail(f"Failed to initialize the test framework: {str(e)}")
    
    def setUp(self):
        self.framework = self.initialize_test()
        self.load_config()
    
    def tearDown(self):
        try:
            self.framework.close_browser()
        except WebDriverException as e:
            print(f"Error closing the browser: {str(e)}")
    
    def load_config(self):
        try:
            if not os.path.exists('config.json'):
                self.fail("config.json file not found.")
            
            with open('config.json') as config_file:
                config = json.load(config_file)
                self.username = config['username']
                self.password = config['password']
        except (json.JSONDecodeError, KeyError) as e:
            self.fail(f"Error loading config.json: {str(e)}")

    def login(self):
        try:
            self.framework.open_url(self.base_url)
            self.framework.input_text({'by': 'id', 'value': 'user-name'}, self.username)
            self.framework.input_text({'by': 'id', 'value': 'password'}, self.password)
            self.framework.click_element({'by': 'id', 'value': 'login-button'})
            return self.framework.is_element_displayed({'by': 'class_name', 'value': 'inventory_item'})
        except (TimeoutException, NoSuchElementException, WebDriverException) as e:
            self.fail(f"Login failed due to an error: {str(e)}")
            return False

    def test_login(self):
        login_success = self.login()
        self.assertTrue(login_success, 'Login failed')

    def test_sorting_by_price_high_to_low(self):
        self.assertTrue(self.login(), "Login failed")
        try:
            self.framework.select_dropdown_option_by_visible_text({'by': 'class_name', 'value': 'product_sort_container'}, 'Price (high to low)')
            prices_elements = self.framework.find_elements({'by': 'class_name', 'value': 'inventory_item_price'})
            prices = [float(price.text.replace('$', '')) for price in prices_elements]
            self.assertTrue(prices == sorted(prices, reverse=True), 'Failed to sort from high to low')
        except (ValueError, WebDriverException) as e:
            self.fail(f"Error during sorting by price high to low: {str(e)}")

    def test_sorting_by_price_low_to_high(self):
        self.assertTrue(self.login(), "Login failed")
        try:
            self.framework.select_dropdown_option_by_visible_text({'by': 'class_name', 'value': 'product_sort_container'}, 'Price (low to high)')
            prices_elements = self.framework.find_elements({'by': 'class_name', 'value': 'inventory_item_price'})
            prices = [float(price.text.replace('$', '')) for price in prices_elements]
            self.assertTrue(prices == sorted(prices), 'Failed to sort from low to high')
        except (ValueError, WebDriverException) as e:
            self.fail(f"Error during sorting by price low to high: {str(e)}")

    def test_add_product_to_cart(self):
        self.assertTrue(self.login(), "Login failed")
        try:
            product_name = self.framework.get_element_text({'by': 'class_name', 'value': 'inventory_item_name'})
            self.framework.click_element({'by': 'css_selector', 'value': '.inventory_item:first-child button'})
            self.framework.click_element({'by': 'class_name', 'value': 'shopping_cart_link'})
            cart_product_name = self.framework.get_element_text({'by': 'class_name', 'value': 'inventory_item_name'})
            self.assertEqual(product_name, cart_product_name, 'Failed to add product to cart')
        except (NoSuchElementException, WebDriverException) as e:
            self.fail(f"Error adding product to cart: {str(e)}")

    def test_logout(self):
        self.assertTrue(self.login(), "Login failed")
        try:
            self.framework.click_element({'by': 'id', 'value': 'react-burger-menu-btn'})
            self.framework.click_element({'by': 'id', 'value': 'logout_sidebar_link'})
            login_present = self.framework.is_element_displayed({'by': 'id', 'value': 'login-button'})
            self.assertTrue(login_present, 'Failed to logout')
        except (NoSuchElementException, WebDriverException) as e:
            self.fail(f"Error during logout: {str(e)}")

    def test_checkout(self):
        self.assertTrue(self.login(), "Login failed")
        try:
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
        except (NoSuchElementException, WebDriverException) as e:
            self.fail(f"Error during checkout: {str(e)}")

if __name__ == '__main__':
    unittest.main()
