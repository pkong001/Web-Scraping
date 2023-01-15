import requests
from bs4 import BeautifulSoup
import pandas as pd

#Imports the HTML into python
url = 'https://www.nfl.com/standings/league/2019/reg/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')


#Subsets the HTML to only get the HTML of our table needed
table = soup.find('table', {'summary':'Standings - Detailed View'})

#Gets all the column headers of our table
headers = []
for i in table.find_all('th'):
    title = i.text.strip()
    headers.append(title)

#Creates a dataframe using the column headers from our table
df = pd.DataFrame(columns = headers)

#gets all our data within the table and adds it to our dataframe
for row in table.find_all('tr')[1:]:
    #line below fixes the formatting issue we had with the team names
    first_td = row.find_all('td')[0].find('div', class_ = 'd3-o-club-fullname').text.strip()
    data = row.find_all('td')[1:]
    row_data = [td.text.strip() for td in data]
    row_data.insert(0,first_td)
    length = len(df)
    df.loc[length] = row_data



