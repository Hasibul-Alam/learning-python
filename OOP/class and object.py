class Parrot:

    # class attribute
    species = 'bird'

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# create object
blu = Parrot('Blu',10)
woo = Parrot('Woo',12)

# access the class attributes
print('Blu is a {}'.format(blu.__class__.species))
print('Woo is a {}'.format(woo.__class__.species))

# access the instance attributes
print('{} is {} years old'.format(blu.name,blu.age))
print('{} is {} years old'.format(woo.name,woo.age))
