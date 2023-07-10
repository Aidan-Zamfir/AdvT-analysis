from scraper_characters import CharacterScraper
from scraper_transcripts import TextScraper

import os
from pathlib import Path


import spacy
from spacy import displacy

import networkx as nx
import matplotlib.pyplot as plt


NER = spacy.load("en_core_web_sm")


# find_character = CharacterScraper()
# find_character.scrape()

#Use when transcript text files (in data folder) DONT exist:
# collect_text = TextScraper()
# collect_text.launch()



all_episodes = [i for i in os.scandir('data') if '.txt' in i.name]
ep1 = all_episodes[0]
ep1_text = open(ep1).read()
doc = NER(ep1_text)

displacy.serve(doc, style='ent', port=5001)