import re

def get_findAll_urls(text):
    """
    :param text: 文本
    :return: 返回url列表
    """
    urls=re.findall(r"(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)|([a-zA-Z]+.\w+\.+[a-zA-Z0-9\/_]+)",text)
    urls=list(sum(urls,()))
    urls=[x for x in urls if x!='']
    return urls

with open('/Users/liupeng/PycharmProjects/Learn-Web-Crawler/test/paly.txt') as file_object:
    contents = file_object.read()
    #print(contents)
    get_findAll_urls(contents)



