#webscraping

#BeautifulSoup is good for the HTML anchor tag variations when scraping web pages

#download file from py4e.com and then import urllib.request, urllib.parse, urllib.error from bs4 import BeautifulSoup

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
#open and read URL input
soup = BeautifulSoup(html, 'html.parser')
#can query against this variable, sorts all a href imperfections

tags = soup('a')
#function to find all links on webpage
for tag in tags:
    print(tag.get('href',None))
    
#Harrison I don't know if Walmart allows for scraping, tried https://www.google.com and it worked but when i search https://www.walmart.com/browse/home/shower-curtains/4044_539095_533461 it doesnt return all the anchor tags

#this is what comes up for walmart.com /
    #https://help.walmart.com/app/answers/detail/a_id/8
    #https://corporate.walmart.com/privacy-security
    #/account/api/ccpa-intake?native=false&type=sod
    #/account/api/ccpa-intake?native=false&type=access