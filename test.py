from selenium import webdriver
from selenium.webdriver.common.by import By
import pprint as pp


URL = "https://adventuretime.fandom.com/wiki/Category:Transcripts"
driver = webdriver.Chrome()
driver.get(URL)

episode = driver.find_elements(By.CLASS_NAME, "category-page__members-wrapper ul li")


episode_list = [{'ep': i.text.split('/')[0],
      'url': i.find_element(By.CLASS_NAME, 'category-page__member-link').get_attribute('href')}
     for i in episode[1:]]


#WORKS: ----
# for ep_dict in episode_list:
#     driver.get(ep_dict['url']) #get link to specific episode
#     ep_text = driver.find_elements(By.CSS_SELECTOR, "dl")
#     print('--------TEXT BREAK--------')
#     for line in ep_text[1:]:
#         print(line.text)


for ep_dict in episode_list:
    driver.get(ep_dict['url'])
    ep_text = driver.find_elements(By.CSS_SELECTOR, "dl")
    xx = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div/aside/nav')
    print(str(xx.text))





