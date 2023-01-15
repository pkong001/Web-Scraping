# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 07:39:56 2022

@author: pkong
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # method 1 #this is javaexecutor
import time #method 2
from bs4 import BeautifulSoup
import pandas as pd



s = Service('C:/Users/pkong/JUPYTER/Web Scarping Spyder/Driver/msedgedriver.exe')
driver = webdriver.Edge(service = s)
#24
#driver.get('https://www.linkedin.com/jobs/search?keywords=Machine%20Learning&location=Thailand&locationId=&geoId=105146118&f_TPR=r86400&position=1&pageNum=0')
#week
driver.get('https://www.linkedin.com/jobs/search?keywords=Machine%20Learning&location=Thailand&locationId=&geoId=105146118&f_TPR=r604800&position=1&pageNum=0')

#for 2560x1440
height = 1850
width = 1385
driver.set_window_size(height,width)



#scrool to the buttom, and resume to the top
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height
driver.execute_script('window.scrollTo(0,1)')

soup = BeautifulSoup(driver.page_source, 'lxml')
clicking = soup.find_all('div', class_ = 'base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
clicking_count = len(clicking)
tabs = soup.find_all('a', class_ = 'base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]')

    
df = pd.DataFrame({'link':[''],
                   'title':[''],
                   'company':[''],
                   'area':[''],
                   'post_time':[''],
                   'applicants':[''],
                   'level':[''],
                   'employment_type':[''],
                   'function':[''],
                   'industries':['']})
height_scroll = 1254
height_append = 1254
index = 51
page_run = 1
error = 1
while True:
    try:
        print('index = {0}'.format(index))
        driver.find_element(By.XPATH, '/html/body/div[1]/div/main/section[2]/ul/li['+str(index)+']').click()
        time.sleep(4)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/section/div[2]/div/section[1]/div/div/section/button[1]').click()
        time.sleep(2)
        index += 1
    except:
        print('scroll')
        driver.execute_script('window.scrollTo(0,'+str(height_scroll)+')')
        height_scroll += height_append
        error += 1
        if error == 10:
            break
    try:
        soup = BeautifulSoup(driver.page_source, 'lxml')
        postings = soup.find('div', 'details-pane__content details-pane__content--show')
        title = postings.find('h2', 'top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0 topcard__title').text.strip()
        print(title)
        company = postings.find('a', 'topcard__org-name-link topcard__flavor--black-link').text.strip()
        print(company)
        area = postings.find('span', 'topcard__flavor topcard__flavor--bullet').text.strip()
        print(area)
        try:
            post_time = postings.find('span', 'posted-time-ago__text topcard__flavor--metadata').text.strip()
            print(post_time)
        except:
            post_time = postings.find('span', 'posted-time-ago__text posted-time-ago__text--new topcard__flavor--metadata').text.strip()
            print(post_time)
        try:
            applicants = postings.find('span', 'num-applicants__caption topcard__flavor--metadata topcard__flavor--bullet').text.strip()
            print(applicants)
        except:
            applicants = postings.find('figcaption', 'num-applicants__caption').text.strip()
            print(applicants)
        level = postings.find_all('span', 'description__job-criteria-text description__job-criteria-text--criteria')[0].text.strip()
        print(level)
        employment_type = postings.find_all('span', 'description__job-criteria-text description__job-criteria-text--criteria')[1].text.strip()
        print(employment_type   ) 
        function = postings.find_all('span', 'description__job-criteria-text description__job-criteria-text--criteria')[2].text.strip()
        print(function)
        industries = postings.find_all('span', 'description__job-criteria-text description__job-criteria-text--criteria')[3].text.strip()
        print(industries)
        detail = postings.find('div', 'show-more-less-html__markup').text.strip()
        detail
        temp = tabs[index-2].get('href')
        temp
        df = df.append({'link':temp,
                        'title':title, 
                        'company':company, 
                        'area':area,
                        'post_time':post_time,
                        'applicants':applicants,
                        'level':level,
                        'employment_type':employment_type,
                        'function':function,
                        'industries':industries,
                        'detail':detail}, ignore_index=True)         
    except:
        pass
        
            
    
from datetime import date
today = date.today()
df.to_csv('C:/Users/pkong/JUPYTER/Web Scarping Spyder/linkedin export_'+str(today)+'.csv')

       
            
# soup = BeautifulSoup(driver.page_source, 'lxml')
# postings = soup.find('div', class_ ='show-more-less-html__markup')
# t = postings.text


# driver.execute_script("return document.body.scrollHeight")
# driver.execute_script('window.scrollTo(0,'+str(height_scroll)+')')

###THIS ONE IS GOODDDDDDD
# element = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/section[2]/ul/li[10]/div/a')
# driver.execute_script('arguments[0].scrollIntoView();', element)

    

# driver.find_element(By.XPATH, '/html/body/div[1]/div/main/section[2]/ul/li[10]/div/a').click()
#         time.sleep(1)
#         driver.find_element(By.XPATH, '/html/body/div[1]/div/section/div[2]/div/section[1]/div/div/section/button[1]').click()
        
# for i in range(5):
#     if i == 0:
#         print('pass', i)
#     else:
#         time.sleep(1)
#         print(i)
        


#location_ti = 'C:/Users/pkong/JUPYTER/Web Scarping Spyder/Driver/msedgedriver.exe'
#location_laptop = 'G:/Other computers/PIC MIKI TI/JUPYTER/Web Scarping Spyder/Driver/msedgedriver.exe'


# driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
# element = WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[1]/input')))
# box = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[1]/input')
# box.send_keys('pkongdan02@gmail.com')


# element = WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[2]/input')))
# box = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[2]/input')
# box.send_keys('tinb9977')
# box.send_keys(Keys.ENTER)

# time.sleep(3)
# try:
#     driver.find_element(By.XPATH, '/html/body/div[5]/header/div/nav/ul/li[3]/a').click()
# except Exception:
#     pass

# try:
#     driver.find_element(By.XPATH, '/html/body/div[4]/header/div/nav/ul/li[3]/a').click()
# except Exception:
#     pass

# element = WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.CLASS_NAME, 'jobs-search-box__text-input jobs-search-box__keyboard-text-input')))
# box = driver.find_element(By.CLASS_NAME, 'jobs-search-box__text-input jobs-search-box__keyboard-text-input')
# box.send_keys('Machine Learning')
# box.send_keys(Keys.ENTER)

# element = WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/header/div/div/div/div[2]/div[2]/div/div/input[1]')))
# box = driver.find_element(By.XPATH, '/html/body/div[5]/header/div/div/div/div[2]/div[2]/div/div/input[1]')
# box.click()
# for i in range(20):
#     box.send_keys(Keys.BACKSPACE)
# box.send_keys('Thailand')
# box.send_keys(Keys.ENTER)






