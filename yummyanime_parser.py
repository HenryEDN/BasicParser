import requests

from bs4 import BeautifulSoup as BS
from os import system
from datetime import datetime



URL = 'https://yummyanime.club/top'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 OPR/72.0.3815.186',
            'accept': '*/*'}
count = 0

r = requests.get(URL, headers = HEADERS)
html = BS(r.content, 'html.parser')

if r.status_code != 200:
    input("ERROR\nPress enter to exit.")
    system('exit')

with open('Parser\yummyanime_parser\yummyanime_content.txt', mode='w', encoding='UTF-8') as txt_file:
    now = datetime.today().replace(microsecond=0)
    txt_file.write('\t\tTop 100 anime\n\n' + 'From: ' + URL + '\nDate: ' + str(now) +'\n\n')
    for el in html.select('.anime-column'):
        count +=1
        title = el.select('.anime-title')
        views = el.select('.icons-row > div')
        votes = el.select('.icons-row > div')
        rate = el.select('.rating-info > span')
        txt_file.write('title: "' + title[0].text + '"' \
        + '\nposition: ' + '#' + str(count) \
        + '\nviews: ' + views[1].text.replace(' ', '').replace('\n', '') \
        + '\nvotes: ' + votes[-1].text.replace(' ', '').replace('\n', '') \
        + '\nrate: ' + rate[1].text.replace('\n', '') \
        + '\n\n')
print('Контент успешно записался!')