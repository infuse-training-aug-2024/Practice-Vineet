
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select

from time import sleep

driver_path = r'C:\Users\sawan\Desktop\infuse\Practice-Vineet\selenium-exercise\drivers\chromedriver-win64\chromedriver.exe'

try:
    chrome_service = ChromeService(executable_path=driver_path)
    driver = Chrome(service=chrome_service)
    
    
    driver.get('https://letcode.in/forms')
    driver.maximize_window()

    select_country = driver.find_element(By.XPATH, value='/html/body/app-root/app-forms/section[1]/div/div/div[1]/div/div/form/div[5]/div[2]/div/div/div/select')

    select = Select(select_country)
    options = select.options

    print("List of dropdown options: ")
    for option in options: 
        print(option.text)

    
except WebDriverException as e:
    print(f"Error occurred: {e}")
finally:
    sleep(2)
    driver.quit()
