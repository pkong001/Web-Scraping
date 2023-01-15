# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 12:28:50 2022

@author: pkong
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # method 1
import time #method 2

# find where chromedriver app is
s = Service('G:/Other computers/PIC MIKI TI/JUPYTER/Web Scarping Spyder/Driver/msedgedriver.exe')
# link to our Chrome() class
driver = webdriver.Edge(service = s)

driver.get('https://www.google.com/')
box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('top 100 movies of all time')
time.sleep(2)
button = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]')
button.click()
driver.find_element(By.XPATH, '//*[@id="rso"]/div[2]/div/div/div[1]/div/div/div[1]/div/a/h3').click()
element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div[3]/div[1]/div/div[4]/div[3]/div[100]/div[2]/p[4]/span[2]')))#wait at 'driver' until it find specific element
driver.execute_script('window.scrollTo(0,22250)')
driver.save_screenshot('G:/Other computers/PIC MIKI TI/JUPYTER/Web Scarping Spyder/Jaws_screen.png')
jaw_pic = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[3]/div[1]/div/div[4]/div[3]/div[50]/div[1]/a/img')
jaw_pic.screenshot('G:\Other computers\PIC MIKI TI\JUPYTER\Web Scarping Spyder\Jaws_pic.png')  

from bs4 import BeautifulSoup
import pandas as pd
soup = BeautifulSoup(driver.page_source, 'lxml')
post = soup.find_all('h3', class_ = 'lister-item-header')
df = pd.DataFrame({'Number':[''], 'Head':['']})
for i in post:
    head = i.find('a').text
    number = i.find('span').text
    df = df.append({'Number':number, 'Head':head}, ignore_index=True)
df
#main

