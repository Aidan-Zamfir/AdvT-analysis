from scraper_characters import CharacterScraper
from scraper_transcripts import TextScraper
from char_data import CharacterData

from pathlib import Path
import pandas as pd

import networkx as nx
import matplotlib.pyplot as plt




#STEP 1:

find_character = CharacterScraper()
find_character.scrape()


#Use when transcript text files (in data folder) DONT exist:
# collect_text = TextScraper()
# collect_text.launch()

#STEP 2:
# x = CharacterData()
# x.from_episode()
