
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver_path = r'C:\Users\sawan\Desktop\infuse\Practice-Vineet\selenium-exercise\drivers\chromedriver-win64\chromedriver.exe'

try:
    chrome_service = ChromeService(executable_path=driver_path)
    driver = Chrome(service=chrome_service)
    
    
    driver.get('https://the-internet.herokuapp.com/tables ')
    driver.maximize_window()

    table = driver.find_element(By.ID, value='table1')
    tbody = table.find_element(By.TAG_NAME, value='tbody')
    rows = tbody.find_elements(By.TAG_NAME, value='tr')
    data = rows[1].find_elements(By.TAG_NAME,value='td')

    print(data[2].text) #gets the email from the cell


    
except WebDriverException as e:
    print(f"Error occurred: {e}")
finally:
    driver.quit()
