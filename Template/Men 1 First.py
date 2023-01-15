# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
import lxml
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
soup2 = BeautifulSoup(page.content, 'lxml')
print(soup == soup2)

tag = soup.header.p
tag.string
soup.header.p.string


tag2 = soup.header.a
tag2.attrs
tag2['data-toggle']
tag2['attribute_new'] = 'this is a new attribute'
tag2.attrs



soup.find('header').attrs
soup.find('div', {'class':'container test-site'})

# This can use with many attibutes, THIS CALLED DICTIONARY METHOD
soup.find('h4', {'class':'pull-right price'})

# This only work with class attibute.
soup.find('h4', class_ = 'pull-right price')

soup.find_all('h4', {'class':'pull-right price'})[:3]
a1 = soup.find_all('h4', {'class':'pull-right price'})
[i.text for i in a1]

a2 = soup.find_all('a', class_ = 'title')
[i.text for i in a2]

# Returning 'h4', 'p', and 'a' tags
soup.find_all(['h4','p','a'])

# Returning all the line of code that have 'id' as its attributes
soup.find_all(id = True)

# Find all the string and equal to 'Iphone'
soup.find_all(string = 'Iphone')

# Import re to complie find all string
# Find if work containing some certain alphabets
import re
soup.find_all(string = re.compile('Iph'))
soup.find_all(class_ = re.compile('pull'))
soup.find_all('p', class_ = re.compile('pull'))
soup.find_all('p', class_ = re.compile('pull'), limit = 3)
soup.find_all(string = ['Iphone', 'Nokia 123'])




product_name = soup.find_all('a', {'class':'title'})
product_name_list =[]
for i in product_name:
    name = i.text
    product_name_list.append(name)
# OR
product_name_list = [i.text for i in product_name]

price = soup.find_all('h4', {'class':'pull-right price'})
price_list = [i.text for i in price]

reviews = soup.find_all('p', class_ = re.compile('pull'))
review_list = [i.text for i in reviews]

description = soup.find_all('p', class_ = 'description')
description_list = [i.text for i in description]



import pandas as pd
df = pd.DataFrame()
df['product_name']= product_name_list
df['description'] = description_list
df['price'] = price_list
df['reviews'] = review_list
df
# OR
df = pd.DataFrame({'Product Name':product_name_list, 
                      'Description':description_list,
                      'Price':price_list,
                      'Reviews':review_list})
df



# Find in nesting
boxes = soup.find_all('div', class_ = 'col-sm-4 col-lg-4 col-md-4')[6]
boxes
boxes.find('a').text
boxes.find('p', class_ = 'description').text
box2 = soup.find_all('ul', class_ = 'nav', id = 'side-menu')[0]
box2.find_all('li')[1]



    