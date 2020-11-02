import re
def clean(a, b, c):
    for i in range(len(b)):
        a = a.replace(b[i], c[i])
    return a
def regfunc():
    file = open('Macbeth.txt', 'r')
    text = file.read()

    text_cl = clean(text, ['\n', '    ', '   ', '  ', '   ', ' ', '  ', '[', ']'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', '', ''])
    #print(text_cl)
    text_cl = text_cl.replace('\'', '_')
    text_cl = text_cl.replace('-', 'Я')
    text_cl = text_cl.replace('.', '..')
    text_cl = text_cl.replace('!', '!!')
    text_cl = text_cl.replace('?', '??')
    result = re.findall(r'[\.\?!] \b[\w-]+\b[,;\-\s:\"]*\b[\w-]+\b[,;\-\s:\"]*\b[\w-]+\b[,;\-\s:\"]*\b[\w-]+\b[,;\-\s:\"]*\b[\w-]+\b[,;\-\s:\"]*\b[\w-]+\b[,;\-\s:\"]*[\.\?!]', text_cl)
    for i in range(len(result)):
        result[i] = clean(result[i], ['. ', '? ', '! '], ['', '', ''])
        result[i] = result[i].replace('Я', '-')
        result[i] = result[i].replace('_', '\'')
    res = []
    for i in result:
        cnt = 0
        for j in i.split():
            smres = re.findall(r'[aAeEiIoOuUyY]', j)
            if len(smres) == 2:
                cnt += 1
        if cnt == 1:
            res.append(i)
        cnt = 0
    print(res)
    return res
def noregfunc():
    file = open('Macbeth.txt', 'r')
    text = file.read()
    text_cl = clean(text, ['\n', '    ', '   ', '  ', '   ', ' ', '  ', '[', ']'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', '', ''])
    massent = re.split('[\.\?!]', text_cl)
    sent6 = []

    for i in massent:
        if len(i.split()) == 6:
            sent6.append(i)
    res = []
    for s in sent6:
        cnt = 0
        for w in s.split():
            vowcnt = 0
            for l in w:
                if l == 'a' or  l == 'A' or l == 'e' or l == 'E' or l == 'i'  \
                        or l == 'I' or l == 'o' or l == 'O' or l == 'u' or l == 'U' or l == 'y' or l == 'Y':
                    vowcnt += 1
            if vowcnt == 2:
                cnt += 1
        if cnt == 1:
            res.append(s)
    print(res)
    return res
def testfunc():
    regres = regfunc()
    noregres = noregfunc()
    for i in range(len(noregres)):
        noregres[i] = re.sub('^ ', '', noregres[i])
    for i in range(len(regres)):
        regres[i] = re.sub('[\.\?!]', '', regres[i])
    if regres == noregres:
        print('True')
    else:
        print('False')
testfunc()

