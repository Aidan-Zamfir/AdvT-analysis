from selenium import webdriver
from selenium.webdriver.common.by import By
import re



URL = "https://adventuretime.fandom.com/wiki/List_of_episodes#Original_Order"
driver = webdriver.Chrome()

driver.get(URL)

epi = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div/div[1]/div[3]')
x = epi.find_elements(By.CSS_SELECTOR, 'tbody tr td a')

episodes = [i.text for i in x[10:]]


for i in episodes:
    if i == '':
        episodes.remove(i)



print(episodes)
