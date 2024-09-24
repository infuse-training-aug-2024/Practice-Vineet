from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from DriversClass import DriverClass

try:
    driver = DriverClass("Chrome").initialize_driver()
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

    print("Executed Successfully!")

    
except WebDriverException as e:
    print(f"Error occurred: {e}")
finally:
    driver.quit()
