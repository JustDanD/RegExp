import re

file1 = open('11.txt', 'r')
file2 = open('12.txt', 'r')
file3 = open('13.txt', 'r')
file4 = open('14.txt', 'r')
file5 = open('15.txt', 'r')
texts = []
texts.append(file1.read())
texts.append(file2.read())
texts.append(file3.read())
texts.append(file4.read())
texts.append(file5.read())

for i in texts:
    i = re.sub('-', '_', i)
    result = re.sub(r'(\b\w+\b)(\s*\b\1\b)+', r'\1', i)
    result = re.sub('_', '-', result)
    print(result)