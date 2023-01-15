# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 18:20:03 2022

@author: pkong
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.airbnb.ca/s/honolulu/homes?tab_id=home_tab&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&refinement_paths%5B%5D=%2Fhomes&date_picker_type=calendar&checkin=2022-11-02&checkout=2022-11-03&adults=1&search_type=unknown'
page=requests.get(url)
page
soup = BeautifulSoup(page.text, 'lxml')
soup


df = pd.DataFrame({'link':[''],'Title':[''], 'Detials':[''], 'Price per Night':[''], 'Rating':['']})
current_page = 1
current_post = 1
print('current page {0}'.format(current_page))
while True:
    postings = soup.find_all('div', class_ = 'c4mnd7m dir dir-ltr')
    for post in postings:
        print('current post {0}'.format(current_post))
        link = post.find('a', class_ = 'ln2bl2p dir dir-ltr').get('href')
        link_full = 'https://www.airbnb.ca' + link
        
        title = post.find('span', class_ = 't6mzqp7 dir dir-ltr').text
        
        temp_get = requests.get(link_full)
        temp_soup = BeautifulSoup(temp_get.text, 'lxml')
        description = temp_soup.find('div', {'class':'d1isfkwk dir dir-ltr'}).text
        
        temp_detail = temp_soup.find_all('ol', class_ = 'lgx66tx dir dir-ltr')[0]
        detail =''
        for i in temp_detail:
            j = i.text
            detail += j
        
        price_per_night = post.find('span', class_ = '_tyxjp1').text
        
        rating = post.find('span', class_ = 'r1dxllyb dir dir-ltr').text[:4]
        
        df = df.append({'link':link_full,'Title':title, 'Detials':detail, 'Price per Night':price_per_night, 'Rating':rating}, ignore_index = True)
        current_post += 1
    next_page = soup.find('a', {'aria-label':'Next'}).get('href')
    next_full = 'https://www.airbnb.ca' + next_page
    # Some site has a full url and some site has a partial url  
    page = requests.get(next_full)
    soup = BeautifulSoup(page.text, 'lxml')
    current_page += 1
    print('current page {0}'.format(current_page))
  
    #it will run until reach page 15th then it will be error
    
df = df[1:]

df.to_csv('C:/Users/pkong/JUPYTER/Web Scarping Spyder/airbib_honolulu.csv')


#NOTE BELOW
b = soup.find('div', class_ = 'a8jt5op dir dir-ltr')
a = soup.find_all('div', class_ = 'c4mnd7m dir dir-ltr')
a[0].find('span', class_ = 't5eq1io r4a59j5 dir dir-ltr').get('aria-label')


g1qv1ctd cb4nyux dir dir-ltr #information
'a', ln2bl2p dir dir-ltr #url
c4mnd7m dir dir-ltr #main
t1jojoys dir dir-ltr # hotal name
_tyxjp1 # price per night
r1dxllyb dir dir-ltr # span rating



while True:
   

temp_get = requests.get(link_full)
temp_soup = BeautifulSoup(temp_get.text, 'lxml')
temp_soup.find('div', {'class':'d1isfkwk dir dir-ltr'}).text

ss = temp_soup.find_all('ol', class_ = 'lgx66tx dir dir-ltr')[0]

detail =""
for i in ss:
    j = i.text
    detail = detail + j
    
[i.text for i in ss]
