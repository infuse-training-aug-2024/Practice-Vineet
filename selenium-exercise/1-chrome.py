from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService

driver_path = r'C:\Users\sawan\Desktop\infuse\Practice-Vineet\selenium-exercise\drivers\chromedriver-win64\chromedriver.exe'
chrome_service = ChromeService(executable_path = driver_path)

driver = Chrome(service=chrome_service);

driver.maximize_window()
sleep(2)
driver.quit()