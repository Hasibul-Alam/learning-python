list_of_numbers = [1, 2, 2, 3, 4, 5, 5, 5, 6, 6]
no_duplicate_set = set(list_of_numbers)
no_duplicate_list = list(no_duplicate_set)
list_of_numbers = no_duplicate_list
print(list_of_numbers)

library_1 = {'Harry Potter', 'Hunger Games', 'Lord of the rings'}
library_2 = {'Harry Potter', 'Romeo and Juliet'}

# union_operation find common and uncommon elements of both sets
union_operation = library_1.union(library_2)
print('All book in the town:',union_operation)

# intersection_operation find only common element in both sets
intersection_operation = library_1.intersection(library_2)
print('Books found in both library:',intersection_operation)

# difference_operation find the uncommon element of the first set
difference_operation = library_1.difference(library_2)
print(difference_operation)
