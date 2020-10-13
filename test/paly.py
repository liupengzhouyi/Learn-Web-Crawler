# -*- coding: utf-8 -*-
import requests

from bs4 import BeautifulSoup

url = 'https://www.jb51.net/article/142096.htm'

res = requests.get (url)

print(res.status_code)

soup = BeautifulSoup(res.text,'html.parser')

item = soup.find('a') #使用find()方法提取首个<div>元素，并放到变量item里。

print(type(item)) #打印item的数据类型

print(item)
#打印item









