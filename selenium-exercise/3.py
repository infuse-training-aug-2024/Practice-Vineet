from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from DriversClass import DriverClass

try:
    driver = DriverClass("Chrome").initialize_driver()
    driver.get('https:///www.yahoo.com/')
    driver.maximize_window()
    test_button = driver.find_element(By.ID,value="login-container")
    test_button.click()
    print("Executed Successfully!")
except WebDriverException as e:
    print(f"Error occurred: {e}")
finally:
    driver.quit()


