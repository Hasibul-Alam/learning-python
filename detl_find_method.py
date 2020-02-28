data = 'From halambd7@diu.edu.bd sat jan 3:30 AM'
atpos = data . find ('@')
print ( atpos )
# find a string starting from a certain position
dtpos = data . find ( ' ' , atpos )
print ( dtpos )
# slicing a string
str = data [ atpos + 1 : dtpos ]
print ( str )
