# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 13:34:31 2022

@author: pkong
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # method 1
import time #method 2
from bs4 import BeautifulSoup
import pandas as pd



s = Service('G:/Other computers/PIC MIKI TI/JUPYTER/Web Scarping Spyder/Driver/msedgedriver.exe')
driver = webdriver.Edge(service = s)
driver.get('https://www.nike.com/ca/w/sale-3yaep/')


last_height = driver.execute_script('return document.body.scrollHeight')
last_height

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height
print('done')


soup = BeautifulSoup(driver.page_source, 'lxml')    
product_care=soup.find_all('div', class_ = 'product-card__body')    
product_care[0]
len(product_care)
links = []
for i in product_care:
    try:
        link = i.find('a', class_ = 'product-card__link-overlay').get('href')
        links.append(link)
    except:
        pass # try and except is for case that someone forget to put data in it will result in erorr.
links





while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')#scroll until reach the bottom