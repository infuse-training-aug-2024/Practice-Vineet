from DriverClass import DriverClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import Select

class Framework:
    def __init__(self, browser='chrome'):
        try:
            if browser.lower() == 'chrome':
                self.driver = DriverClass("chrome").initialize_driver()
            elif browser.lower() == 'firefox':
                self.driver = DriverClass("firefox").initialize_driver()
            elif browser.lower() == 'edge':
                self.driver = DriverClass("edge").initialize_driver()
            else:
                raise ValueError("Unsupported browser. Choose 'chrome', 'firefox', or 'edge'.")

            self.wait = WebDriverWait(self.driver, 10)
        except WebDriverException as e:
            raise Exception(f"Failed to initialize WebDriver: {str(e)}")

    def _get_by_type(self, locator: dict):

        by_type = locator.get("by")
        value = locator.get("value")

        if by_type == "id":
            return By.ID, value
        elif by_type == "xpath":
            return By.XPATH, value
        elif by_type == "name":
            return By.NAME, value
        elif by_type == "class_name":
            return By.CLASS_NAME, value
        elif by_type == "css_selector":
            return By.CSS_SELECTOR, value
        elif by_type == "tag_name":
            return By.TAG_NAME, value
        elif by_type == "link_text":
            return By.LINK_TEXT, value
        elif by_type == "partial_link_text":
            return By.PARTIAL_LINK_TEXT, value
        else:
            raise ValueError("Invalid locator type")

    def open_url(self, url):
        try:
            self.driver.get(url)
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            return self.driver.title
        except Exception as e:
            print(f"Error Navigating to URL{str(e)}")
            return "ErrorLoadingPage"

    def find_element(self, locator: dict):
        try:
            return self.wait.until(EC.presence_of_element_located(self._get_by_type(locator)))
        except Exception as e:
            print(f'Error while finding element: {e}')
            return False
        
    def find_elements(self, locator: dict):
        try:
            by, value = self._get_by_type(locator)
            return self.wait.until(EC.presence_of_all_elements_located((by, value)))
        except Exception as e:
            print(f'Error while finding elements: {e}')
            return []

        

    def click_element(self, locator: dict):
        try:
            element = self.wait.until(EC.element_to_be_clickable(self._get_by_type(locator)))
            element.click()
            return True
        except Exception as e:
           print(f"Failed to click element with {locator['by']}: {locator['value']}. Error: {str(e)}")
           return False

    def input_text(self, locator: dict, text):

        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
            return True
        except Exception as e:
            print(f"Failed to input text into element with {locator['by']}: {locator['value']}. Error: {str(e)}")
            return False
        
    def is_element_displayed(self, locator: dict)->bool:
        try:
            return self.wait.until(EC.visibility_of_element_located(self._get_by_type(locator))) is not None
        except Exception as e:
            print(f'Error while checking element visibility: {e}')
            return False
    
    def is_element_present(self, locator: dict):
        try:
            return self.wait.until(EC.visibility_of_element_located(self._get_by_type(locator))) is not None
        except Exception as e:
            print(f'Error while checking element visibility: {e}')
            return False

    def get_element_text(self, locator: dict):
        try:
            element = self.wait.until(EC.presence_of_element_located(self._get_by_type(locator)))
            text = element.text if element.text else element.get_attribute("value")
            return text
        except Exception as e:
            print(f"Failed to get text from element with {locator['by']}: {locator['value']}. Error: {str(e)}")
            return "" 

    def wait_for_element(self, locator: dict, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(self._get_by_type(locator)))
            return True
        except Exception:
            return False

    def select_dropdown_option_by_visible_text(self, locator: dict, option_text):
    
        try:
            dropdown_element = self.find_element(locator)
            if dropdown_element:
                select = Select(dropdown_element)
                select.select_by_visible_text(option_text)
            return True
        except Exception as e:
            print(f'Error while selecting dropdown: {e}')
            return False
        
    def wait_for_element_to_be_clickable(self, locator: dict):
        try:
            element = self.wait.until(EC.element_to_be_clickable(self._get_by_type(locator)))
            return element
        except Exception as e:
            print(f'Error while waiting for element to be clickable: {e}')
            return None

    def close_browser(self):
        try:
            self.driver.quit()
        except WebDriverException as e:
            print(f"Warning: Failed to close browser properly. Error: {str(e)}")
