from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://adventuretime.fandom.com/wiki/Category:Main_Characters"
driver = webdriver.Chrome()

episodes = []

driver.get(URL)
main_chars = driver.find_elements(By.CLASS_NAME, "category-page__member-link")
main_characters = [{'name': i.text, 'url': i.get_attribute('href')} for i in main_chars]
del main_characters[6]





for i in main_characters:
    if i['name'] == 'Finn' or i['name'] == 'Jake':
        driver.get(i['url'])
        episode = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div/ul[1]')
        x = episode.find_elements(By.CSS_SELECTOR, 'ul li a')
        for e in x:
            print(e.text)
            # episodes.append({'episode_name': e.text, 'character_name': i['name']})
    else:
        pass
    # else:
    #     driver.get(i['url'])
    #     episode = driver.find_elements(By.CSS_SELECTOR, 'table[cellpadding="0"] ul li a')
    #
    #     for e in episode:
    #         episodes.append({'episode_name': e.text, 'character_name': i['name']})
    #
