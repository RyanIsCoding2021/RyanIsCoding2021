import turtle
turtle.bgcolor("white")
turtle.pensize(2)
def curve() :
    for i in range(100) :
        turtle.right (2)
        turtle.forward(2)
        
turtle.speed (10)
turtle.color("green","purple")
turtle.begin_fill ()
turtle.left (140)
turtle.forward (111.65)
curve()

turtle.left (120)
curve()
turtle.forward (111.65)
turtle.end_fill ()
turtle.hideturtle()
