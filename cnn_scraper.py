import bs4
from bs4 import BeautifulSoup
import requests
import csv
from csv import writer

source = requests.get('https://edition.cnn.com/world').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cnn_scraper.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Catagory','Headline', 'Link', 'Description'])

for para in soup.find_all('div', class_='metadata-header__top'):
    catagory = para.h1.text
    print(catagory)
    print()

for para3 in soup.find_all('div', class_="cd__content"):
    headline = para3.h3.a.text
    print(headline)
    link = para3.find('a')['href']
    print(link)
   
    if link.split(':')[0] == 'https':
        source2 = requests.get(link).text
    else:
        source2 = requests.get(f'https://edition.cnn.com{link}').text
    soup2 = BeautifulSoup(source2, 'lxml')
    
    for des in soup2.find_all('div', class_="pg-rail-tall__body"):
        try:
            description = des.text
        except Exception as e:
            pass

    print(description)
    print()
    csv_writer.writerow([catagory, headline, link, description]) 




     
