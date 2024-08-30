from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path='./driver/geckodriver.exe')
driver = webdriver.Firefox(service=service)

driver.get("https://www.google.com/search?q=tic+tac+toe")

WebDriverWait(driver, 10).until(
    lambda d: d.execute_script("return document.readyState") == "complete"
)
time.sleep(6)

bestFirstMove = driver.find_element(By.XPATH, "//td[@jsname='WfZakb' and @data-col='0']")
bestFirstMove.click()
time.sleep(2)

elements = driver.find_elements(By.CLASS_NAME, '')
if len(elements) >= 3:
  elements[2].click()
else:
  print("Less than three elements found.")

print('clicked restart')
time.sleep(20)
driver.quit()
