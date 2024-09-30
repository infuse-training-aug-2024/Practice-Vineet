import unittest
from selenium.webdriver.common.by import By
from framework import Framework

class TestFramework(unittest.TestCase):

    _LINK = "https://artoftesting.com/samplesiteforselenium"

    def setUp(self):
        self.framework = Framework(browser='chrome')
        self.framework.open_url(self._LINK)

    def test_open_url(self):
        title = self.framework.open_url(self._LINK)
        self.assertTrue(title, "Sample page for Selenium Automation")

    def test_find_element_valid(self):
        self.framework.open_url(self._LINK)
        locator = {"by": "tag_name", "value": "h1"}
        element = self.framework.find_element(locator)
        self.assertIsNotNone(element)
    
    def test_find_element_invalid(self):
        self.framework.open_url(self._LINK)
        locator = {"by": "tag_name", "value": "invalid-h1"} # invalid-h1 --> error
        element = self.framework.find_element(locator)
        self.assertFalse(element)

    def test_find_elements_valid(self):
        self.framework.open_url(self._LINK)
        locator = {"by": "tag_name", "value": "div"}
        element = self.framework.find_elements(locator)
        self.assertTrue(element)
    
    def test_find_elements_invalid(self):
        self.framework.open_url(self._LINK)
        locator = {"by": "id", "value": "invalid"}
        element = self.framework.find_elements(locator)
        # self.assertIsNone(element,[])0.
        self.assertFalse(element)

    def test_click_element_valid(self):
        self.framework.open_url(self._LINK)
        locator = {"by": "id", "value": "menu-item-102"}
        success = self.framework.click_element(locator)
        self.assertTrue(success)
    
    def test_click_element_invalid(self):
        self.framework.open_url(self._LINK)
        locator = {"by": "css_selector", "value": "invalid"} #menuu -->error
        failure = self.framework.click_element(locator)
        self.assertFalse(failure)

    def test_input_text_valid(self):
        self.framework.open_url(self._LINK)
        locator = {"by": "name", "value": "firstName"}
        text = "test_user"
        input_text = self.framework.input_text(locator, text)
        self.assertTrue(input_text)

    def test_input_text_invalid(self):
        self.framework.open_url(self._LINK)
        locator = {"by": "name", "value": "invalid"}
        text = "test_user"
        input_text = self.framework.input_text(locator, text)
        self.assertFalse(input_text)

    def test_get_element_text_valid(self):
        self.framework.open_url(self._LINK)
        locator = {"by": "css_selector", "value": "#idOfDiv > p > b"}
        text = self.framework.get_element_text(locator)
        self.assertEqual(text, "This is sample text!")
    
    def test_get_element_text_invalid(self):
        self.framework.open_url(self._LINK)
        locator = {"by": "css_selector", "value": "invalid"}
        text = self.framework.get_element_text(locator)
        self.assertEqual(text, "")

    def test_is_element_displayed_valid(self):
        self.framework.open_url(self._LINK)
        locator = {"by": "id", "value": "idOfButton"}
        is_displayed = self.framework.is_element_displayed(locator)
        self.assertTrue(is_displayed)

    def test_is_element_displayed_invalid(self):
        self.framework.open_url(self._LINK)
        locator = {"by": "id", "value": "invalid"}
        is_displayed = self.framework.is_element_displayed(locator)
        self.assertFalse(is_displayed)

    def test_is_element_present_valid(self):
        self.framework.open_url(self._LINK)
        locator = {"by": "id", "value": "idOfButton"}
        is_present = self.framework.is_element_present(locator)
        self.assertTrue(is_present, "Element is not present")
    
    def test_is_element_present_invalid(self):
        self.framework.open_url(self._LINK)
        locator = {"by": "id", "value": "invalid"}
        is_present = self.framework.is_element_present(locator)
        self.assertFalse(is_present)

    def test_select_dropdown_option_by_visible_text_valid(self):
        self.framework.open_url(self._LINK)
        locator = {"by": "id", "value": "testingDropdown"}
        option_text = "Performance Testing"
        success = self.framework.select_dropdown_option_by_visible_text(locator, option_text)
        self.assertTrue(success)
    
    def test_select_dropdown_option_by_visible_text_invalid(self):
        self.framework.open_url(self._LINK)
        locator = {"by": "id", "value": "testingDropdown"}
        option_text = "invalid option"
        failure = self.framework.select_dropdown_option_by_visible_text(locator, option_text)
        self.assertFalse(failure)

    
    def test_wait_for_element_to_be_clickable_valid(self):
        self.framework.open_url(self._LINK)
        locator = {"by": "id", "value": "idOfButton"}
        button = self.framework.wait_for_element_to_be_clickable(locator)
        self.assertIsNotNone(button)
    
    def test_wait_for_element_to_be_clickable_invalid(self):
        self.framework.open_url(self._LINK)
        locator = {"by": "id", "value": "invalid"}
        button = self.framework.wait_for_element_to_be_clickable(locator)
        self.assertIsNone(button)

    def tearDown(self):
        self.framework.close_browser()

if __name__ == "__main__":
    unittest.main()
