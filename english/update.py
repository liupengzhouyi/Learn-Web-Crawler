

newPath = '../english/newReading/reading.md'
file2 = open(newPath, 'w+', encoding='utf-8')
for i in range(1, 100):
    path = '../english/pages/reading' + str(i) + '.md'


    f = open(path)
    line = f.readline()  # 调用文件的 readline()方法
    print("正在标准化第" + str(i) + "篇阅读理解\n")
    file2.write('---\n')
    print("...")
    while line:
        if line[0:2] == '1.':
            file2.write('### ' + line)
        elif line[0:2] == '2.':
            file2.write('### ' + line)
        elif line[0:2] == '3.':
            file2.write('### ' + line)
        elif line[0:2] == '4.':
            file2.write('### ' + line)
        elif line[0:2] == '5.':
            file2.write('### ' + line)
        elif line[0:2] == 'A.':
            file2.write('* ' + line)
        elif line[0:2] == 'B.':
            file2.write('* ' + line)
        elif line[0:2] == 'C.':
            file2.write('* ' + line)
        elif line[0:2] == 'D.':
            file2.write('* ' + line)
        else:
            file2.write(line)
        line = f.readline()
    f.close()
    file2.write('\n')
    file2.write('\n')
    file2.write('\n')
    print("标准化第" + str(i) + "篇阅读理解完成✅\n")

file2.close()