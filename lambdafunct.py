#!/usr/bin/python3.9
# Program to show the use of lambda functions
square = lambda x: x*x
print (square(25))
#----------+++++++++++-----------
# program to find and sort even number in a list using filter()
my_list = [2,1,5,8,4,9,6]
new_list = list(filter(lambda x: x%2 == 0, my_list))
new_list.sort()
print ('Even numbers:',new_list)
# ------------++++++++++++++-------------
# Program to double each item in a list using map()
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
# Output: [2, 10, 8, 12, 16, 22, 6, 24]
print(new_list)
