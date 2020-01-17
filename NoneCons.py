smallest = None
for value in [54,95,84,17,14,38,7,19]:
    if smallest is None:
        smallest = value
        print("smallest",smallest)
    elif smallest > value:
        smallest = value
    print("smallest",smallest,value)
print('Final',smallest)
