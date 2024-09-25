from selenium.common.exceptions import WebDriverException
from DriversClass import DriverClass

try:
    driver = DriverClass("Chrome").initialize_driver()
    driver.get('https://www.google.com')
    title = driver.title
    print(f"Title: {title}")
    print("Executed Successfully!")
except WebDriverException as e:
    print(f"Error occurred: {e}")
finally:
    driver.quit()