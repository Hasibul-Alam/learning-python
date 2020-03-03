#!/usr/bin/python3.9
''' Program Writer: Hasibul Alam
    "Play with Python"
    Create a histogram of people apper in a file
    using dictionary datatype.'''
mydict = {}
fname = input('Enter the name \'names.txt\':')
fopen = open('names.txt')
wd = 0
wordlist = []
for line in fopen:
    line.rstrip()
    words = line.split()
    wd = len(words)+wd
    wordlist.extend(words)
    words.clear()
print ('People in the file:\n',wordlist,'\nNo of People:',wd)

choose_name = []
for i in wordlist:
    if i in choose_name:
        continue
    else:
        choose_name.append(i)
#print (choose_name,len(choose_name))
mychoose_name = sorted(choose_name)
#print (mychoose_name)
print ('------------++++++++++++-------------')
hist_name = dict.fromkeys(mychoose_name,0)
count = 0
for name in hist_name.keys():
    for j in wordlist:
        if name == j:
            count+=1
        else:
            continue
    hist_name[name] = count
    count = 0
print ('Histogram of the People:\n',hist_name)
