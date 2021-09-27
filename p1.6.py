import random
import turtle
fred = turtle.Pen()
fred.shape("turtle")
fred.width(3)
fred.speed(0)
colorlist = ["red", "blue", "green", "orange", "yellow"]

def square(size):
    for i in range(4):
        fred.forward(size)
        fred.left(90)

def circle(size):
    fred.circle(size)

def polygon(len):
    fred.left(90)
    for _ in range(3):        
        fred.right(360 / 3)
        fred.forward(len)

for i in range(100):
    x = random.randrange(-200, 200)
    y = random.randrange(-200, 200)
    fred.up()
    fred.goto(x, y)
    fred.down()
    col = random.choice(colorlist)
    fred.color(col)
    square(random.randrange(10, 200))
    circle(random.randrange(10, 200))
    polygon(random.randrange(10, 200))
