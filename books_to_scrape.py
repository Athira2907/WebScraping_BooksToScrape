import requests
from bs4 import BeautifulSoup
import pandas as pd
url1='https://books.toscrape.com/'
url='https://books.toscrape.com/'
response=requests.get(url)
content=response.text
soup=BeautifulSoup(content,'html.parser')

nav=[]
nav_link=[]
ul=soup.find('div',attrs={'class':'side_categories'}).find('ul',attrs={'class':'nav nav-list'}).find('ul').find_all('li')
for i in ul:
    nav+=[i.find('a').string.replace('\n','').replace(' ','')]
    nav_link+=[url+i.find('a').attrs['href']]

img=[]
title=[]
categ=[]
price=[]
rating=[]
avail=[]

for j in nav_link:
    url=j
    response=requests.get(url)
    content=response.text
    soup=BeautifulSoup(content,'html.parser')
    articles=soup.find_all('article')
    for k in articles:
        img+=[url1+k.find('div',attrs={'class':'image_container'}).find('a').find('img').attrs['src'].replace('../../../../','')]
        title+=[k.find('h3').find('a').string]
        categ+=[soup.find('div',attrs={'class':'page-header action'}).find('h1').get_text()]
        price+=[k.find('div',attrs={'class':'product_price'}).find('p').string]
        rating+=[k.find('p').attrs['class'][1]]
        avail+=[k.find('div',attrs={'class':'product_price'}).find('p',attrs={'class':'instock availability'}).get_text(strip=True)]

df_nav=pd.DataFrame({'Title':title,'Category':categ,'Price':price,'Rating':rating,'Availability':avail,'Image':img})
df_nav.to_excel('books_to_scrape.xlsx',index=False,header=True)