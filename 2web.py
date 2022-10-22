import pandas as pd
import requests
from bs4 import BeautifulSoup

#Get first page
page = requests.get('https://www.stonybrook.edu/commcms/studentaffairs/res/housing/undergraduate_housing/chavez_tubman_nobel')
page
page.text

#Create a BeautifulSoup object 

soup = BeautifulSoup(page.text, 'html.parser')
soup 

print(soup.prettify())

web3 = soup.find_all('h3')
web3s = []
for i in web3:
    print(i.text)
    data = i.text
    web3s.append(data)

web4 = soup.find_all('ul', class_="accordion-controls drop-accordion drop-accordion-1 clearfix")
web4s = []
for i in web4:
    print(i.text)
    data = i.text 
    web4s.append(data)
len(web4s)
for data in  web4s:
    print(data)


web4s.append('Dorm')
web4s.append('West Campus')
web4s.append('Undergraduate Dorms')
web4s.append('More Questions?')
web4s.append('Via Phone')

list1 = web3s
list2 = web4s

len(web3s)
len(web4s)


dictionary = {'title': list1, 'dorms': list2}
df = pd.DataFrame({'title': web3s,'dorms': web4s})
df.to_csv('/Users/marialozano/Documents/GitHub/web-scraping/data/Dorms_info.csv')
