import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.rbc.ru/life/news/64888fdf9a79477a0585d069')

with open('rbk.txt', 'w', encoding='utf-8') as file:
    file.write(response.text)

bs = BeautifulSoup(response.text, 'lxml')

title = bs.find('p', 'paragraph')
text_title = title.text

word_selebrate = bs.find('ul', 'list circle gutter-b')
word_selebrate_text = word_selebrate.text


