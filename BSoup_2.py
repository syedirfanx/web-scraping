import bs4
from bs4 import BeautifulSoup
import requests

source = requests.get('https://syedirfanx.me/myfavourites').text

soup = BeautifulSoup(source, 'lxml')

for favourites in soup.find_all('div', class_='whole-wrap'):
    try:
        headline = favourites.h2.text
        print(headline)

        description = favourites.h3.text
        print(description)

        video_src = favourites.find('iframe')['src']
        print(video_src)

        video_id = video_src.split('/')[4]
        print(video_id)

        yt_link = f'https://youtube.com/watch?v={video_id}'
        print(yt_link)
    except Exception as e:
        pass
