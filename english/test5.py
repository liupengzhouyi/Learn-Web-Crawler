# chinese

import requests
from bs4 import BeautifulSoup

book_page = requests.get("https://www.cnblogs.com/hanxiangmin/p/11294420.html", )
print(book_page.status_code)
status_code = book_page.status_code

# if status_code == 200:
#    print("The content is " + book_page.content)


bs_page = BeautifulSoup(book_page.content, features='lxml', from_encoding='utf8')

print(u"Article_info is {}")
article_info = bs_page.find_all('p')
file2 = open('../english/pages/'+'test.txt','w',encoding='utf-8')
for article in article_info:
    article.encode('gb18030')
    print(article.text)
    file2.write(article.text)
file2.close()