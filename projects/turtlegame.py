import turtle
import random

tur = turtle.Turtle()
tur.speed(0)
tur.width(5)

colors = ['red','blue','green','yellow','orange','black']

def up():
    tur.setheading(90)
    tur.forward(100)

def down():
    tur.setheading(270)
    tur.forward(100)

def left():
    tur.setheading(180)
    tur.forward(100)

def right():
    tur.setheading(0)
    tur.forward(100)

def leftclick(x,y):
    tur.color(random.choice(colors))
    tur.forward(100)

def rightclick(x,y):
    tur.stamp()

turtle.listen()
turtle.onscreenclick(leftclick,1)
turtle.onscreenclick(rightclick,3)
turtle.onkey(up,'Up')
turtle.onkey(down,'Down')
turtle.onkey(left,'Left')
turtle.onkey(right,'Right')

turtle.mainloop()
