from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select
from DriversClass import DriverClass

def check_position(i, select):
    if(i < 0 or i >= len(select.options)):
        print(f"{i} position is invalid")
        return 
    else:
        selected_value = select.options[i].get_attribute('value')
        return selected_value

def select_ith_item_from_dropdown(i):
    try:
        driver = DriverClass("Chrome").initialize_driver()

        driver.get('https://testpages.herokuapp.com/styled/basic-html-form-test.html')
        driver.maximize_window()

        select_element = driver.find_element(By.NAME, value="dropdown")
        select = Select(select_element)

        ans = check_position(i, select)
        print(ans)

        print("Executed Successfully!")

            
    except WebDriverException as e:
        print(f"Error occurred: {e}")
    finally:
        driver.quit()


print(select_ith_item_from_dropdown(2))