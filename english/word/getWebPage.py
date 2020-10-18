

# newPath = '../word/word.md'
# file2 = open(newPath, 'w+', encoding='utf-8')
# file2.write('''
# |   词汇   |   音标   |   翻译   |
# | ---- | ---- | ---- |
# ''')
path = '../word/ppp.txt'
f = open(path)
line = f.readline()  # 调用文件的 readline()方法
while line:
    if len(line) >= 3:
        if '[' in line:
            word = line[0:line.index('[')]
            phoneticSymbols = line[line.index('['):line.index(']')+1]
            translation = line[line.index(']')+1:len(line)-1]
            # file2.write('|   ' + word + '   |  ' + phoneticSymbols + '    |   ' + translation + '   |\n')

            # print(word)
            # print(phoneticSymbols)
            # print(translation)
            # print(line)
        else:
            print(line)


    line = f.readline()
f.close()
# file2.close()






