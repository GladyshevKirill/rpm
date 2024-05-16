import requests
from bs4 import BeautifulSoup
import re

response = requests.get('https://www.rbc.ru/life/news/64888fdf9a79477a0585d069')

with open('rbk.txt', 'w', encoding='utf-8') as file:
    file.write(response.text)

bs = BeautifulSoup(response.text, 'lxml')

#получение праздников paragraphs - это дофига текста
#h3 subtitle tertiary gutter-t
selebrate_title = bs.findAll('h3', 'subtitle tertiary gutter-t')
titles = str(selebrate_title)
len_titles = titles.split('<h3 class="subtitle tertiary gutter-t">')
titles = ''.join(len_titles)
len_titles = titles.split('</h3>')
titles = ''.join(len_titles)
len_titles = titles.split(',')

#paragraph
paragraph = bs.find_all('p', 'paragraph')
paragraphs = str(paragraph)
len_par = paragraphs.split('<p class="paragraph">')
paragraphs = ''.join(len_par)
len_par = paragraphs.split('</p>,')
#print(len_par)

#subtitle secondary
secondary = bs.find_all('h2', 'subtitle secondary')
sec = str(secondary)
len_sec = sec.split('<h2 class="subtitle secondary">')
sec = ''.join(len_sec)
len_sec = sec.split('</h2>')
sec = ''.join(len_sec)
print(len_sec)

#ul class="list circle gutter-b
ul = bs.findAll('ul', 'list circle gutter-b')
print(ul[0].text)
#заголовок
prazdniki_segodnya = len_sec[0]
prazdniki_segodnya = prazdniki_segodnya.replace('[', '')
print(prazdniki_segodnya)

#мировые праздники
vstuplenie = len_par[0]
vstuplenie = vstuplenie.replace('[', '')
print(vstuplenie)
a = len_titles[0]
a = a.replace('[', '')
print(a, ':')
word_selebrate = bs.find('ul', 'list circle gutter-b')
word_selebrate = word_selebrate.text
print(word_selebrate)

#православные праздники
b = len_titles[1]
print(b, ':')
print(len_par[1])

#народный календарь
c = len_titles[2]
c = c.replace(']', '')
print(c,':')
narodni_kalendar = len_par[2]
narodni_kalendar = narodni_kalendar.replace('</p>]', '')
print(narodni_kalendar)

#дни рождения зарубежных знамениостей
d = len_sec[1]
d = d.replace(', ', '')
print(d, ':')

#<h3 class="subtitle tertiary gutter-t"> - заголовки православных, народных и мировых праздников.
#<h2 class="subtitle secondary"> - заголовки знаменитостей, памятные даты и именины
#<p class="paragraph"> - православные, народные
#ul class="list circle gutter-b" - международыне, знаменитости, даты в истории, именины

