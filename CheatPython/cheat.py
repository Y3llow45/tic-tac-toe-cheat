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
time.sleep(10)

corner = driver.find_element(By.XPATH, "//td[@jsname='WfZakb']")
corner.click()
#driver.quit()
