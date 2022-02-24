# Libraries 
from bs4 import BeautifulSoup
import requests 
import time 
import datetime 
import smtplib


URL = 'https://www.amazon.com.au/PlayStation-5-Console/dp/B08HHV8945'

headers = {'"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36",'}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content,"html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id="productTitle").get_text)()

print(title)