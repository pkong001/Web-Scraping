# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 13:16:04 2022

@author: pkong
"""

#1. remember to import the HTML into python
#2. price of the stock
#3. Closing price of the stock
#4. 52 week range( lower, upper)
#5. Analyst rating

import requests
import lxml
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.marketwatch.com/investing/stock/aapl'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
soup2 = BeautifulSoup(page.content, 'lxml')
print(soup == soup2)


#MY SOLUTION----------------------------------------------------------
# current price
soup.find('bg-quote', class_ = 'value').text
# closed price
soup.find('td', class_ ='table__cell u-semi').text
#Lower range
soup.find_all('div', class_ = 'range__header')[2].find_all('span')[0].text
#upper range
soup.find_all('div', class_ = 'range__header')[2].find_all('span')[2].text
#Rating
soup.find('li', class_ ='analyst__option active').text


#CHRISTOPHER SOLUTION-----------------------------------------

import requests
from bs4 import BeautifulSoup

url = 'https://www.marketwatch.com/investing/stock/aapl'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

#2. get the current price of the stock
price = soup.find('bg-quote', class_ = 'value').text
price

#3. get closing price of stock 
closing_price = soup.find('td', class_ = 'table__cell u-semi').text
closing_price

#4. 52 week range (lower, upper)
nested = soup.find('mw-rangebar', class_ = 'element element--range range--yearly')
nested

lower = nested.find_all('span', class_ = 'primary')[0].text
lower

upper = nested.find_all('span', class_ = 'primary')[1].text
upper

#5. analyst rating
rating = soup.find('li', class_ = 'analyst__option active').text
rating
