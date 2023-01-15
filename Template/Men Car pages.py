# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 07:59:15 2022

@author: pkong
"""

#1 GET THE LINK OF EACH POSTING
#2. GET THE NAME OF EACH CAR
#3. GET TEH PRICE OF EACH CAR
#4. GET THE COLOR OF EACH CAR
#5. PUT ALL THAT DATA INTO A DATAFRAME
#6. DO THIS FOR THE FIRST 10 - 15 PAGES ON THE SITE


import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.carpages.ca/used-cars/search/?num_results=50&fueltype_id%5B0%5D=3&fueltype_id%5B1%5D=7&p=1'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
soup
base_link = 'https://www.carpages.ca'

count = 1
current_post = 1
current_page = 1

df = pd.DataFrame({'Link':[''], 'Name':[''], 'Price':[''],'Color':['']})

while count<=10:
    posting = soup.find_all("div",  {"class": ["media soft push-none", "media soft push-none rule"]})
    print('current page = {0}'.format(current_page))
    for i in posting:
        print('current post = {0}'.format(current_post))
        link = i.find('a', class_ = 'media__img media__img--thumb').get('href')
        link_full = base_link + link
        name = i.find('h4').text.strip()
        price = i.find('strong', class_ = 'delta').text.strip()
        color = i.find_all('div', class_ = 'grey l-column l-column--small-6 l-column--medium-4')[1].text.strip()
        
        df = df.append({'Link':link_full, 'Name':name, 'Price':price,'Color':color}, ignore_index=True)
        current_post += 1

    next_page = soup.find('a', {'title':'Next Page'}).get('href')
    next_page_full = base_link + next_page
    
    page = requests.get(next_page_full)
    soup = BeautifulSoup(page.text, 'lxml')
    count += 1

df = df[1:]

df.to_csv('C:/Users/pkong/JUPYTER/Web Scarping Spyder/Car_page.csv')


#NOTE BELOW
soup.find_all(True, {'class':['media soft push-none', 'media soft push-none rule']})
#main
b = soup.find_all("div",  {"class": ["media soft push-none", "media soft push-none rule"]})
len(b)
#link
a = soup.find_all('a', class_ = 'media__img media__img--thumb')[0].get('href')
len(a)
#name
a = soup.find_all('h4')
len(a)
#price
a = soup.find_all('strong', class_ = 'delta')
len(a)
#color
a = posting[0].find_all('div', class_ = 'grey l-column l-column--small-6 l-column--medium-4')
a[1].text.strip()
count=0
while count<=10:
    print(x)
    x +=1  
    count += 1
