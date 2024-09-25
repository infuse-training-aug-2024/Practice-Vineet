from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from DriversClass import DriverClass

try:
    driver = DriverClass("Chrome").initialize_driver()

    driver.get('https://demo.automationtesting.in/Register.html')
    driver.maximize_window()

    radio_btn_value = '#basicBootstrapForm > div:nth-child(5) > div > label:nth-child(1) > input'
    radio_btn = driver.find_element(By.CSS_SELECTOR, value=radio_btn_value)
    check_box_1 = driver.find_element(By.ID, value="checkbox2")
    check_box_2 = driver.find_element(By.ID, value="checkbox3")

    radio_btn.click()
    check_box_1.click()
    check_box_2.click()    

    print("Executed Successfully!")


except WebDriverException as e:
    print(f"Error occurred: {e}")
finally:
    driver.quit()
