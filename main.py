import spacy

from scraper_characters import CharacterScrapper
import pandas as pd
import pprint as pp
from spacy import displacy
import networkx as nx
import matplotlib.pyplot as plt

NER = spacy.load(("en_core_web_sm"))

find = CharacterScrapper()
find.get_characters()
find.get_episodes()

episode_df = pd.DataFrame(find.episodes)
print(episode_df)

