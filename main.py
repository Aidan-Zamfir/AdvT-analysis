import pandas as pd
import pprint as pp
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://adventuretime.fandom.com/wiki/Category:Main_Characters"

driver = webdriver.Chrome()
driver.get(URL)

main_characters = driver.find_elements(By.CLASS_NAME, "category-page__member-link")

main_chars = []
for i in main_characters:
    name = i.text
    link = i.get_attribute('href')
    main_chars.append({'name': name, 'url': link})

pp.pprint(main_chars)
print(" ")

