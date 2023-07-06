from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://adventuretime.fandom.com/wiki/Category:Transcripts"

class TextScraper:
    """Access episode transcripts & convert each episode to a text file"""

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.episode = []


    def get_episode(self):
        """Get episode name & URL: store in nested dict"""

        self.driver.get(URL)
        episode = self.driver.find_elements(By.CLASS_NAME, "category-page__members-wrapper ul li")

        self.episode = [{'episode': i.text.split('/')[0],
                         'url': i.find_element(By.CLASS_NAME, 'category-page__member-link').get_attribute('href')}
                        for i in episode[1:]]


    def create_episode_file(self):
        """Scrape transript text & save to a text file in project"""
        for i in self.episode:
            self.driver.get(i['url'])
            text = self.driver.find_elements(By.CSS_SELECTOR, "dl")

            with open(f"data/{i['episode']}.txt", "w") as f:
                for line in text[1:]:
                    f.write(f"{line.text}\n")


    def launch(self):
        self.get_episode()
        self.create_episode_file()
