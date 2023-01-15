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
driver.get('https://www.qualityexpress.co.th/tour/Japan?keyword=&country=Japan&page=1&view=list')


# SETTING UP THE PARAMETER FOR THE BROWSER
#for 2560x1440
height = 1850
width = 1385
driver.set_window_size(height,width)
time.sleep(1)
scroll_down()
time.sleep(1)
#DEFINE THE DATAFRAME FOR ADDING DATAS
df = pd.DataFrame({'title':[''],
                   'airline':[''],
                   'full_link':[''],
                   'img':[''],
                   'code':[''],
                   'duration':[''],
                   'countries':[''],
                   'cities':[''],
                   'description':[''],
                   'price':[''],
                   'schedule':['']})
df = df[1:]

soup = BeautifulSoup(driver.page_source, 'lxml')
postings = soup.find_all('div', class_ = 'col-xs-12 col-sm-12 col-lg-12 tour-box-main no-padding')


for i in postings:
    title = i.find('div', class_ = 'title-category').text #Title
    try:
        airline = title.split('สายการบิน')[1]
    except:
        try:
            airline = title.split('การบิน')[1]
        except:
            airline = title.split('สายการ')[1]
        
    link = i.find('a').get('href')
    base_link = 'https://www.qualityexpress.co.th'
    full_link = base_link + link
    img = i.find_all('img')[0].get('src')
    code = i.find('p', class_ = 'st-code').text 
    duration = i.find('div', class_ = 'col-lg-4 col-sm-5 col-xs-6 no-padding').find_all('p')[1].text #Duration
    countries = i.find('p', class_ = 'tour_sch').text #Countries
    cities = i.find('div', class_ = 'col-lg-6 col-sm-5 col-xs-6 no-padding').find_all('p')[1].text #Cities
    description = i.find('p', class_ = 'desc_new hidden-xs').text.strip().replace('\uf052','').replace('\t','').replace('\n','')
    price = i.find('div', class_ = 'price-category').text.replace('฿','').replace(',','')
    schedule = i.find('p', class_ = 'month_per').text.replace('\xa0','')
    df = df.append({'title':title,
                    'airline':airline,
                    'full_link':full_link,
                    'img':img,
                    'code':code,
                    'duration':duration,
                    'countries':countries,
                    'cities':cities,
                    'description':description,
                    'price':price,
                    'schedule':schedule}, ignore_index = True)
df.to_csv("G:/Other computers/PIC MIKI TI/JUPYTER/Web Scarping Spyder/Export/japan tour.csv")
    

#NOTE-------------------------------
# title = postings[0].find('div', class_ = 'title-category').text #Title
# airline = title.split('โดยสายการบิน')[1]
# link = postings[0].find('a').get('href')
# base_link = 'https://www.qualityexpress.co.th'
# full_link = base_link + link
# img = postings[0].find_all('img')[0].get('src')
# img
# code = postings[0].find('p', class_ = 'st-code').text #Code
# duration = postings[0].find('div', class_ = 'col-lg-4 col-sm-5 col-xs-6 no-padding').find_all('p')[1].text #Duration
# countries = postings[0].find('p', class_ = 'tour_sch').text #Countries
# cities = postings[0].find('div', class_ = 'col-lg-6 col-sm-5 col-xs-6 no-padding').find_all('p')[1].text #Cities
# description = postings[0].find('p', class_ = 'desc_new hidden-xs').text.strip().replace('\uf052','').replace('\t','').replace('\n','')
# price = postings[0].find('div', class_ = 'price-category').text.replace('฿','').replace(',','')
# schedule = postings[0].find('p', class_ = 'month_per').text.replace('\xa0','')

# #EXPORTING FILE
# from datetime import date
# today = date.today()
# #df.to_csv('C:/Users/pkong/JUPYTER/Web Scarping Spyder/jobsdb export_'+str(today)+'.csv')

# #df.to_csv(directory +'/Export/'+ str(today) + 'jobsdb_export_2.csv')
# # df.to_csv("G:/Other computers/PIC MIKI TI/JUPYTER/Web Scarping Spyder/Export/jobsdb_"+str(today)+".csv")
# df.to_csv('C:/Users/pkong/JUPYTER/Web Scarping Spyder/Export/jobsdb_'+str(today)+'.csv')
#ENDNOTE------------------------------


#SENDING EMAIL TO RECIPIENTS    ------------------------
# from email.message import EmailMessage
# import ssl
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart
# from email import encoders

# recipients = ['pkongdan01@gmail.com','pkongdan02@gmail.com']

# for i in recipients:
#     email_sender = 'pkong.py@gmail.com'
#     email_password = 'vujuandcrbzkosuj'
#     email_receiver = i
#     print(i)
#     subject = 'Export Jobs research Raw data'
#     body = """
#     This is the export file for today dude!!!
    
#     """
    
#     msg = MIMEMultipart()
#     msg['Subject'] = subject
#     msg['From'] = email_sender
#     msg['To'] = email_receiver
    
#     part = MIMEBase('application', 'octet-stream')
#     part.set_payload(open('G:/Other computers/PIC MIKI TI/JUPYTER/Web Scarping Spyder/Export/jobsdb_'+str(today)+'.csv', 'rb').read())
#     # part.set_payload(open('C:/Users/pkong/JUPYTER/Web Scarping Spyder/Export/jobsdb_'+str(today)+'.csv', 'rb').read())
#     encoders.encode_base64(part)
#     part.add_header('Content-Disposition', 'attachment; filename ="jobs_today_db.csv"')
#     msg.attach(part)
#     context = ssl.create_default_context()
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465, context= context) as smtp:
#         smtp.login(email_sender, email_password)
#         smtp.sendmail(email_sender, email_receiver, msg.as_string())
#         smtp.quit
#     print('success')
    
#END OF EMAIL PART-------------------
    
# import sys
# print(sys.version)
# python_location = 'C:/ProgramData/Anaconda3/python.exe'
# file_location = directory+'/Men Jobsdb.py'

