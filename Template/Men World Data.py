# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 13:48:54 2022

@author: pkong
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import lxml


url = 'https://www.worldometers.info/world-population/'
page = requests.get(url)
page

soup = BeautifulSoup(page.text, 'lxml')
soup

table = soup.find('table', class_="table table-striped table-bordered table-hover table-condensed table-list")
table

table.find_all('th')

headers = []
for i in table.find_all('th'):
    title = i.text
    headers.append(title)

df_population = pd.DataFrame(columns = headers)

table_info = table.find_all('tr')[1:]
table_info

#Real
for j in table_info:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    add_to_row_number = len(df_population) # count number of row in df
    df_population.loc[add_to_row_number] = row #add to specific row
    # the .loc transpose the list into the table
df_population
#---------------------------------------------------------------
#Testing
for j in table_info:
    row_data = j.find_all('td')
    break
row_data
#Testing apply .text to all within
for j in table_info:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    break
row
#OR
row = []
for j in table_info:
    row_data = j.find_all('td')
    for i in row_data:
        row.append(i.text)
    break
row
#-----------------------------------------------------------

df_population.to_csv('C:/Users/pkong/JUPYTER/table_population.csv')
