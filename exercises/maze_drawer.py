import turtle
import random
import threading

s = turtle.Screen()
s.bgcolor("#16EA38")
s.setup(width=turtle.window_width, height=700)

turtle1 = turtle.Pen()
turtle1.hideturtle()
turtle1.color("#8F531B")
turtle1.speed(0)
turtle1.penup()
turtle1.goto(-467, 400)
turtle1.pendown()

def generate_maze(turtle, pensize):
    turtle.pensize(pensize)
    turtle.forward(200)
    turtle.left(-90)
    
    turtle.forward(400)
    turtle.left(90)
    
    turtle.forward(200)
    turtle.left(90)
    
    turtle.forward(230)
    turtle.left(-90)
    
    turtle.forward(230)
    turtle.left(90)
    
    turtle.forward(-370)
    turtle.left(90)
    
    turtle.forward(370)
    turtle.left(90)
    
    turtle.forward(270)
    turtle.left(90)
    
    turtle.forward(270)
    turtle.left(90)
    
    turtle.forward(480)
    turtle.left(-90)
    
    turtle.forward(250)
    turtle.left(-90)
    
    turtle.forward(250)
    turtle.left(90)
    
    turtle.forward(130)
    turtle.left(-90)
    
    turtle.forward(-500)
    turtle.left(90)
    
    turtle.forward(-200)
    turtle.left(-90)
    
    turtle.forward(-150)

def draw_rect(turtle, pensize):
    turtle.pensize(pensize)
    turtle.goto()
    turtle.forward(200)
    turtle.left(-90)
    
    turtle.forward(400)
    turtle.left(90)
    
    turtle.forward(200)
    turtle.left(90)
    
    turtle.forward(230)
    turtle.left(-90)
    
    turtle.forward(230)
    turtle.left(90)
    
    turtle.forward(-370)
    turtle.left(90)
    
    turtle.forward(370)
    turtle.left(90)
    
    turtle.forward(270)
    turtle.left(90)
    
    turtle.forward(270)
    turtle.left(90)
    
    turtle.forward(480)
    turtle.left(-90)
    
    turtle.forward(250)
    turtle.left(-90)
    
    turtle.forward(250)
    turtle.left(90)
    
    turtle.forward(130)
    turtle.left(-90)
    
    turtle.forward(-500)
    turtle.left(90)
    
    turtle.forward(-200)
    turtle.left(-90)
    
    turtle.forward(-150)

generate_maze(turtle=turtle1,  pensize=40)


def generate_maze_all(turtles):
    for i in range(500):
        for t in turtles:
            if t.xcor() < -267:
                t.forward(4)
                if t.xcor() >= -267:
                    t.left(-90)
            
            if t.ycor() > 0:
                t.forward(4)
                if t.ycor() <= 0:
                    t.left(90)
            
            # turtle.forward(200)
            # turtle.left(90)
            
            # turtle.forward(230)
            # turtle.left(-90)
            
            # turtle.forward(230)
            # turtle.left(90)
            
            # turtle.forward(-370)
            # turtle.left(90)
            
            # turtle.forward(370)
            # turtle.left(90)
            
            # turtle.forward(270)
            # turtle.left(90)
            
            # turtle.forward(270)
            # turtle.left(90)
            
            # turtle.forward(480)
            # turtle.left(-90)
            
            # turtle.forward(250)
            # turtle.left(-90)
            
            # turtle.forward(250)
            # turtle.left(90)
            
            # turtle.forward(130)
            # turtle.left(-90)
            
            # turtle.forward(-500)
            # turtle.left(90)
            
            # turtle.forward(-200)
            # turtle.left(-90)
            
            # turtle.forward(-150)
    
    
    
    
def walk():
    global enemies
    enemy = enemies[0]
    enemies.remove(enemy)
    generate_maze(enemy, pensize=1)
    
enemies = []

for i in range(3):
    pos = -467 + i * 20
    enemy = turtle.Turtle()
    enemy.hideturtle()
    enemy.color("red")
    enemy.shape("circle")
    enemy.pensize(1)
    enemy.penup()
    enemy.speed(10)
    enemy.goto(pos, 400)

    enemy.showturtle()
    enemies.append(enemy)

# for i in range(len(enemies)):
#     turtle.ontimer(walk, t=random.randint(0, 3))

generate_maze_all(enemies)

# for e in enemies:
#     t = threading.Thread(target=generate_maze, args=(e, 1))
#     t.start()