from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from DriversClass import DriverClass

def login(driver):
    try:
        driver.find_element(By.ID, 'user-name').send_keys("standard_user")
        driver.find_element(By.ID, 'password').send_keys("secret_sauce")
        driver.find_element(By.ID, 'login-button').click()
    except Exception as e:
        print(e)
   
def add_product_to_cart(driver):
    items = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    second_item = items[1]
    cart_button = second_item.find_element(By.TAG_NAME, 'button')
    cart_button.click()
 
def remove_product(driver):
    items = driver.find_elements(By.CLASS_NAME, 'cart_item')
    try:
        remove_button = items[0].find_element(By.TAG_NAME, 'button')
        remove_button.click()
    except IndexError as e:
        print(e)
       
def filter_products(driver):
    header_section = driver.find_element(By.CLASS_NAME, 'header_secondary_container')
    filter_options = header_section.find_elements(By.TAG_NAME, 'option')
    filter_options[2].click()

def buy_product(driver):
    driver.find_element(By.ID, 'checkout').click()
    driver.find_element(By.ID, 'first-name').send_keys("aaa")
    driver.find_element(By.ID, 'last-name').send_keys("bbb")
    driver.find_element(By.ID, 'postal-code').send_keys("12345")
    driver.find_element(By.ID, 'continue').click()
    driver.find_element(By.ID, 'finish').click()
    driver.find_element(By.ID, 'back-to-products').click()

 
def go_to_cart(driver):
    driver.find_element(By.ID, 'shopping_cart_container').click()
 
try:
    driver = DriverClass("Chrome").initialize_driver()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
 
    login(driver)
    filter_products(driver)
    add_product_to_cart(driver)
    go_to_cart(driver)
    remove_product(driver)
   
    previous_page = driver.find_element(By.CLASS_NAME, 'cart_footer')
    previous_page_button = previous_page.find_element(By.TAG_NAME, 'button')
    previous_page_button.click()
 
    
    add_product_to_cart(driver)
    go_to_cart(driver)
    buy_product(driver)

    print("Executed Successfully!")
 
except Exception as e:
    print(e)