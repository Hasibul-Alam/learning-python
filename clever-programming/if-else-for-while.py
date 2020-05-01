import turtle, random

tur = turtle.Turtle('turtle')
tur.speed(1)
tur.color('green')

def square():
    tur.forward(100)
    tur.right(90)
    tur.forward(100)
    tur.right(90)
    tur.forward(100)
    tur.right(90)
    tur.forward(100)

def triangle():
    tur.forward(200)
    tur.left(120)
    tur.forward(200)
    tur.left(120)
    tur.forward(200)

def hexagonal():
    tur.forward(100)
    tur.right(60)
    tur.forward(100)
    tur.right(60)
    tur.forward(100)
    tur.right(60)
    tur.forward(100)
    tur.right(60)
    tur.forward(100)
    tur.right(60)
    tur.forward(100)

turtle_speed = int(input('Enter the speed of a turtle: '))
rabbit_speed = int(input('Enter the speed of a rabbit: '))

if rabbit_speed > turtle_speed:
    square()
else:
    triangle()

rand1 = random.randrange(-200, 200)
rand2 = random.randrange(-200, 200)

tur.setpos(rand1, rand2)
for i in range(4):
    square()

tur.setpos(rand2, rand1)
while(True):
    tur.color('orange')
    hexagonal()
    break
 
turtle.done()
