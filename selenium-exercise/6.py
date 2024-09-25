from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select
from DriversClass import DriverClass

try:
    driver = DriverClass("Chrome").initialize_driver()

    driver.get('https://letcode.in/forms')
    driver.maximize_window()

    val = '/html/body/app-root/app-forms/section[1]/div/div/div[1]/div/div/form/div[5]/div[2]/div/div/div/select'
    select_country = driver.find_element(By.XPATH, value=val)

    select = Select(select_country)
    options = select.options

    print("List of dropdown options: ")
    for option in options: 
        print(option.text)
    
    print("Executed Successfully!")
    
except WebDriverException as e:
    print(f"Error occurred: {e}")
finally:
    driver.quit()
