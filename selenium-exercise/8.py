
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
    
    
    driver.get('https://www.globalsqa.com/demo-site/sliders/#Steps')
    driver.maximize_window()

    iframe = driver.find_element(By.XPATH, value='/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[3]/p/iframe')
    driver.switch_to.frame(iframe)

    slider = driver.find_element(By.ID, value='slider')
    handler = slider.find_element(By.CLASS_NAME, value='ui-slider-handle')

    action = ActionChains(driver)
    action.click_and_hold(handler).move_by_offset(100, 0).release().perform()

    amount_value = driver.find_element(By.ID, value='amount')
    print(f"amount : {amount_value.get_attribute('value')}")
    sleep(3)
    
    driver.switch_to.default_content()

    
except WebDriverException as e:
    print(f"Error occurred: {e}")
finally:
    driver.quit()
