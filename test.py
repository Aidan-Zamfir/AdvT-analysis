from selenium import webdriver
from selenium.webdriver.common.by import By
import pprint as pp

URL = "https://adventuretime.fandom.com/wiki/Category:Transcripts"
driver = webdriver.Chrome()
driver.get(URL)
episode = driver.find_elements(By.CLASS_NAME, "category-page__members-wrapper ul li")


x = []

for i in episode[1:]:
    link = i.find_element(By.CLASS_NAME, 'category-page__member-link')
    x.append({'ep': i.text.split('/')[0], 'url': link.get_attribute('href')})

pp.pprint(x)
