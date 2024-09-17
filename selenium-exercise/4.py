from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import WebDriverException
#from selenium.webdriver import ActionChains

from time import sleep

driver_path = r'C:\Users\sawan\Desktop\infuse\Practice-Vineet\selenium-exercise\drivers\chromedriver-win64\chromedriver.exe'

try:
    chrome_service = ChromeService(executable_path=driver_path)
    driver = Chrome(service=chrome_service)
    #actions = ActionChains(driver)
    
    driver.get('https://demo.automationtesting.in/Register.html')
    driver.maximize_window()

    radio_btn = driver.find_element(By.CSS_SELECTOR, value='#basicBootstrapForm > div:nth-child(5) > div > label:nth-child(1) > input')
    check_box_1 = driver.find_element(By.ID, value="checkbox2")
    check_box_2 = driver.find_element(By.ID, value="checkbox3")

    # actions.click(radio_btn).click(check_box_1).click(check_box_2)
    radio_btn.click()
    check_box_1.click()
    check_box_2.click()
    
    
except WebDriverException as e:
    print(f"Error occurred: {e}")
finally:
    sleep(5)
    driver.quit()
