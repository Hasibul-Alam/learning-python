baseval = -1
for i in [5,12,7,74,56,67]:
    if baseval < i:
        baseval = i
print('Max value:',baseval)
found = False
print('Before',found)
for i in [12,35,18,64,59]:
    if i == 18:
        found = True
        print(found,i)
print('After',found)
