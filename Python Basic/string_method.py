#!/usr/bin/python3.9
str = '   This is Hasibul Alam.\nI am 26 years old.\nI like to play football.'
'''striping from left and the opposit is rstrip()
and strip() does striping from the both side'''
str1 = '  Hey! How are you? '
print ( str1. strip () )
print ('----------=========----------')
print ( str . lstrip() )
print ('----------=========----------')
# startwith() method check weather the string start with a particular string.
dir (str)
print ( str . startswith ('Please') )
print ('----------=========----------')
# Using in operator, can search the presence of a chereacter or a substring.
print ( 'is' in str )
print ('----------=========----------')
# finding a substring
print ( str . find ('26') )
print ( str )
print ('----------=========----------')
# Changing the string in lower case
print ( str . lower () )
print ('----------=========----------')
# changing the string in upper case
print ( str . upper () )
print ('----------=========----------')
'''Replacing substrings with new string.
It will replace all the substring found
simillar to the particular string'''
print ( str . replace ('26', 'twenty six') )
