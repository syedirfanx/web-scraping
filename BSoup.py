import bs4
from bs4 import BeautifulSoup

import requests

with open("myexperience.html") as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

for match in soup.find_all('div', class_='timeline-event-copy'):

    company = match.h3.a.text
    print(company)

    summery = match.ul.text
    print(summery)
