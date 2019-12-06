from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time 

driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/chromedriver")

driver.get("https://www.vvlimmen.nl/592/5247/competitie/programma/?sid=3")
time.sleep(10)
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
games = soup.findAll("td")

datum = []
tijd = []
thuis = []
uit = []
count = 0

for game in games:  
    if not game.text:
        count = 0
    elif count == 0:
        datum.append(game.text)
        count += 1
    elif count == 1:
        tijd.append(game.text)
        count += 1
    elif count == 2:
        thuis.append(game.text)
        count += 1
    else:
        uit.append(game.text)
        count += 1
    
df = pd.DataFrame({"datum": datum, "tijd": tijd, "thuis": thuis, "uit": uit})
df.to_csv('games.csv', index=False, encoding='utf-8')   