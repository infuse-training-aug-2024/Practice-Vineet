from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import WebDriverException
from time import sleep

driver_path = r'C:\Users\sawan\Desktop\infuse\Practice-Vineet\selenium-exercise\drivers\chromedriver-win64\chromedriver.exe'
chrome_service = ChromeService(executable_path=driver_path)


try:
    driver = Chrome(service=chrome_service)
    driver.get('https://www.google.com')
    title = driver.title
    print(f"Title: {title}")
    assert title
except WebDriverException as e:
    print(f"Error occurred: {e}")
finally:
    driver.quit()