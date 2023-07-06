import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager

URL = "https://adventuretime.fandom.com/wiki/List_of_episodes"

driver = webdriver.Chrome()
driver.get(URL)

# data = driver.find_element(By.CSS_SELECTOR, '.table-wide-inner') #cant re-find this class in html source code....
# eps = data.find_elements(By.TAG_NAME, 'a') #only gives 46-56......
data = driver.find_elements(By.CLASS_NAME, "wds-tab__content wds-is-current")
# for i in data:
#     print(i.find_elements(By.TAG_NAME, 'a'))


