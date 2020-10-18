import urllib.request


# respouse = urllib.request.urlopen("https://m.kekenet.com/gaokao/201601/421823.shtml")

respouse = urllib.request.urlopen("http://zz.xdf.cn/gkbk/202003/048572712.html")

print(respouse.read().decode("utf-8"))
