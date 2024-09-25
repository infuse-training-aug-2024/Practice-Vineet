from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from DriversClass import DriverClass
try:
    driver = DriverClass("Chrome").initialize_driver()
    driver.get('https://the-internet.herokuapp.com/tables ')
    driver.maximize_window()

    table = driver.find_element(By.ID, value='table1')
    tbody = table.find_element(By.TAG_NAME, value='tbody')
    rows = tbody.find_elements(By.TAG_NAME, value='tr')
    data = rows[1].find_elements(By.TAG_NAME,value='td')

    print(data[2].text) #gets the email from the cell

    print("Executed Successfully!")

except WebDriverException as e:
    print(f"Error occurred: {e}")
finally:
    driver.quit()
