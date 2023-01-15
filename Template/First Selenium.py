# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 15:48:09 2022

@author: pkong
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# find where chromedriver app is
s = Service('G:/Other computers/PIC MIKI TI/JUPYTER/Web Scarping Spyder/Driver/msedgedriver.exe')
# link to our Chrome() class
driver = webdriver.Edge(service = s)
# get the website url
driver.get('https://goat.com/sneakers/')
driver.find_element(By.CLASS_NAME, 'bg-wrap')


#Mostly we use Xpath to click some certain botton
driver.find_element(By.XPATH,'/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[]/a/div[1]/div[2]/div/div/span').text
driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[1]/div/div[2]/aside[1]/div/div[1]/a[2]').click()

#However, we can also use xpath to so this, but don't do it then why teach us .
for i in range(1,30):
    price = driver.find_element(By.XPATH,'/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[' +str(i)+']/a/div[1]/div[2]/div/div/span').text
    print(price)
    
#Sending Keys
from selenium.webdriver.common.keys import Keys
driver.get('https://www.google.com/')
box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('Alan')
box.send_keys(Keys.ENTER) #

#Sending Keys Then click on Search
driver.get('https://www.google.com/')
box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('Jack Sparrrow')
time.sleep(2)
button = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]')
button.click()
driver.find_element(By.XPATH, '/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[2]/a').click()

#Taking a screen Shot
driver.save_screenshot('G:\Other computers\PIC MIKI TI\JUPYTER\Web Scarping Spyder\screenshot.png')

#Takinga screen  shot on specific element
driver.find_element(By.XPATH, '/html/body/div[7]/div/div[11]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/a/h3').screenshot('G:\Other computers\PIC MIKI TI\JUPYTER\Web Scarping Spyder\screenshot2.png')                       
driver.find_element(By.XPATH,'/html/body/div[7]/div/div[11]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div/img').screenshot('G:\Other computers\PIC MIKI TI\JUPYTER\Web Scarping Spyder\screenshot3.png')                  
       
#Scrolling
driver.execute_script('return document.body.scrollHeight') #get height
driver.execute_script('window.scrollTo(0,3511)') #scroll to certain y coordinate
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)') #scroll to the bottom


while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')#scroll until reach the bottom
    
#Wait time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # method 1
import time #method 2
driver.get('https://www.google.com/')
box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('Jack Sparrrow')
time.sleep(2)
button = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]')
button.click()
element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'hdtb-tls')))#wait at 'driver' until it find specific element
driver.find_element(By.XPATH, '/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[2]/a').click()

                
test=[]
for i in range(1,10):
    t = i
    test.append(t)
    
for i in test:
    print('what'+str(i)+'is')