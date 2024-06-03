import requests
from bs4 import BeautifulSoup

response = requests.get('https://my-calend.ru/holidays')


bs = BeautifulSoup(response.text, 'lxml')

holidays = bs.find('ul', 'holidays-items')
holidays = str(holidays.text)
holidays = ''.join([i for i in holidays if not i.isdigit()])
