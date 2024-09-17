
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select

from time import sleep

driver_path = r'C:\Users\sawan\Desktop\infuse\Practice-Vineet\selenium-exercise\drivers\chromedriver-win64\chromedriver.exe'
def select_ith_item_from_dropdown(i):
    try:
        chrome_service = ChromeService(executable_path=driver_path)
        driver = Chrome(service=chrome_service)
        
        driver.get('https://testpages.herokuapp.com/styled/basic-html-form-test.html')
        driver.maximize_window()

        select_element = driver.find_element(By.NAME, value="dropdown")
        select = Select(select_element)
        
        if(i < 0 or i >= len(select.options)):
            print(f"{i} position is invalid")
            return 
        else:
            selected_value = select.options[i].get_attribute('value')
            return selected_value
            
    except WebDriverException as e:
        print(f"Error occurred: {e}")
    finally:
        driver.quit()


print(select_ith_item_from_dropdown(2))