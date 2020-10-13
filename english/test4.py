import requests
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}

url = 'https://m.kekenet.com/gaokao/201509/397224.shtml'
html_doc = requests.get(url=url, headers=headers)
soup = BeautifulSoup(html_doc.content, features='lxml', from_encoding='utf8')
links = soup.find_all('p')
file2 = open('../english/pages/'+'test.txt','w+',encoding='utf-8')
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
            print(s)
            file2.write(s)
        elif link.text[0:3] == '2. ':
            s = link.text
            s = s.replace("A. ", "\n * A. ")
            s = s.replace("B. ", "\n * B. ")
            s = s.replace("C. ", "\n * C. ")
            s = s.replace("D. ", "\n * D. ")
            print(s)
            file2.write(s)
        elif link.text[0:3] == '3. ':
            s = link.text
            s = s.replace("A. ", "\n * A. ")
            s = s.replace("B. ", "\n * B. ")
            s = s.replace("C. ", "\n * C. ")
            s = s.replace("D. ", "\n * D. ")
            print(s)
            file2.write(s)
        elif link.text[0:3] == '4. ':
            s = link.text
            s = s.replace("A. ", "\n * A. ")
            s = s.replace("B. ", "\n * B. ")
            s = s.replace("C. ", "\n * C. ")
            s = s.replace("D. ", "\n * D. ")
            print(s)
            file2.write(s)
        elif link.text[0:3] == '5. ':
            s = link.text
            s = s.replace("A. ", "\n * A. ")
            s = s.replace("B. ", "\n * B. ")
            s = s.replace("C. ", "\n * C. ")
            s = s.replace("D. ", "\n * D. ")
            print(s)
            file2.write(s)
        else:
            file2.write(link.text)
    file2.write('\n')

    print(link.text)
    print('\n')

file2.close()

#2. According to Mr. Yuan from Hunan, the opening of the Southern China Great Wall is a good way to ________.A. rebuild the wall B. help local Miao minority peopleC. discover the history D. arouse foreigners' interest

