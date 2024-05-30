import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.rbc.ru/life/news/64888fdf9a79477a0585d069')


bs = BeautifulSoup(response.text, 'lxml')

main = bs.find('main', 'main-content-100')
site = str(main.text)
site = site[site.rfind('Список'):]
site = site[:site.rfind('ПоделитьсяАвторыТеги')]
site = site.replace('Праздники сегодня', '')

word_s = site.find('Международные праздники')
rus_s = site.rfind('Праздники в России')
print(site[word_s:rus_s])

#print(site)
