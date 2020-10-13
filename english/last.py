import time

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

index = 1
for i in list:
    print("正在爬取第" + str(index) + "篇阅读理解\n")
    print("...")
    fileName = 'reading' + str(index)
    path = '../english/pages/' + fileName + '.md'
    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
    url = 'https://m.kekenet.com' + i
    html_doc = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(html_doc.content, features='lxml', from_encoding='utf8')
    links = soup.find_all('p')

    file2 = open(path, 'w+', encoding='utf-8')
    file2.write('# Read')
    file2.write('\n')
    for link in links[3:]:
        link.encode('gb18030')
        if link.text == ' 官方APP |官方微信 | 查词':
            break
        if link.text == '阅读答案':
            file2.write('## 阅读答案')
        else:
            if link.text[0:3] == '1. ':
                s = link.text
                s = s.replace("A. ", "\n * A. ")
                s = s.replace("B. ", "\n * B. ")
                s = s.replace("C. ", "\n * C. ")
                s = s.replace("D. ", "\n * D. ")

                file2.write(s)
            elif link.text[0:3] == '2. ':
                s = link.text
                s = s.replace("A. ", "\n * A. ")
                s = s.replace("B. ", "\n * B. ")
                s = s.replace("C. ", "\n * C. ")
                s = s.replace("D. ", "\n * D. ")

                file2.write(s)
            elif link.text[0:3] == '3. ':
                s = link.text
                s = s.replace("A. ", "\n * A. ")
                s = s.replace("B. ", "\n * B. ")
                s = s.replace("C. ", "\n * C. ")
                s = s.replace("D. ", "\n * D. ")

                file2.write(s)
            elif link.text[0:3] == '4. ':
                s = link.text
                s = s.replace("A. ", "\n * A. ")
                s = s.replace("B. ", "\n * B. ")
                s = s.replace("C. ", "\n * C. ")
                s = s.replace("D. ", "\n * D. ")

                file2.write(s)
            elif link.text[0:3] == '5. ':
                s = link.text
                s = s.replace("A. ", "\n * A. ")
                s = s.replace("B. ", "\n * B. ")
                s = s.replace("C. ", "\n * C. ")
                s = s.replace("D. ", "\n * D. ")

                file2.write(s)
            elif link.text[0:3] == '6. ':
                s = link.text
                s = s.replace("A. ", "\n * A. ")
                s = s.replace("B. ", "\n * B. ")
                s = s.replace("C. ", "\n * C. ")
                s = s.replace("D. ", "\n * D. ")

                file2.write(s)
            else:
                file2.write(link.text)
        file2.write('\n')
        # print(link.text)
        # print('\n')
    file2.close()
    index = index + 1
    print("第" + str(index) + "篇阅读理解爬取完成✅\n")
    time.sleep(1.5)  # 休眠0.1秒




