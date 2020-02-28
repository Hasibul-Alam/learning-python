#!/usr/bin/python3.9
'''List is a collection which is ordered and changeable.
Allows duplicate members.'''
#-----------+++++++++++------------
x = list(['Hasinur', 'Habib', 'Alam'])
print ("Original List:",x)

print('------------+++++++++++++------------')
# The append() method appends an element to the end of the list.
x.append("Hasib")
print('Applied append() method:',x)

print('------------+++++++++++++------------')
# The copy() method returns a copy of the specified list.
z = x.copy()
print ('Applied copy() method:',z)

print('------------+++++++++++++------------')
# The clear() method removes all the elements from a list.
y = x.clear()
print ('Applied clear() method:',y)

print('------------+++++++++++++------------')
# The count() method returns the number of elements with the specified value.
print ('Applied count() method:',z.count('Hasib'))

print('------------+++++++++++++------------')
''' The extend() method adds the specified list elements
(or any iterable like list, set, tuple etc) to the end of the current list.'''
bro = ['Sajib', 'Rajib', 'Rabbi']
z.extend(bro)
print ('Applied extend() method:', z)

print('------------+++++++++++++------------')
''' The index() method returns the position
at the first occurrence of the specified value.'''
print ('Applied index() method:', z.index('Hasib'))

print('------------+++++++++++++------------')
# The insert() method inserts the specified value at the specified position.
z.insert(4,'Sayed')
print ('Applied insert() method:', z)

print('------------+++++++++++++------------')
# The pop() method removes the element at the specified position.
print('Applied pop() method:', z.pop(3),'\nUpdated List:',z)

print('------------+++++++++++++------------')
'''The remove() method removes the first occurrence of
the element with the specified value. elmnt	Required.
Any type (string, number, list etc.) The element you want to remove'''
print ('Applied remove() method:',z.remove('Alam'),'\nUpdated list:',z)

print('------------+++++++++++++------------')
# The reverse() method reverses the sorting order of the elements.
print ('Applied reverse() method:',z.reverse(),'\nReverse List:',z)

print('------------+++++++++++++------------')
'''The sort() method sorts the list ascending by default.
You can also make a function to decide the sorting criteria(s).'''
z.sort()
print('Applied Sort() method:',z)
def myfunction (e):
    return len(e)
z.sort(reverse = True, key = myfunction)
print ('Again applied sort() method using function:',z)

print('------------+++++++++++++------------')
print ("That's all about the methods of list.")
