import turtle
import os

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# botton 1
botton1 = turtle.Turtle()
botton1.speed(0)
botton1.write("1 player", False, align="center", font=("Courier", 24, "normal"))
botton1.shape("square")
botton1.color("white")
botton1.shapesize(stretch_wid=2,stretch_len=4)
botton1.penup()
botton1.goto(0, 0)

# botton 2
botton2 = turtle.Turtle()
botton2.speed(0)
botton2.write("2 players", align="center", font=("Courier", 24, "normal"))
botton2.shape("square")
botton2.color("white")
botton2.shapesize(stretch_wid=2,stretch_len=4)
botton2.penup()
botton2.goto(0, 60)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


def main():

    # Score
    score_a = 0
    score_b = 0

    # Functions
    def paddle_a_up():
        y = paddle_a.ycor()
        y += 25
        paddle_a.sety(y)

    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 25
        paddle_a.sety(y)

    def paddle_b_up():
        y = paddle_b.ycor()
        y += 25
        paddle_b.sety(y)

    def paddle_b_down():
        y = paddle_b.ycor()
        y -= 25
        paddle_b.sety(y)

    # Keyboard bindings
    wn.listen()
    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")
    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_down, "s")

    # Main game loop
    while True:
        wn.update()
        
        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            os.system("afplay /Users/ryan/Desktop/Ryan_code/images/bounce.wav&")
        
        elif ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            os.system("afplay /Users/ryan/Desktop/Ryan_code/images/bounce.wav&")

        # Left and right
        if ball.xcor() > 350:
            score_a += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1

        elif ball.xcor() < -350:
            score_b += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1
            
        # Paddle and ball collisions
        if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
            ball.dx *= -1
            os.system("afplay /Users/ryan/Desktop/Ryan_code/images/bounce.wav&")
        
        elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
            ball.dx *= -1
            os.system("afplay /Users/ryan/Desktop/Ryan_code/images/bounce.wav&")
                
        # if paddle_b.ycor() < ball.ycor():
        #     paddle_b_up()

        # if paddle_b.ycor() > ball.ycor():
        #     paddle_b_down()
        
        # if paddle_a.ycor() < ball.ycor():
        #     paddle_a_up()

        # if paddle_a.ycor() > ball.ycor():
        #     paddle_a_down()

            
        if score_b >= 10:
            pen.clear()
            pen.write("Player B won! {}".format(score_b), align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1
            paddle_b.dy = 0
            wn.listen()
            pen.clear()
            wn.onkeypress(main, "space")

        if score_a >= 10:
            pen.clear()
            pen.write("Player A won! {}".format(score_a), align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1
            paddle_a.dy = 0       
            wn.listen()
            pen.clear()     
            wn.onkeypress(main, "space")
            
main()