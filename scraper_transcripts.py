from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://adventuretime.fandom.com/wiki/Category:Transcripts"

class TextScraper:
    """Access episode transcripts & convert each to a text file"""

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.episode = []

    def get_episode(self):
        """Access episode transcript page & read/save text"""

        self.driver.get(URL)
        episode = self.driver.find_elements(By.CLASS_NAME, "category-page__members-wrapper")


    def create_episode_file(self):
        """Take parsed text & save to a text file in project"""

        pass