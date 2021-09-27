import turtle
import math


wn = turtle.Screen() 
wn.bgcolor("black")
wn.title("space game")
wn.tracer(0)

game_over = False

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

for size in range(4):
    border_pen.fd(600)
    border_pen.lt(90)    
border_pen.hideturtle()
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()


 

number_of_enemies = 30
enemies = []
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

enemy_start_x = -225
enemy_start_y = 250
enemy_number = 0


for enemy in enemies: 
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x  + (50 * enemy_number)
    y = enemy_start_y
    enemy.setposition(x, y)
    enemy_number += 1
    if enemy_number == 10:
        enemy_start_y -= 50
        enemy_number = 0
        
    enemyspeed = 1

playerspeed = 15

 
bullet = turtle.Turtle()
bullet.color("blue")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 7


bulletstate = "ready"

enemy_bullet = turtle.Turtle()
enemy_bullet.color("blue")
enemy_bullet.shape("triangle")
enemy_bullet.penup()
enemy_bullet.speed(0)
enemy_bullet.setheading(90)
enemy_bullet.shapesize(0.5, 0.5)
enemy_bullet.hideturtle()

enemy_bulletspeed = 7


enemy_bulletstate = "ready"

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = - 280
    player.setx(x)
    
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()
        
def fire_enemy_bullet():
    global enemy_bulletstate
    if enemy_bulletstate == "ready":
        enemy_bulletstate = "fire"
        x = enemy.xcor()
        y = enemy.ycor() - 10
        enemy_bullet.setposition(x, y)
        enemy_bullet.showturtle()
        
def iscollision(t1, t2):
        distince = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
        if distince < 15:
            return True
        else:
            return False
        
wn.listen()
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(fire_bullet, "space")

for enemy in enemies:
    fire_enemy_bullet()

while True:
    wn.update()    
    for enemy in enemies:       
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y-=40
                e.sety(y)
                
            enemyspeed *= -1
            
        if iscollision(bullet, enemy):
                bullet.hideturtle()
                bulletstate = "ready"
                bullet.setposition(0, -400)
                enemy.setposition(0, 10000)

                score += 20
                scorestring = "Score: %s" %score
                score_pen.clear()
                score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal")) 
                
        if iscollision(player, enemy):
            game_over = True


        if game_over:
            player.hideturtle()
            for enemy in enemies:
                enemy.hideturtle()
                print ("game over!")
                game_over = False
                break

    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    if enemy == (0):
        print("you win!") 
