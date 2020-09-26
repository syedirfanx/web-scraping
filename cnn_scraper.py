import bs4
from bs4 import BeautifulSoup
import requests
import csv
from csv import writer

source = requests.get('https://edition.cnn.com/world').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cnn_scraper.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Catagory','Headline', 'Link'])

for para in soup.find_all('div', class_='metadata-header__top'):
    catagory = para.h1.text
    print(catagory)
    print()

for para3 in soup.find_all('div', class_="cd__content"):
    headline = para3.h3.a.text
    print(headline)
    print()
    link = para3.find('a')['href']
    print(link)
    print()
    csv_writer.writerow([catagory, headline, link]) 




     
