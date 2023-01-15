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
import os

# directory = os.getcwd()
# directory = directory.replace('\\','/')
# driver_location = '/driver/msedgedriver.exe'
# directory_full = directory + driver_location
# directory2 = "G:/Other computers/PIC MIKI TI/JUPYTER/Web Scarping Spyder/msedgedriver.exe"
# s = Service(directory2)

#DEFINE SCROLL_DOWN FUNCTION TO CALL LATER
def scroll_down():
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == last_height:
            break
        last_height = new_height
    driver.execute_script('window.scrollTo(0,1)')

#GET THE SERVICE AND OPENING MICROSOFT EDGE
#s = Service('C:/Users/pkong/JUPYTER/Web Scarping Spyder/Driver/msedgedriver.exe')
s = Service('G:/Other computers/PIC MIKI TI/JUPYTER/Web Scarping Spyder/Driver/msedgedriver.exe')

driver = webdriver.Edge(service = s)

#OPEN A CERTAIN URL
#24
#driver.get('https://www.linkedin.com/jobs/search?keywords=Machine%20Learning&location=Thailand&locationId=&geoId=105146118&f_TPR=r86400&position=1&pageNum=0')
#week
driver.get('https://th.jobsdb.com/th/search-jobs/machine-learning/1?Locations=2%2C67&SalaryF=30000&SalaryT=70000&SalaryType=1&createdAt=30d')
# driver.get('https://th.jobsdb.com/th/search-jobs/machine-learning/1?Locations=2%2C67&SalaryF=30000&SalaryT=70000&SalaryType=1&createdAt=1d')

# SETTING UP THE PARAMETER FOR THE BROWSER
#for 2560x1440
height = 1850
width = 1385
driver.set_window_size(height,width)
time.sleep(1)
scroll_down()
time.sleep(1)
#DEFINE THE DATAFRAME FOR ADDING DATAS
df = pd.DataFrame({'link':[''],
                   'title':[''],
                   'premise':[''],
                   'post_time':[''],
                   'highlight':[''],
                   'information':[''],
                   'detail':['']})
df = df[1:]



#things to enter
# count_post_all as a page per url

#DEFINE VARIABLES
base_link = 'th.jobsdb.com' # define base link for changing pages
soup = BeautifulSoup(driver.page_source, 'lxml')
postings = soup.find_all('div', 'sx2jih0 zcydq876 zcydq866 zcydq896 zcydq886 zcydq8n zcydq856 zcydq8f6 zcydq8eu') # use for extraction of data from job posts
index = 1 #default is 1 for index
page_run = 1 #using for changing page in if argument
count_scroll = 0 #for counting the scroll in each iteration
count_post_all = 30 #number of job posts per page in a single URL
while len(df) < count_post_all:
    print('index ={0}'.format(index))
    #CLICKING THE JOB POSTS
    try:
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[2]/div/div['+str(index)+']/div/div/article/div/div/div[1]/div[1]/div[1]').click()
        time.sleep(1)   
    #SCROLL IF THE JOB POSTS CAN NOT BE CLICK         
    except:
        print('can not click > try to scroll = {0}'.format(count_scroll))
        driver.execute_script('window.scrollBy(0,400)')
        count_scroll += 1
        continue
    try:
        detail = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/span').text.strip()
    except:
        try:
            detail = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/span/div').text.strip()
        except:
            detail = 'N/A'
        
    print(detail)
    soup3 = BeautifulSoup(driver.page_source, 'lxml')
    postings3 = soup3.find_all('div', class_ = 'sx2jih0 zcydq856 zcydq8fe _17fduda27')
    try:
        information = postings3[0].text.strip() + ' &&& ' + postings3[1].text.strip()
    except:
        try:
            information = postings3[0].text.strip()
        except:
            information = 'N/A'
    print(information)
    title = postings[index-1].find('div', class_ = 'sx2jih0 l3gun70 l3gun74 l3gun72').text.strip()
    print(title)
    link = postings[index-1].find('a', {'data-automation':'jobCardLocationLink'}).get('href')
    link = base_link + link
    print(link)
    area = postings[index-1].find_all('a', class_ = 'sx2jih0 sx2jihf QytTO')
    premise =''
    for i in area:
        x = i.text
        premise +=' & '+ x
    print(premise)
    highlight_all = postings[index-1].find_all('div', class_ = 'sx2jih0 zcydq856')
    highlight = ''
    for i in highlight_all:
        x = i.text
        highlight +=' & '+ x
    print(highlight)
    post_time = postings[index-1].find('span', 'sx2jih0 zcydq84u _18qlyvc0 _18qlyvc1y _18qlyvc1 _18qlyvc7').text
    print(post_time)
    
    df = df.append({'link':link,
                       'title':title,
                       'premise':premise,
                       'post_time':post_time,
                       'highlight':highlight,
                       'information':information,
                       'detail':detail}, ignore_index = True)
    index += 1
    
    #CHAGING PAGE IF THE INDEX REACH A CERTAIN NUMBER
    if index == 31:
        index = 1
        page_run += 1
        print("changing_page to page = {0}".format(page_run))
        get_link_one = 'https://th.jobsdb.com/th/search-jobs/machine-learning/'
        number_page = page_run
        # get_link_two = '?Locations=2%2C67&SalaryF=30000&SalaryT=70000&SalaryType=1&createdAt=30d'
        get_link_two = '?Locations=2%2C67&SalaryF=30000&SalaryT=70000&SalaryType=1&createdAt=1d'
        get_link_full = get_link_one + str(number_page) + get_link_two
        driver.get(get_link_full)
        time.sleep(6)
        soup_count = BeautifulSoup(driver.page_source, 'lxml')
        count_post = soup_count.find_all('div', 'sx2jih0 zcydq876 zcydq866 zcydq896 zcydq886 zcydq8n zcydq856 zcydq8f6 zcydq8eu')
        count_post_all += len(count_post)
        current_page1 = driver.current_url
        scroll_down()
        time.sleep(1)
        


#EXPORTING FILE
from datetime import date
today = date.today()
#df.to_csv('C:/Users/pkong/JUPYTER/Web Scarping Spyder/jobsdb export_'+str(today)+'.csv')

#df.to_csv(directory +'/Export/'+ str(today) + 'jobsdb_export_2.csv')
# df.to_csv("G:/Other computers/PIC MIKI TI/JUPYTER/Web Scarping Spyder/Export/jobsdb_"+str(today)+".csv")
df.to_csv('C:/Users/pkong/JUPYTER/Web Scarping Spyder/Export/jobsdb_'+str(today)+'.csv')



#SENDING EMAIL TO RECIPIENTS    
from email.message import EmailMessage
import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

recipients = ['pkongdan01@gmail.com','pkongdan02@gmail.com']

for i in recipients:
    email_sender = 'pkong.py@gmail.com'
    email_password = 'vujuandcrbzkosuj'
    email_receiver = i
    print(i)
    subject = 'Export Jobs research Raw data'
    body = """
    This is the export file for today dude!!!
    
    """
    
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = email_sender
    msg['To'] = email_receiver
    
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open('G:/Other computers/PIC MIKI TI/JUPYTER/Web Scarping Spyder/Export/jobsdb_'+str(today)+'.csv', 'rb').read())
    # part.set_payload(open('C:/Users/pkong/JUPYTER/Web Scarping Spyder/Export/jobsdb_'+str(today)+'.csv', 'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename ="jobs_today_db.csv"')
    msg.attach(part)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context= context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, msg.as_string())
        smtp.quit
    print('success')
    
    
# import sys
# print(sys.version)

# python_location = 'C:/ProgramData/Anaconda3/python.exe'
# file_location = directory+'/Men Jobsdb.py'

