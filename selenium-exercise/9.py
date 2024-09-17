
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
    
    
    driver.get('https://cosmocode.io/automation-practice-webtable/ ')
    driver.maximize_window()

    table = driver.find_element(By.TAG_NAME, value='tbody')
    row = table.find_elements(By.TAG_NAME, value='tr')
    row_elements = row[0].find_elements(By.TAG_NAME, 'td')

    for i in row_elements:
        print(i.text)


    
except WebDriverException as e:
    print(f"Error occurred: {e}")
finally:
    driver.quit()
