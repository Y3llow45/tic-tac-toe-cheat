from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to geckodriver
service = Service(executable_path='/path/to/geckodriver')  # Update this path
driver = webdriver.Firefox(service=service)

driver.get("https://www.google.com/search?q=tic+tac+toe")

WebDriverWait(driver, 10).until(
    lambda d: d.execute_script("return document.readyState") == "complete"
)

corner = driver.find_element(By.XPATH, "//td[@jsname='WfZakb']")
corner.click()

driver.quit()
