import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.rbc.ru/life/news/64888fdf9a79477a0585d069')

with open('rbk.txt', 'w', encoding='utf-8') as file:
    file.write(response.text)

bs = BeautifulSoup(response.text, 'lxml')

#получение праздников paragraphs - это дофига текста
selebrate_title = bs.findAll('h3', 'subtitle tertiary gutter-t')
titles = str(selebrate_title)
len_titles = titles.split('<h3 class="subtitle tertiary gutter-t">')
titles = ''.join(len_titles)
len_titles = titles.split('</h3>')
titles = ''.join(len_titles)
len_titles = titles.split(',')

paragraph = bs.find_all('p', 'paragraph')
paragraphs = str(paragraph)
len_par = paragraphs.split('<p class="paragraph">')
paragraphs = ''.join(len_par)
len_par = paragraphs.split('</p>,')
#print(len_par)


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

#православный праздник
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


#<h3 class="subtitle tertiary gutter-t"> - заголовки православных, народных и мировых праздников.
#<h2 class="subtitle secondary"> - заголовки знаменитостей, памятные даты и именины
#<p class="paragraph"> - православные, народные
#ul class="list circle gutter-b" - международыне, знаменитости, даты в истории, именины

