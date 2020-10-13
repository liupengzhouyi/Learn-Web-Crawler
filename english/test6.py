# file

file1 = open('../english/test5.py','r',encoding='utf-8')
filecontent = file1.read()
print(filecontent)
file1.close()

file2 = open('../english/test7.py','w+',encoding='utf-8')
file2.write(filecontent)
file2.close()