from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

#Starts the driver and goes to our starting webpage
driver = webdriver.Chrome(
    'C:/Web Scraping course/chromedriver.exe'
)

driver.get('https://ca.indeed.com/')

#Inputs a job title into the input box
input_box = driver.find_element_by_xpath('//*[@id="text-input-what"]')
input_box.send_keys('data analyst')

#Clicks on the search button
button = driver.find_element_by_xpath('//*[@id="whatWhereFormId"]/div[3]/button').click()

#Creates a dataframe
df = pd.DataFrame({'Link':[''], 'Job Title':[''], 'Company':[''], 'Location':[''],'Salary':[''], 'Date':['']})

#This loop goes through every page and grabs all the details of each posting
#Loop will only end when there are no more pages to go through
while True:  
    #Imports the HTML of the current page into python
    soup = BeautifulSoup(driver.page_source, 'lxml')
    
    #Grabs the HTML of each posting
    postings = soup.find_all('div', class_ = 'jobsearch-SerpJobCard unifiedRow row result clickcard')
    
    #grabs all the details for each posting and adds it as a row to the dataframe
    for post in postings:
        link = post.find('a', class_ = 'jobtitle turnstileLink').get('href')
        link_full = 'https://ca.indeed.com'+link
        name = post.find('h2', class_ = 'title').text.strip()
        company = post.find('span', class_ = 'company').text.strip()
        try:
            location = post.find('div', class_ = 'location accessible-contrast-color-location').text.strip()
        except:
            location = 'N/A'
        date = post.find('span', class_ = 'date').text.strip()
        try:
            salary = post.find('span', class_ = 'salaryText').text.strip()
        except:
            salary = 'N/A'
        df = df.append({'Link':link_full, 'Job Title':name, 'Company':company, 'Location':location,'Salary':salary, 'Date':date},
                       ignore_index = True)
    
    #checks if there is a button to go to the next page, and if not will stop the loop
    try:
        button = soup.find('a', attrs = {'aria-label': 'Next'}).get('href')
        driver.get('https://ca.indeed.com'+button)
    except:
        break

