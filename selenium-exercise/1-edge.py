from selenium.webdriver import Edge
from selenium.webdriver.edge.service import Service as EdgeService
from time import sleep

driver_path = r'C:\Users\sawan\Desktop\infuse\Practice-Vineet\selenium-exercise\drivers\edgedriver_win64\msedgedriver.exe'
edge_service = EdgeService(executable_path=driver_path)
driver = Edge(service=edge_service)

driver.maximize_window()
sleep(2)
driver.quit()