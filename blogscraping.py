import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.wunderground.com/')

soup= BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all('div')

print(posts)
