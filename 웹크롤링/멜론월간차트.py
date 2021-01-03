import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriverpip
from selenium.webdriver.common.keys import Keys

chrome_driver = 'C:/Users/GH/AI_WORK/web/chromedriver'
driver = webdriver.Chrome(chrome_driver)

url = 'https://www.melon.com/chart/month/index.htm'
driver.get(url)
source = driver.page_source

melonchart = source
soup_melonchart = BeautifulSoup(melonchart)

song_title = soup_melonchart.select('div.wrap_song_info div.ellipsis.rank01')
song_artist = soup_melonchart.select('div.wrap_song_info div.ellipsis.rank02 span')

for i in range(len(song_title)):
    song_title[i] = song_title[i].text.strip()

for i in range(len(song_artist)):
    song_artist[i] = song_artist[i].text.strip()

for rank, (i, j) in enumerate(zip(song_title, song_artist)):
    print(rank + 1, i, j)