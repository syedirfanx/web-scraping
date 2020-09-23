import bs4
from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.theverge.com/science').text

soup = BeautifulSoup(source, 'lxml')

for para in soup.find_all('div', class_='c-entry-box--compact__body'):
    try:
        headline = para.h2.a.text
        print(headline)

        subtitle = para.div.span.a.span.text
        print(subtitle)

        time = para.div.span.time.text
        month = time.split(" ")[10]
        print(month)

        date = time.split(" ")[11]
        date = date.split("/")[0]

        print(date)

        print()
    except Exception as e:
        date = time.split(" ")[12]
        date = date.split("/")[0]
        print(date)
