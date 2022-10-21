import pandas as pd
import requests
from bs4 import BeautifulSoup

#Get first page
page = requests.get('https://www.youtube.com')
page
page.text

#Create a BeautifulSoup object 

soup = BeautifulSoup(page.text, 'html.parser')
soup 

print(soup.prettify())

web2 = soup.find_all('div',class_="style-scope ytd-two-column-browse-results-renderer")
output_web2 = []
for i in web2:
    print(i.text)
    data = i.text
    output_web2.append(data)

df = pd.DataFrame({'names':repo_names,'descriptions':repo_descs})