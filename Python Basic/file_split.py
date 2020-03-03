#!/usr/bin/python3.9
fname = input ('Enter a file name:')
try:
    fhand = open (fname)
except:
    print ('File is not found:',fname)
    quit()
count = 0
for line in fhand :
    if line.startswith('Subject:'):
        count += 1
        #print (line)
print ('No. of line startswith **SUBJECT** is:',count)
print ('---------++++++++++---------')
fhand = open('filehandle.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print (words[1:3])
    ##print (words[3])
print ('---------++++++++++---------')
# reading a file into a single string
file = open ('mbox-short.txt')
line = file.read()
print (len(line))
print ('---------++++++++++---------')
print (line[10000])
print ('---------++++++++++---------')
print (line[:100])
print ('---------++++++++++---------')
print (line[100:150])
