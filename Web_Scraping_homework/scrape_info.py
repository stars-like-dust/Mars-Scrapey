
# Dependencies
import os
from splinter import Browser
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)
from bs4 import BeautifulSoup as bs
import requests
import pymongo
import tweepy
import pandas as pd
import json
import time


#Begin Scraping of NASA News
#URL of page to be scraped
url = 'https://mars.nasa.gov/news/'

# Retrieve page with the requests module
response = requests.get(url)
# Create BeautifulSoup object; parse with 'lxml'
soup = bs(response.text, 'lxml')

#Start NASA Mars News

title = soup.title.text
#print(title)


#Print out first title
results_1 = soup.find('div', 'content_title','a').text

print(results_1)



#Print out 1st paragraph
results_2 = soup.find('div', 'rollover_description_inner').text
print(results_2)


#Start JPL Space Image

url_2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url_2)
time.sleep(5)
browser.click_link_by_partial_text('FULL IMAGE')
time.sleep(5)
expand = browser.find_by_css('a.fancybox-expand')
expand.click()
time.sleep(5)

Bowser = browser.html
image_soup = bs(Bowser, 'html.parser')


next_URL = image_soup.find('img', class_='fancybox-image')['src']
final_URL = f'https://www.jpl.nasa.gov{next_URL}'
print(final_URL)


# In[7]:


# Twitter API Keys
from config import (consumer_key,
                    consumer_secret,
                    access_token,
                    access_token_secret)

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Target User
target_user = "MarsWxReport"
public_tweets = api.user_timeline(target_user)


# Loop through all tweets
for tweet in public_tweets:

    # Utilize JSON dumps to generate a pretty-printed json
     print(json.dumps(tweet, sort_keys=True, indent=4))


#Print Tweet
text=(tweet['text'])
text


#Begin Mars Facts

url = 'http://space-facts.com/mars/'

# Retrieve page with the requests module
response = requests.get(url)
# Create BeautifulSoup object; parse with 'lxml'
soup = bs(response.text, 'lxml')


#title
title = soup.title.text
print(title)


#Print tbody
results_3 = soup.find_all('tbody')
print(results_3)


#print out column 1
results_4 = soup.find_all('tr')

result4list=[]
for x in results_4:
    result4list.append(x.text)
    
print(result4list)

#start loop 2, strip for text and put into a dictionary

Planetdata = {}
for x in result4list:
    rowdata= x.strip().split(':')
    Planetdata[rowdata[0]]=rowdata[1]
print(Planetdata)


# Mars Hemispheres
url_10 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
response = requests.get(url_10)
# Create BeautifulSoup object; parse with 'lxml'
soup_pea = bs(response.text, 'lxml')
soup_pea



# In[17]:


title = soup.title.text
print(title)

#'Cerberus Hemisphere Enhanced
browser.visit(url_10)
time.sleep(10)
browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
time.sleep(10)
html = browser.html
soup = bs(html, 'html.parser')
cerberus_link = soup.find('div', 'downloads').a['href']


# In[20]:


cerberus_link


# In[21]:


#Schiaparelli Hemisphere Enhanced
browser.visit(url_10)
time.sleep(10)
browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
time.sleep(10)
html = browser.html
soup = bs(html, 'html.parser')
Schiaparelli = soup.find('div', 'downloads').a['href']


# In[22]:


Schiaparelli


# In[23]:


#Syrtis Major Hemisphere Enhanced

browser.visit(url_10)
time.sleep(10)
browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
time.sleep(10)
html = browser.html
soup = bs(html, 'html.parser')
Syrtis = soup.find('div', 'downloads').a['href']


# In[24]:


Syrtis


# In[25]:


#Valles Marineris Hemisphere Enhanced
browser.visit(url_10)
time.sleep(10)
browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
time.sleep(10)
html = browser.html
soup = bs(html, 'html.parser')
Valles = soup.find('div', 'downloads').a['href']


# In[26]:


Valles


# In[27]:


# Create single dictionary

#Ultimate_Dic = {}
#Ultimate_Dic['NASA Mars Title'] = results_1
#Ultimate_Dic['NASA MARS Paragraph'] = results_2
#Ultimate_Dic['Featured Image'] = final_URL
#Ultimate_Dic['Data List'] = Planetdata
#Ultimate_Dic['Mars Tweet'] = text
#Ultimate_Dic['Title1'] = 'Cerebus', cerberus_link
#Ultimate_Dic['Title2'] = 'Schiaparelli', Schiaparelli
#Ultimate_Dic['Title3'] = 'Syrtis', Syrtis
#Ultimate_Dic['Title4'] = 'Valees', Valles

#Ultimate_Dic

#insert Ulitmate_Dic to pymango

#conn = 'mongodb://localhost:27017'
#client = pymongo.MongoClient(conn)
#db = client.Mars_info_home
#collection = db['Mars_collection']
#collection.insert_one(Ultimate_Dic)





