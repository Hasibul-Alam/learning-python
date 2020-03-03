#!/usr/bin/python3.9
inp=input('How many time you want to ran the program:')
n=int(inp)
for i in range(n):
    grab=input('Enter a Number:')
    a=int(grab)
    if a>=10:
        print('It is a number')
    elif a<10 | a>0:
        print('It is a digit')
    else:
        print('It is a negetive number')
