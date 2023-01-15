from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

#Starts the driver and goes to our starting webpage
driver = webdriver.Chrome(
    'C:/Web Scraping course/chromedriver.exe'
)

driver.get('https://store.unionlosangeles.com/collections/outerwear')

#Will keep scrolling down the webpage until it cannot scroll no more
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if last_height == new_height:
        break
    last_height = new_height

#Imports the HTML of the webpage into python      
soup = BeautifulSoup(driver.page_source, 'lxml')

#Grabs the section of the HTML that has all our products
section = soup.find('div', {'id':'main', 'role':'main'})

#grabs the HTML of each product
postings = section.find_all('li')

#Creates a dataframe
df = pd.DataFrame({'Link':[''], 'Vendor':[''],'Title':[''], 'Price':['']})

#Grabs the product details for every product on the page and adds each product as a row in our dataframe
for post in postings:
    try:
        link = post.find('a').get('href')
        vendor = post.find(class_ = 'cap-vendor').text
        title = post.find(class_ = 'cap-title').text
        price = post.find(class_ = 'cap-price').text
        df = df.append({'Link':link, 'Vendor':vendor,'Title':title, 'Price':price}, ignore_index = True)
    except:
        pass

#fixes the link of the first 4 products on the page    
df['Link'][4:] = 'https://store.unionlosangeles.com'+df['Link'][4:]




