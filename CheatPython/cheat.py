from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path='./driver/geckodriver.exe')
driver = webdriver.Firefox(service=service)
X = 'X'
O = 'O'
EMPTY = ' '
board = [[EMPTY for _ in range(3)] for _ in range(3)]
score = [0,0]   # X,O

def main():
  load()
  set_clickables()
  btns[0].click()
  # Minimax() 3x3 list of lists
  for i in range(200):
    update_board()
    print(board)
    time.sleep(1)
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

def set_clickables():
  global btns
  global restart_button
  btns = [None] * 9
    
  wait = WebDriverWait(driver, 2)
  for i in range(3):
    for j in range(3):
      btns[i * 3 + j] = wait.until(EC.presence_of_element_located(
        (By.XPATH, f"//td[@jsname='WfZakb' and @data-col='{j}' and @data-row='{i}']")
      ))
  restart_buttons = wait.until(EC.presence_of_all_elements_located(
    (By.CLASS_NAME, 'lv7K9c')
  ))
  if len(restart_buttons) > 2:
    restart_button = restart_buttons[2]

def update_board():   
  for i in range(3):
    for j in range(3):
      x_css_selector = f"td[jsname='WfZakb'][data-col='{j}'][data-row='{i}'] svg[jsname='uECznc']"
      o_css_selector = f"td[jsname='WfZakb'][data-col='{j}'][data-row='{i}'] svg[jsname='D7yUae']"
      x_element = driver.find_element(By.CSS_SELECTOR, x_css_selector)
      o_element = driver.find_element(By.CSS_SELECTOR, o_css_selector)
      
      if x_element.is_displayed():
        board[i][j] = X
      elif o_element.is_displayed():
        board[i][j] = O
      else:
        board[i][j] = EMPTY
  return board

def check_score():
  x_score_element = driver.find_element(By.XPATH, "//span[@jsname='AvUL5b']")
  o_score_element = driver.find_element(By.XPATH, "//span[@jsname='H3g9pe']")
  print(x_score_element.text)
  print(o_score_element.text)

def restart():
  restart_button.click()

if __name__ == "__main__":
  main()