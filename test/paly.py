# -*- coding: utf-8 -*-
import urllib.request
import re
import urllib


# 1、网址url  --豆瓣网
url = 'http://www.zuowenwang.net/p/216893.html'

# 2、直接请求  返回结果
response = urllib.request.urlopen(url)

# 3、获取状态码，如果是200表示获取成功
print('状态码：', response.getcode())

# 4、读取内容
data = response.read()

# 5、设置编码
data = data.decode('GB2312')

# 6、打印结果
# print(data)



