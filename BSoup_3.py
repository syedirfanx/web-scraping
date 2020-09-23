import bs4
from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.theverge.com/science').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('BSoup_3.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Writer', 'Month', 'Date'])

for para in soup.find_all('div', class_='c-entry-box--compact__body'):
    try:
        headline = para.h2.a.text
        print(headline)

        subtitle = para.div.span.a.span.text
        print(subtitle)

        time = para.div.span.time.text
        mon = time.split(' ')[10]
        print(mon)

        date = time.split(' ')[11]
        date = date.split('/')[0]
    except Exception as e:
        date = time.split(' ')[12]
        date = date.split('/')[0]

    print(date)
    print()
    csv_writer.writerow([headline, subtitle, mon, date])
