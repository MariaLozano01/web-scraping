import pandas as pd
import requests
from bs4 import BeautifulSoup

#Get first page
page = requests.get('https://www.stonybrook.edu/commcms/korean/academics/language')
page
page.text

#Create a BeautifulSoup object 

soup = BeautifulSoup(page.text, 'html.parser')
soup

print(soup.prettify())

web1 = soup.find_all('h3')
web1s = []
for i in web1:
    print(i.text)
    data = i.text 
    web1s.append(data)
len(web1s)
for data in  web1s:
    print(data)


web2 = soup.find_all('span', class_= 'subtitle')
web2s = []
for i in web2:
    print(i.text)
    data1 = i.text 
    web2s.append(data1)
len(web2s)
for data1 in  web2s:
    print(data1)

list1 = web1s
list2 = web2s

dictionary = {'program': list1, 'courses': list2}
df = pd.DataFrame({'program':web1s ,'courses':web2s})
df.to_csv('/Users/marialozano/Documents/GitHub/web-scraping/data/Korean_info.csv')