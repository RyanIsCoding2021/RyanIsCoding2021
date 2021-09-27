
# Python: Snake Game 
import turtle
import time
import random
import os
delay = 0.1

score = 0
high_score = 0

speed = 10
bg = (255, 200, 150)

wn = turtle.Screen()
wn.title("Snake game")
wn.bgcolor("#E7B384")
wn.setup(width=600, height=600)
wn.tracer(0)

#turtle.register_shape("apple.gif")

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(-100,0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#CA4E32")
food.penup()
food.goto(0,100)

bodys = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center",font=("courier", 24, "normal"))

def go_up():
    if head.direction != "down":
        head.direction = "up"        

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"
    
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + speed)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - speed)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + speed)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - speed)


wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
while True:
    wn.update()

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for body in bodys:
            body.goto(1000, 1000)

        bodys.clear()

        score = 0

        delay = 0.1
        
        pen.clear()
        pen.write("Score: {} High Score: {}". format (score, high_score),align="center",font=("courier", 24, "normal"))


        for body in bodys:
            body.goto(1000, 1000)

        bodys.clear()

        score = 0

        delay = 0.1
        
        pen.clear()
        pen.write("Score: {} High Score: {}". format (score, high_score),align="center",font=("courier", 24, "normal"))
    
    if head.distance(food) < speed:
        os.system("afplay bite.wav&")

        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        food.goto(x,y)
        
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("green")
        new_body.penup()
        bodys.append(new_body)

        delay -= 0.00
        
        score += 5
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}". format (score, high_score),align="center",font=("courier", 24, "normal"))



    if head.distance(food) < speed:
        os.system("afplay bite.wav&")

        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        food.goto(x,y)
        
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("grey")
        new_body.penup()

        delay -= 0.00
        
        score += 5
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}". format (score, high_score),align="center",font=("courier", 24, "normal"))

    
        
    for index in range(len(bodys)-1, 0, -1):
        x = bodys[index-1].xcor()
        y = bodys[index-1].ycor()
        bodys[index].goto(x, y)

    if len(bodys) > 0:
        x = head.xcor()
        y = head.ycor()
        bodys[0].goto(x, y)        
    
    move()

    
    for body in bodys:
        if body.distance(head) < speed:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for body in bodys:
                body.goto(1000, 1000)
                
            bodys.clear()

    time.sleep(delay)