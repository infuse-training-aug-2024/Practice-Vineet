from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import WebDriverException

from time import sleep

driver_path = r'C:\Users\sawan\Desktop\infuse\Practice-Vineet\selenium-exercise\drivers\chromedriver-win64\chromedriver.exe'

try:
    chrome_service = ChromeService(executable_path=driver_path)
    driver = Chrome(service=chrome_service)
    
    
    driver.get('https://www.yahoo.com/')
    driver.maximize_window()
    text_box = driver.find_element(by=By.ID, value="ybar-sbq")
    submit_button = driver.find_element(by=By.ID, value="ybar-search")

    text_box.send_keys("Nutty Putty Cave")
    sleep(2)

    submit_button.click()
    sleep(5)
    
except WebDriverException as e:
    print(f"Error occurred: {e}")
finally:
    sleep(5)
    driver.quit()
