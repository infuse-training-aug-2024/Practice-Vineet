from selenium.webdriver import Chrome,Edge
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_driver_path = r'C:\Users\sawan\Desktop\infuse\Practice-Vineet\selenium-exercise\drivers\chromedriver-win64\chromedriver.exe'

edge_driver_path = r'C:\Users\sawan\Desktop\infuse\Practice-Vineet\selenium-exercise\drivers\edgedriver_win64\msedgedriver.exe'
browser=""
 
def chrome_setup():
    global browser
    chrome_service=Service(executable_path=chrome_driver_path)
    chrome_driver=Chrome(service=chrome_service)
    browser = "Chrome"
    return chrome_driver
 
def edge_setup():
    global browser
    edge_service=Service(executable_path=edge_driver_path)
    edge_driver=Edge(service=edge_service)
    browser = "Edge"
    return edge_driver
 
def get_automationID(driver):
    string = driver.find_element(By.ID, browser.lower()).get_attribute("automation-id")
    print(string)
 
def get_rectangle_text(driver):
    return driver.find_element(By.ID, 'js-test')
 
try:
 
    chrome_driver = chrome_setup()
    chrome_driver.get("https://joyrel-vaz.github.io/cross-browser-testing/")
    rectangle = get_rectangle_text(chrome_driver)
    if chrome_driver.capabilities['browserName'].lower() in rectangle.text.lower():
        print("Chrome Browser Passed")
        get_automationID(chrome_driver)
    else:
        print("error")
    chrome_driver.quit()
 
    edge_driver = edge_setup()
    edge_driver.get("https://joyrel-vaz.github.io/cross-browser-testing/")
    rectangle = get_rectangle_text(edge_driver)
    if browser.lower() in rectangle.text.lower():
        print("Edge Browser Passed")
        get_automationID(edge_driver)
    else:
        print("error")      
    edge_driver.quit()
 
except Exception as e:
    print(e)