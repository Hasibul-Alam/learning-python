#!/usr/bin/python3.9
'''' Program Writer: Hasibul Alam
    "Play with Python"
    Create a histogram of people apper in a file
    using dictionary datatype. This program is
    upgrade version of application_of_dict*.py'''

fgrab = input('Enter the file name \'names.txt\':')
fhan = open(fgrab)
names = dict()
for line in fhan:
    words = line.split()
    for name in words:
        names[name] = names.get(name,0)+1
bigcount = None
bigname = None
lst = list()
for word,count in names.items():
    if bigcount is None or count > bigcount:
        bigname = word
        bigcount = count
    tup = (count,word)
    lst.append(tup)
x = sorted(lst[:5], reverse = True)
print('Reversely sorted first five tuple:')
for v,k in x:
     print(k,v)
print('Bigcount:',bigname,bigcount)
