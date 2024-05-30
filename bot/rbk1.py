import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.rbc.ru/life/news/64888fdf9a79477a0585d069')


bs = BeautifulSoup(response.text, 'lxml')

main = bs.find('main', 'main-content-100')
site = str(main.text)
site = site[site.rfind('Список'):]
site = site[:site.rfind('ПоделитьсяАвторыТеги')]
site = site.replace('Праздники сегодня', '')

w_s = site.find('Международные праздники')
r_s = site.rfind('Праздники в России')
word_s = site[w_s:r_s]

r_s = site.find('Праздники в России')
c_s = site.rfind('Православный праздник')
rus_s = site[r_s:c_s]

c_s = site.find('Православный праздник')
d_s = site.rfind('Праздник по народному календарю')
church_s = site[c_s:d_s]

d_s = site.find('Праздник по народному календарю')
b_s = site.rfind('Дни рождения российских и зарубежных знаменитостей')
demos_s = site[d_s:b_s]

b_s = site.find('Дни рождения российских и зарубежных знаменитостей')
h_s = site.rfind('Памятные даты в истории')
birthday_s = site[b_s:h_s]

h_s = site.find('Памятные даты в истории')
i_s = site.rfind('Кто сегодня отмечает именины')
history_s = site[h_s:i_s]

i_s = site.find('Кто сегодня отмечает именины')
imenins_s = site[i_s:]
#print(site)
