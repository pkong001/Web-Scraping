# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:57:31 2022

@author: pkong
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.nfl.com/standings/league/2019/REG'

page = requests.get(url)
page

soup = BeautifulSoup(page.text, 'lxml')
soup

table = soup.find('table', class_ ="d3-o-table d3-o-table--row-striping d3-o-table--detailed d3-o-standings--detailed d3-o-table--sortable {sortlist: [[4,1]], sortinitialorder: 'desc'}")
table

headers_find = table.find('thead').find_all('th')

headers = []
for i in headers_find:
    title =i.text.strip()
    headers.append(title)
    
    
df_football = pd.DataFrame(columns = headers)
for i in table.find('tbody'):
    row = i.find_all('td')[1:]
    row_add =[j.text.strip() for j in row]
    first_td = i.find_all('td')[0].find('div', class_ ='d3-o-club-fullname').text.strip()
    row_add.insert(0,first_td) # add the first_td back
    df_football.loc[len(df_football)]= row_add


#Christopher Solution
import requests
from bs4 import BeautifulSoup
import pandas as pd

#Imports the HTML into python
url = 'https://www.nfl.com/standings/league/2019/reg/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')


#Subsets the HTML to only get the HTML of our table needed
table = soup.find('table', {'summary':'Standings - Detailed View'})

#Gets all the column headers of our table
headers = []
for i in table.find_all('th'):
    title = i.text.strip()
    headers.append(title)

#Creates a dataframe using the column headers from our table
df = pd.DataFrame(columns = headers)

#gets all our data within the table and adds it to our dataframe
for row in table.find_all('tr')[1:]:
    #line below fixes the formatting issue we had with the team names
    first_td = row.find_all('td')[0].find('div', class_ = 'd3-o-club-fullname').text.strip()
    data = row.find_all('td')[1:]
    row_data = [td.text.strip() for td in data]
    row_data.insert(0,first_td)
    length = len(df)
    df.loc[length] = row_data
