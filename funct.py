def addtwo(a,b):
    adder=a+b
    return adder
print(addtwo(2,3))

def greet(name,msg):
    print ('Hello',name,',',msg)

for i in range(2):
    if i == 0:
        han = input('Enter the name:')
    else:
        han1 = input('Type the message:')
greet(han,han1)

def wlcmsg(*names):
    for name in names:
        print (name,'Welcome to PYTHON')
wlcmsg('Hasib,','Habib,','Hasinur,')
