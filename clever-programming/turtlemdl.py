import turtle

wn = turtle.Screen()
wn.bgcolor('light green')
wn.title('Turtle')
skk = turtle.Turtle()
skk.speed(1)

def square():
    skk.forward(100)
    skk.left(90)

for i in range(5):
    square()
    if i == 4:
        skk.forward(200)
        for j in range(4):
            square()

#turtle.done()

tur = turtle.Turtle()
tur.color('red')
tur.pensize(5)
tur.shape('turtle')
turtle.done()
