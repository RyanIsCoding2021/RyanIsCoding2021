import turtle
import os
import random
import time

level = 1
lives = 100

#turtle.register_shape("plane.gif")
#turtle.register_shape("launcher.gif")
#turtle.register_shape("badguy.gif")


turtle.fd(0)            # move forward
turtle.speed(0)
turtle.bgcolor("black") # background color
#turtle.bgpic('mars.gif')
turtle.title("spacewar")
turtle.ht()             # hide turtle
turtle.setundobuffer(1) # Set or disable undobuffer
turtle.tracer(10)        # Turn turtle animation on/off and set delay for update drawings


class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()    # Pull the pen up – no drawing when moving.
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1
        
    def move(self):
        self.fd(self.speed)
        
        if self.xcor() > 290:
            self.setx(290)
            self.rt(60)

        if self.xcor() < -290:
            self.setx(-290)
            self.rt(60)

        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)

        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)

    def is_collision(self, other):
        if (self.xcor() >= (other.xcor() - 20)) and \
        (self.xcor() <= (other.xcor() + 20)) and \
        (self.ycor() >= (other.ycor() - 20)) and \
        (self.ycor() <= (other.ycor() + 20)):
            return True
        else:
            return False

        
class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 3
        self.level = 1
        #self.shape("plane.gif")


    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1


class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 5
        self.setheading(random.randint(0, 360))
        #self.shape("badguy.gif")


class Ally(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 7
        self.setheading(random.randint(0, 360))
        #self.shape("launcher.gif")

    def move(self):
        self.fd(self.speed)
        
        if self.xcor() > 290:
            self.setx(290)
            self.lt(60)

        if self.xcor() < -290:
            self.setx(-290)
            self.lt(60)

        if self.ycor() > 290:
            self.sety(290)
            self.lt(60)

        if self.ycor() < -290:
            self.sety(-290)
            self.lt(60)

class Missile(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.3, stretch_len=0.4, outline=None)
        self.speed = 40
        self.status = "ready"
        self.goto(-1000, 1000)
        

    def fire(self):
        if self.status == "ready":
            os.system("afplay laser_sound.wav&")
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"

    def move(self):
        if self.status == "ready":
            self.goto(-1000, 1000)
        
        if self.status == "firing":self.xcor() < -290 or \
            self.fd(self.speed)
        if self.xcor() < -290 or self.xcor() > 290 or \
            self.ycor()< -290 or self.ycor()> 290:
                self.goto(-1000, 1000)
                self.status = "ready"

class Particle(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
        self.goto(-1000,-1000)
        self.frame = 0

    def explode(self, startx, starty):
        self.goto(startx, starty)
        self.setheading(random.randint(0,360))
        
    def move(self):
        self.fd(10)

        
                
class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        

    def draw_border(self):
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()
        
    def show_status(self, isGameOver = False):
        self.pen.undo()
        msg = "Score: %s" %(self.score)
        msg += "\nLevel: %s" % level
        msg += "\nLives: %s" % lives
        if isGameOver == True:
            msg += "\n\nGame Over ! "
        self.pen.penup()
        self.pen.goto(-300, 310)
        self.pen.write(msg, font=("Arial", 16, "normal"))

        
game = Game()
game.draw_border()
game.show_status()                       
                 
player = Player("triangle", "white", 0, 0)
missile = Missile("triangle", "yellow", 0, 0)

enemies = []
for i in range(15):
    enemies.append(Enemy("circle", "red", -100, 0))

allies = []
for i in range(15):
    allies.append(Ally("circle", "blue", 100, 0))

particles = []
for i in range(30):
    particles.append(Particle("circle", "orange", 0,0))

turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.onkey(missile.fire, "space")
turtle.listen()

hideCount = 0

while True:
    player.move()
    missile.move()

    if len(enemies) == hideCount:
        hideCount = 0
        level += 1
        game.show_status()
        for enemy in enemies:
            enemy.st()
        for _ in range(0, 2):
            enemies.append(Enemy("circle", "red", -100, 0))
    
    for enemy in enemies:
        enemy.move()

        if player.is_collision(enemy):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            game.score -= 5
            lives -= 1
            game.show_status()
            

            
        if missile.is_collision(enemy):
            enemy.ht()
            hideCount += 1
            game.show_status()
            missile.status = "ready"
            game.score += 5
            game.show_status()
            for particle in particles:
                particle.goto(missile.xcor(), missile.ycor())
                particle.setheading(random.randint(0, 360))
                

                                  
    for ally in allies:
        ally.move()

        if missile.is_collision(ally):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            ally.goto(x, y)
            missile.status = "ready"
            game.score -= 5
            game.show_status()

    for particle in particles:
        particle.move()

    if lives == 0:
        game.show_status(True)
        break