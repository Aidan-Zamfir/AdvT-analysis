from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


URL = "https://adventuretime.fandom.com/wiki/Category:Main_Characters"

class CharacterScraper:
    """Access character data from fandomwiki"""

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.main_characters = []
        self.episodes = []

    def get_characters(self):
        """Retreive main character name & wiki link"""

        self.driver.get(URL)
        main_chars = self.driver.find_elements(By.CLASS_NAME, "category-page__member-link")
        self.main_characters = [{'name': i.text, 'url': i.get_attribute('href')} for i in main_chars]


    def get_episodes(self):
        """For each character get each episode which they appear in"""

        for i in self.main_characters:
            self.driver.get(i['url'])
            episode = self.driver.find_elements(By.CSS_SELECTOR, 'table[cellpadding="0"] ul li a')

            for e in episode:
                self.episodes.append({'episode_name': e.text, 'character_name': i['name']})
            # self.episodes = [{'episode_name': e.text, 'character_name': i['name']} for e in episode]


    def dataframe(self):
        """Create dataframe from episode/character data and save to csv"""
        character_df = pd.DataFrame(self.episodes)
        character_df.to_csv('character_list.csv')


    def scrape(self):
        self.get_characters()
        self.get_episodes()
        self.dataframe()
