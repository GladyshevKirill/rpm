import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.rbc.ru/life/news/64888fdf9a79477a0585d069')


bs = BeautifulSoup(response.text, 'lxml')

main = bs.find_all('main', 'main-content-100')
site = main[0].text
site = site[site.find('Список'):]
site = site[:site.find('Поделиться')]
print(site)


