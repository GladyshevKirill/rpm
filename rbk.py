import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.rbc.ru/life/news/64888fdf9a79477a0585d069')

with open('rbk.txt', 'w', encoding='utf-8') as file:
    file.write(response.text)

bs = BeautifulSoup(response.text, 'lxml')

#<h3 class="subtitle tertiary gutter-t"> - заголовки православных, народных и мировых праздников.
selebrate_title = bs.findAll('h3', 'subtitle tertiary gutter-t')

#<p class="paragraph"> - православные, народные
paragraph = bs.find_all('p', 'paragraph')

#<h2 class="subtitle secondary"> - заголовки знаменитостей, памятные даты и именины
secondary = bs.find_all('h2', 'subtitle secondary')

#ul class="list circle gutter-b" - международыне, знаменитости, даты в истории, именины
ul = bs.findAll('ul', 'list circle gutter-b')

print(selebrate_title[0].text, ':')
print(ul[0].text)

print(selebrate_title[1].text, ':')
print(paragraph[1].text)

print(selebrate_title[2].text, ':')
print(paragraph[2].text)

print(secondary[1].text, ':')
print(ul[1].text)

print(secondary[2].text, ':')
print(ul[2].text)

print(secondary[3].text, ':')
print(paragraph[4].text)