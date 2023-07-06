import pandas as pd
import pprint as pp
import time
from scraper import Scrapper

find = Scrapper()
find.get_characters()

pp.pprint(find.main_characters)

