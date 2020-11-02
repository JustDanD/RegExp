import re
file1 = open('31.txt', 'r')
file2 = open('32.txt', 'r')
file3 = open('33.txt', 'r')
file4 = open('34.txt', 'r')
file5 = open('35.txt', 'r')
texts = []
texts.append(file1.read())
texts.append(file2.read())
texts.append(file3.read())
texts.append(file4.read())
texts.append(file5.read())
for text in texts:
    mas = 'ауоыиэяюёеАУОЫИЭЯЮЁЕaAeEiIoOuUyY'
    vars = []
    text = re.sub('-', '_', text)
    while len(text) > 0:
        result = re.search(r'\b\w*[ауоыиэяюёеАУОЫИЭЯЮЁЕaAeEiIoOuUyY]{2,2}\w*\b\s*\b\w+\b', text)
        if result != None:
            text = re.sub(result.group(0).split()[0], '', text)
            vars.append(result.group(0))
        else:
            break
    #print(vars)
    #print(text)
    res = []
    for i in vars:
        a = i.split()[0]
        w = i.split()[1]
        cnt = 0
        for i in w:
            if i not in mas and i != '_':
                cnt += 1
        if cnt <= 3:
            res.append(a)
    for i in range(len(res)):
        res[i] = re.sub('_', '-', res[i])
    print(res)
