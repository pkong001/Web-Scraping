# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 21:07:29 2023

@author: pkong
"""

import requests 
from bs4 import BeautifulSoup 
import pandas as pd
import re

def findmax(soup_p):
    max_page = soup_p.find_all("a", class_ = "page-numbers")
    max_p = []
    for i in max_page:
        num_page = i.text.strip()
        try:
            num_page = int(num_page)
        except:
            num_page = 0
        max_p.append(num_page)
    max_p = max(max_p)
    print(max_p)
    return max_p

def scrap(url,gerne):
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    manga_divs = soup.find_all("div", class_="bs")

    # empty list to store data
    df = pd.DataFrame({'title':[],'score':[],'chapter':[],'link':[]})
    i=2 #หน้าเริ่มต้น
    # loop to extract the data
    max_page = findmax(soup)
    while i < max_page:
        for manga in manga_divs:
            title = manga.find("div", attrs={"class": "tt"}).text.strip()
            score = manga.find("div", attrs={"class": "numscore"}).text.strip()
            chapter = manga.find("div", class_="epxs").text.strip()
            link = manga.find('a').get('href')
            try:
                chapter = int(re.findall(r'\b\d+\b',chapter)[0])
            except:
                chapter = 0
            df = df.append({'title':title,'score':score,'chapter':chapter,'link':link}, ignore_index = True)
            next_page = soup.find('a', {'class':'next page-numbers'}).get('href')
    
        html_content = requests.get(next_page).text
        soup = BeautifulSoup(html_content, "lxml")
        manga_divs = soup.find_all("div", class_="bs")
        i+=1
        print('page',i)
    # create the dataframe
        df.to_csv('D:/toon_'+str(gerne)+'.csv')
        
adventure_url = "https://manga168.com/genres/adventure/"
romance_url = "https://manga168.com/genres/romance/"
action_url = "https://manga168.com/genres/action/"
fantasy_url = "https://manga168.com/genres/fantasy/"

scrap(adventure_url,'adventure')
scrap(romance_url,'romance')
scrap(action_url,'action')
scrap(fantasy_url,'fantasy')
    




        

