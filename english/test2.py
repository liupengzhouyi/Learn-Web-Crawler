import urllib.request


# respouse = urllib.request.urlopen("https://m.kekenet.com/gaokao/201601/421823.shtml")

respouse = urllib.request.urlopen("https://m.kekenet.com/gaokao/15650/")

print(respouse.read().decode("utf-8"))
