from selenium.webdriver import Chrome
from selenium.webdriver import Edge
from selenium.webdriver import Firefox 
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

class DriverClass:
    browser = ""

    def __init__(self, seleted_browser="chrome"):
        self.browser = seleted_browser

    def initialize_driver(self):
        if self.browser == "chrome":
            driver_path = r'C:\Users\sawan\Desktop\infuse\Practice-Vineet\framework\drivers\chromedriver-win64\chromedriver.exe'
            chrome_service = ChromeService(executable_path = driver_path)
            driver = Chrome(service=chrome_service)

            return driver

        elif self.browser == "edge":
            driver_path = r'C:\Users\sawan\Desktop\infuse\Practice-Vineet\framework\drivers\edgedriver_win64\msedgedriver.exe'
            edge_service = EdgeService(executable_path=driver_path)
            driver = Edge(service=edge_service)

            return driver

        elif self.browser == "firefox":
            driver_path = r'C:\Users\sawan\Desktop\infuse\Practice-Vineet\framework\drivers\geckodriver-v0.35.0-win-aarch64\geckodriver.exe'
            firefox_service = FirefoxService(executable_path=driver_path)
            driver = Firefox(service=firefox_service)

            return driver

        else:
            print("The selected browser driver is not available.")


        