#!/usr/bin/python3.9
han = open ('mbox-short.txt')
for line in han:
    line = line.rstrip()
    wds = line.split()
    type (wds)
    if len(wds) < 3 or wds[0] != 'From':
        continue
    ##print(wds)
    '''if wds[0] != 'From':
        continue'''
    print(wds[2])
