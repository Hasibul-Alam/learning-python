#!/usr/bin/python3.9
while True:
    grab=input('Enter a Number:')
    if grab=='end':
        break
    else:
        a=int(grab)
        if a>=10:
            print('It is a number')
        elif a<10 | a>0:
            print('It is a digit')
        else:
            print('It is a negetive number')
print('Now you are out of the program')
