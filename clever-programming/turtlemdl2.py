import turtle
import random

tur = turtle.Turtle()
colors = ['red','blue','green','yellow','orange','black']

# set color for turtle
tur.color('green','red')

# set pen width
tur.width(5)

# fill the shape with color
tur.begin_fill()
tur.circle(50)
tur.end_fill()

tur.penup()
tur.forward(200)
tur.pendown()

tur.color('black','orange')
tur.begin_fill()
for i in range(4):
    tur.forward(100)
    tur.right(90)
tur.end_fill()

for x in range(6):
    randColor = random.randrange(0, len(colors))
    tur.color(colors[randColor] , colors[randColor])
    rand1 = random.randrange(-400,400)
    rand2 = random.randrange(-400,400)
    tur. penup()
    tur.setpos(rand1,rand2)
    tur.pendown()
    tur.begin_fill()
    tur.circle(random.randrange(0,80))
    tur.end_fill()

turtle.done()
