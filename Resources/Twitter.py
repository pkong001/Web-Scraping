'''
!!!IMPORTANT READ!!!
This code may not work when you run it and it's because one of the classes we called may have changed,
I put a comment below where to expect the error iF there is one and how to fix it
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import time

#Starts the driver and goes to our starting webpage
driver = webdriver.Chrome(
        'C:/Web Scraping course/chromedriver.exe')

driver.get('https://twitter.com/login')
time.sleep(2)

#Variable that contains the celebirty or profile our program will scrape
#This program will scrape Ryan Reynolds tweets as indicated in the line below
celebrity = 'Ryan Reynolds'

#inputs an email and password for the login details
login = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
login.send_keys('webscrapingbot@gmail.com')
password = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
password.send_keys('thisisabot')

#Presses the login button, and creates a wait time to let the home page fully load in
#if your getting an error here just make your browser full screen, it should work then
button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div').click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input')))

#inputs the name from the celebrity variable into the search box and presses enter
search = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input')
search.send_keys(celebrity)
search.send_keys(Keys.ENTER)
time.sleep(2)

#Clicks on the people tab which has all the accounts associated with who we searched up
people = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[2]/nav/div/div[2]/div/div[3]/a/div').click()
time.sleep(2)

#clicks on our celebrities profile
profile = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/a/div/div[1]/div[1]/span').click()
time.sleep(2)

#Imports the HTML of the celebrities profile into python
soup = BeautifulSoup(driver.page_source, 'lxml')

#grabs the HTML of each tweet
#ERROR WARNING! If there is an error try recopying the class attribute here, twitter may have changed it by like one or two letters whcih affects our code
postings = soup.find_all('div', class_ = 'css-901oao r-18jsvk2 r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0') 


#This loop will keep scrolling down the webpage loading in and collecting new tweets until we have scraped 100 unique tweets
tweets = []
while True:
    for post in postings:
        tweets.append(post.text)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    #need to change the class here to match it with the other posting variable if there is an error
    postings = soup.find_all('div', class_ = 'css-901oao r-18jsvk2 r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0')
    tweets2 = list(set(tweets))
    if len(tweets2) > 200:
        break

#Subsets our list of tweets to only contain the tweets with a specific word located in it
new_tweets = []    
for i in tweets2:
    #To change that specific word just input into the string below
    if '' in i:
        new_tweets.append(i)
    
        












