import turtle
import random

score = 0
lives = 10

wn = turtle.Screen()
wn.title("falling skies")
wn.bgcolor("green")
wn.bgpic("background.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

wn.register_shape("horse_left.gif")
wn.register_shape("horse_right.gif")
wn.register_shape("acorn.gif")
wn.register_shape("hunter.gif")



player = turtle.Turtle()
player.shape("horse_left.gif")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"
player.speed(0)

good_guys = []
bad_guys = []

for _ in range(20):
    # Add the good_guys
    good_guy = turtle.Turtle()
    good_guy.speed(0)
    good_guy.shape("acorn.gif")
    good_guy.color("blue")
    good_guy.penup()
    good_guy.goto(100, 250)
    good_guy.speed = random.randint(1, 3)
    good_guys.append(good_guy)
for _ in range(10):
    bad_guy = turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.shape("hunter.gif")
    bad_guy.color("red")
    bad_guy.penup()
    bad_guy.goto(-100, 250)
    bad_guy.speed = random.randint(1, 3)
    bad_guys.append(bad_guy)
    
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.direction = "stop"
pen.write("Score: {} lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
    
def go_left():
    player.direction = "left"
    player.shape("horse_left.gif")

def go_right():
    player.direction = "right"
    player.shape("horse_right.gif")
    
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")


while True:
    wn.update()
    
    if player.direction == "left":
        x = player.xcor()
        x -=good_guy.speed
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x += good_guy.speed
        player.setx(x)

    for good_guy in good_guys:
        y = good_guy.ycor()
        y -= good_guy.speed
        good_guy.sety(y)
        
        if y < -300:
            x = random.randint(-380, 380)       
            y = random.randint(300, 400)
            good_guy.goto(x, y)
             
        if good_guy.distance(player) < 60:
            x = random.randint(-380, 380)       
            y = random.randint(300, 400)
            good_guy.goto(x, y)
            score += 5
            pen.clear()
            pen.write("Score: {} lives: {}".format(score, lives), align="center")
    for bad_guy in bad_guys:
        y = bad_guy.ycor()
        y -= bad_guy.speed
        bad_guy.sety(y)
            
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad_guy.goto(x, y)
                 
        if bad_guy.distance(player) < 60:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad_guy.goto(x, y)
            score -= 5
            lives -= 1
            pen.clear()
            pen.write("Score: {} lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
            
            
wn.mainloop()
