import pandas as pd
import pprint as pp
import time
from scraper import Scrapper

find = Scrapper()
find.get_characters()
find.get_episodes()

episode_df = pd.DataFrame(find.episodes)
print(episode_df)

