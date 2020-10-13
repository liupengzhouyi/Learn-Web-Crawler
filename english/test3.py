import requests
from bs4 import BeautifulSoup

list = []

headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
for i in range(1, 7):
    url = 'https://m.kekenet.com/gaokao/15650/List_' + str(i) + '.shtml'
    html_doc = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(html_doc.text, 'lxml')
    links = soup.find_all('a')
    for link in links:
        s = link['href']
        if s[0:9] == '/gaokao/2':
            list.append(link['href'])


url = 'https://m.kekenet.com/gaokao/15650/index.shtml'
html_doc = requests.get(url=url, headers=headers)
soup = BeautifulSoup(html_doc.text, 'lxml')
links = soup.find_all('a')
for link in links:
    s = link['href']
    if s[0:9] == '/gaokao/2':
        list.append(link['href'])



for i in list:
    print(i)

# https://m.kekenet.com/gaokao/201601/421823.shtml

