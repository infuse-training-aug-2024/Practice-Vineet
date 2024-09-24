from DriversClass import DriverClass
from selenium.common.exceptions import WebDriverException

try: 
    driver = DriverClass("Chrome").initialize_driver()
    driver.maximize_window()
    print("Executed Successfully!")
except WebDriverException as e:
    print(f"Error occurred: {e}")
finally:
    driver.quit()
driver.quit()