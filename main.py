from scraper_characters import CharacterScraper
from scraper_transcripts import TextScraper

import pandas as pd

import spacy
from spacy import displacy

import networkx as nx

import matplotlib.pyplot as plt

NER = spacy.load(("en_core_web_sm"))

find_character = CharacterScraper()
collect_text = TextScraper()

find_character.scrape()
collect_text.launch()





