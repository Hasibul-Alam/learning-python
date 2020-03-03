#!/usr/bin/python3.9
''' A dictionary is a collection which is unordered, changeable and indexed.
In python dictionaries are written with curly brackets, and they have keys and values.'''
# Create a dictionary with dict constractor
d = dict(stu1_name = 'Hasibul', stu1_id = 1, stu1_mark = 90,
stu2_name = 'Habib', stu2_id = 2, stu2_mark = 88,
stu3_name = 'Hasinur', stu3_id = 8, stu3_mark = 75)
print ('Dictionary_constructor:',d)

#Here is the above program with curly brackets:
print ('----------++++++++++++++++----------')
d1 = {
'stu1_name' : 'Hasibul', 'stu1_id' : 1, 'stu1_mark' : 90,
'stu2_name' : 'Habib', 'stu2_id' : 2, 'stu2_mark' : 88,
'stu3_name' : 'Hasinur', 'stu3_id' : 8, 'stu3_mark' : 75
}
print ('Curly Bracket:',d1)

# Accessing Items
print ('----------++++++++++++++++----------')
# Access the items by referring to its key name, inside square brackets.
print ('Accessed Item:',d ['stu3_name'])
# Access an item with get() method
print ('Accessed Item with get():',d.get('stu2_name'))

# Change values
print ('----------++++++++++++++++----------')
# change value of an item by referring its key value.
d['stu3_mark'] = 80
print ('Changed_value:',d['stu3_mark'])

# Loop Through a Dictionary
print ('----------++++++++++++++++----------')
# print all the keys of the dictionary
print ('--------Keys--------')
for i in d:
    print (i)
for h in d.keys():
    print (h)
# print all the values of the Dictionary
print ('--------Values-------')
for j in d:
    print (d[j])
print ('--------Values()-------')
# print (d.values())
for k in d.values():
    print (k)
# loop through both keys and Values eith item() method
print ('-------key:value = item()-------')
for x,y in d.items():
    print (x,':',y)

# Check if Key Exists and Dictionary Length
print ('----------++++++++++++++++----------')
if 'stu1_name' in d:
    print('Yes, key is found')
else:
    print('Key is not found')
# length of the dictionary
print ('Dictionary Length:',len(d))

# Addition & Deletion of items in a Dictionary
print ('----------++++++++++++++++----------')
d['stu4_name'] = 'Alam'
d['stu4_id'] = 10
print ('Item added:',d)
# Remove last inserted item
print (d.popitem())
# Remove specific Item
print (d.pop('stu4_name'))
print (d)
''' del keyword also remove specified item
    del d['stu4_name']'''

# Clear & remove a Dictionary
print ('----------++++++++++++++++----------')
d1.clear()
del d1

# Copy a Dictionary with copy() && dict() method
print ('----------++++++++++++++++----------')
mydict = d.copy()
print ('Copied Dictionary:',mydict)
mydict1 = dict(mydict)
print ('Copied with dict() method:',mydict1)

# Nested Dictionary
print ('----------++++++++++++++++----------')
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print ('Nested Dictionary:',myfamily)
# Nest three dictionary already Exists
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
family = {
   'child1' : child1,
   'child2' : child2,
   'child3' : child3
}
print ('2nd Nested Dictionary:',family)

# fromkeys() method
print ('----------++++++++++++++++----------')
p = ('key1', 'key2', 'key3')
q = 0
thisdict = dict . fromkeys(p, q)
print ('Dictionary with fromkey():', thisdict)

# setdefault() method returns value of specified keyself.
print ('----------++++++++++++++++----------')
car = {
  'brand' : 'Toyota',
  'model' : 'X-Noha',
  'year' : 2006
}
c = car . setdefault('model', 'Corolla')
c1 = car . setdefault('color', 'Black')
print ('Setdefault value:',c,c1)

# Insert an Item to a Dictionary with update() method
print ('----------++++++++++++++++----------')
car.update({'length':'7 ft'})
print ('Updated Dictioonary:',car)

# Python Dictionary Comprehension
print ('----------++++++++++++++++----------')
'''Dictionary comprehension consists of an expression pair (key: value)
followed by for statement inside curly braces {}.'''
squares = {x : x*x for x in range(6)}
print ('Comprehension Dict:',squares)
odd_square = {x : x*x for x in range(6) if x%2 ==1}
print ('Comprehension Dict with condition:', odd_square)
