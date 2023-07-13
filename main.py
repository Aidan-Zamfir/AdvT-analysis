from scraper_characters import CharacterScraper
from scraper_transcripts import TextScraper
from char_data import CharacterData
import os


def scrape_char():
    """Scrape main character data"""

    find_character = CharacterScraper()
    find_character.scrape()

def transcripts():
    """Scrape epsiode transcripts & save.
    Use when 'data' folder is empty"""

    collect_text = TextScraper()
    collect_text.launch()

def relationships():
    """Access transcripts and use nlp to parse through
    episodes. Collect data and create network graph of
     character relationships in each epsiode"""

    x = CharacterData()
    x.run()

def main():
    scrape_char()
    if os.path.isfile("character_list.csv"):
        relationships()
    else:
        transcripts()
        relationships()


if __name__ == '__main__':
    main()