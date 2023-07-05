import pandas as pd
import time
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

URL = "https://adventuretime.fandom.com/wiki/Category:Characte"

driver = webdriver.Chrome()
driver.get(URL)