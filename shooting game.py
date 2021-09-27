import turtle
import numpy as np

WIN_SIZE = 700
cnt = 0

bullet = turtle.Turtle()
bullet.color("red")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bulletspeed = 10

def fire_bullet():
    x = player.xcor()
    y = player.ycor()
    bullet.setposition(x, y)
    bullet.setheading(player.heading())
    bullet.showturtle()

    while True:
        # y = bullet.ycor()
        # y += bulletspeed
        bullet.forward(bulletspeed)

        if bullet.ycor() > WIN_SIZE:
            bullet.hideturtle()
            break             
        
turtle.listen()
turtle.onkey(fire_bullet, "space")

def motion(event):
    global cnt
    cnt += 1
    if np.mod(cnt, 10) != 0:
        return
    x, y = event.x, event.y
    # Transform (0, 0) from top-left to the center
    x -= WIN_SIZE / 2
    y = WIN_SIZE / 2 - y
    print('{}, {}'.format(x, y))
    angle = angle_between((0, 0), (x, y))
    print("angle_between:{}", angle)
    player.setheading(-angle)

def angle_between(p1, p2):
    ang1 = np.arctan2(*p1[::-1])
    ang2 = np.arctan2(*p2[::-1])
    return np.rad2deg((ang1 - ang2) % (2 * np.pi))



w = turtle.Screen()
w.bgcolor("black")
w.title("game")
w.setup(WIN_SIZE, WIN_SIZE)


player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.shapesize(stretch_wid=1, stretch_len=3)


w.mainloop()