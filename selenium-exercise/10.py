
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
    
    
    driver.get('https://computer-database.gatling.io/computers')
    driver.maximize_window()
    
    col = []
    rows = driver.find_elements(By.TAG_NAME, value='tr')
    col_idx = 0
    for row in rows:
        header = row.find_elements(By.TAG_NAME, 'th')
        if(len(header) > col_idx):
            col.append(header[col_idx].text)
        
        cells = row.find_elements(By.TAG_NAME, 'td')
        if len(cells) > col_idx:
            col.append(cells[col_idx].text)
    
    print(f"Data from col {col_idx + 1}: {col}")
    
except WebDriverException as e:
    print(f"Error occurred: {e}")
finally:
    driver.quit()
