from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path='./driver/geckodriver.exe')
driver = webdriver.Firefox(service=service)

def main():
  load()
  setClickables()
  bestFirstMove = driver.find_element(By.XPATH, "//td[@jsname='WfZakb' and @data-col='0']")
  bestFirstMove.click()
  time.sleep(2)

  time.sleep(20)
  driver.quit()

def load():
  driver.get("https://www.google.com/search?q=tic+tac+toe")
  WebDriverWait(driver, 1).until(
    lambda d: d.execute_script("return document.readyState") == "complete"
  )
  div = driver.find_element(By.CSS_SELECTOR, "div.QS5gu.sy4vM")
  div.click()
  time.sleep(2)

def setClickables():
  global restart_button
  global btn1
  global btn2
  global btn3
  global btn4
  global btn5
  global btn6
  global btn7
  global btn8
  global btn9
  restart_button = driver.find_elements(By.CLASS_NAME, 'lv7K9c')[2]

def restart():
  restart_button.click()

if __name__ == "__main__":
  main()