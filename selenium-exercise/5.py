from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from DriversClass import DriverClass

try:
    driver = DriverClass("Chrome").initialize_driver()
    driver.get('https://www.yahoo.com/')
    driver.maximize_window()
    text_box = driver.find_element(by=By.ID, value="ybar-sbq")
    submit_button = driver.find_element(by=By.ID, value="ybar-search")

    text_box.send_keys("Nutty Putty Cave")
 
    submit_button.click()

    print("Executed Successfully!")

except WebDriverException as e:
    print(f"Error occurred: {e}")
finally:

    driver.quit()
