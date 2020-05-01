import turtle
from turtle import Screen

screen = Screen()
tur = turtle.Turtle('turtle')
tur.speed(-1)

def dragging(x,y):
    tur.ondrag(None)
    tur.setheading(tur.towards(x,y))
    tur.goto(x,y)
    tur.ondrag(dragging)

def rightclick(x,y):
    tur.clear()

def main():
    turtle.onscreenclick(dragging,1)
    turtle.onscreenclick(rightclick,3)
    screen.mainloop()

main()
