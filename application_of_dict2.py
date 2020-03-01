#!/usr/bin/python3.9
''' Program Writer: Hasibul Alam
    "Play with Python"
    Create a histogram of people apper in a file
    using dictionary datatype. This program is
    upgrade version of application_of_dict.py'''
fname = input('Enter the name \'names.txt\':')
fopen = open('names.txt')
names = []
for line in fopen:
    line.rstrip()
    names.extend(line.split())
print ('People in the file:\n',names,'\nNo of People:',len(names))
sorted_names = sorted(names)
print ('------------++++++++++++-------------')
hist_name = dict()
for name in sorted_names:
    hist_name [name] = hist_name.get(name,0)+1
print ('Histogram of the People:\n',hist_name)
