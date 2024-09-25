from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from DriversClass import DriverClass

try:
    driver = DriverClass("Chrome").initialize_driver()
    driver.get('https://cosmocode.io/automation-practice-webtable/ ')
    driver.maximize_window()

    table = driver.find_element(By.TAG_NAME, value='tbody')
    row = table.find_elements(By.TAG_NAME, value='tr')
    row_elements = row[0].find_elements(By.TAG_NAME, 'td')

    for i in row_elements:
        print(i.text)

    print("Executed Successfully!")
    

except WebDriverException as e:
    print(f"Error occurred: {e}")
finally:
    driver.quit()
