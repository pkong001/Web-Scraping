# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 15:06:53 2022

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
install
pip install pandas
#location_ti = 'C:/Users/pkong/JUPYTER/Web Scarping Spyder/Driver/msedgedriver.exe'
#location_laptop = 'G:/Other computers/PIC MIKI TI/JUPYTER/Web Scarping Spyder/Driver/msedgedriver.exe'
s = Service('C:/Users/pkong/JUPYTER/Web Scarping Spyder/Driver/msedgedriver.exe')
driver = webdriver.Edge(service = s)
driver.get('https://twitter.com/login')

element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')))
box = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
box.send_keys('pkongdan01@gmail.com')
box.send_keys(Keys.ENTER)

element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))#wait at 'driver' until it find specific element
box = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
for i in range(20):
    box.send_keys(Keys.BACKSPACE)
box.send_keys('tinb9977')
box.send_keys(Keys.ENTER)

element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')))
box = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
box.send_keys('0898168360')
box.send_keys(Keys.ENTER)

element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]')))#wait at 'driver' until it find specific element
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]').click()


element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')))#wait at 'driver' until it find specific element
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input').click()
box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
box.send_keys('dwayne johnson')
box.send_keys(Keys.ENTER)

time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[3]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a').click()

time.sleep(3)
soup = BeautifulSoup(driver.page_source, 'lxml')
postings = soup.find_all('div', class_ = 'css-901oao r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')
len(postings)
tweets = []
scroll_length = 3000
while True:
    for i in postings:

        x = i.find_all('span', class_ = 'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0')      
        t=''
        for j in x:
            y = j.text.strip()
            t +=' '+y
        tweets.append(t)
        driver.execute_script('window.scrollTo(0,'+str(scroll_length)+')')
        scroll_length += 3000
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        postings = soup.find_all('div', class_ = 'css-901oao r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')
        tweets2 = list(set(tweets))
        if (len(tweets2)) > 30:
            break
            

postings[0].text.replace('\n', ' ')
new_string = string.replace("r", "e" )
a = postings[0].find_all('span', class_ = 'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0')
a
t = ''
for i in a:
    y = i.text.strip()
    print(y)
    t +=' '+ y
t
