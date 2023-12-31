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
        self.all_ep = []

    def all_episodes(self):
        """Get all show episodes (used for comparison)"""

        self.driver.get("https://adventuretime.fandom.com/wiki/List_of_episodes#Original_Order")
        episode_page = self.driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div/div[1]/div[3]')
        episodes = episode_page.find_elements(By.CSS_SELECTOR, 'tbody tr td a')
        self.all_ep = [i.text for i in episodes[10:]]

        for i in self.all_ep:
            if i == '':
                self.all_ep.remove(i)


    def get_characters(self):
        """Retreive main character name & wiki link"""

        self.driver.get(URL)
        main_chars = self.driver.find_elements(By.CLASS_NAME, "category-page__member-link")
        self.main_characters = [{'name': i.text, 'url': i.get_attribute('href')} for i in main_chars]
        del self.main_characters[6]


    def get_episodes(self):
        """For each character get each episodes which they appear in"""

        for i in self.main_characters:
            if i['name'] == 'Finn' or i['name'] == 'Jake':
                self.driver.get(i['url'])
                ep_list = self.driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div/ul[1]')
                not_in_episode = [i.text for i in ep_list.find_elements(By.CSS_SELECTOR, 'ul li a')]

                episode = self.compare_eps(not_in_episode)

                for e in episode:
                    self.episodes.append({'episode_name': e, 'character_name': i['name']})

            elif i['name'] == 'Lady Rainicorn' or i['name'] == 'Lumpy Space Princess':
                self.driver.get(i['url'])
                ep_list = self.driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div')

                for e in episode:
                    self.episodes.append({'episode_name': e, 'character_name': i['name']})

            else:
                self.driver.get(i['url'])
                episode = self.driver.find_elements(By.CSS_SELECTOR, 'table[cellpadding="0"] ul li a')

                for e in episode:
                    self.episodes.append({'episode_name': e.text, 'character_name': i['name']})


    def dataframe(self):
        """Create dataframe from episode/character data and save to csv"""

        character_df = pd.DataFrame(self.episodes)
        character_df.to_csv('character_list.csv')


    def compare_eps(self, not_in):
        """Removes episode if already in all episodes
        & creates a new list of episodes to work with"""

        new_ep_list = [i for i in self.all_ep]
        for i in not_in:
            if i in new_ep_list:
                new_ep_list.remove(i)
                return new_ep_list


    def scrape(self):
        self.all_episodes()
        self.get_characters()
        self.get_episodes()
        self.dataframe()
