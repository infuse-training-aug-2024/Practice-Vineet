from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from DriversClass import DriverClass

try:
    driver = DriverClass("Chrome").initialize_driver()
    driver.get('https://www.globalsqa.com/demo-site/sliders/#Steps')
    driver.maximize_window()

    val = '/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[3]/p/iframe'
    iframe = driver.find_element(By.XPATH, value=val)
    driver.switch_to.frame(iframe)

    slider = driver.find_element(By.ID, value='slider')
    handler = slider.find_element(By.CLASS_NAME, value='ui-slider-handle')

    action = ActionChains(driver)
    action.click_and_hold(handler).move_by_offset(100, 0).release().perform()

    amount_value = driver.find_element(By.ID, value='amount')
    print(f"amount : {amount_value.get_attribute('value')}")
    
    driver.switch_to.default_content()

    print("Executed Successfully!")

except WebDriverException as e:
    print(f"Error occurred: {e}")
finally:
    driver.quit()
