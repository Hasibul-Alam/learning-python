#!/usr/bin/python3.9
grab=input('Enter a number:')
try:
    a=int(grab)
except:
    a=-1
if a>0:
    print('Nice Work')
else:
    print('Invalid Input!!!')
