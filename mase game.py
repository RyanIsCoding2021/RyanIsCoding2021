# Python Maze Game

import turtle
import math
import random

w = turtle.Screen()
w.bgcolor("black")
w.title("Maze Game")
w.setup(700, 700)
w.tracer(0)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("grey")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = (0)
    
    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        
    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()
        
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            
    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            
    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))
        if distance < 5:
            return True
        else:
            return False

class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 24
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])


    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0


        if self.is_close(player):
            if player.xcor()< self.xcor():
                self.direction = "left"
            elif player.xcor()> self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"
                
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction = random.choice(["up", "down", "left", "right"])
            
        turtle.ontimer(self.move, t=random.randint(100, 300))

    def is_close(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 75:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



levels = [""]

level_1 = [
"xxxxxxxxxxxxxxxxxxxxxxxxx",
"xp     xxxxxxx     xxxxxx",
"x   xxxxxxx             x",
"x        xxxxxxx       tx",
"xxxxx    xx        xxxxxx",
"xxxxx    xx           xxx",
"xx         x    xx      x",
"xxxxxx     xxxxxxx      x",
"x e     x          xxxx x",
"x     xxxxxxx    xxxx   x",
"x   xxxxxxxxx    xxxx   x",
"x       xxxxx    xxxx   x",
"xxxxx            xx     x",
"x            xxxxxxxx   x",
"xxxxxxxxx          xxx  x",
"xxxxxxxxxxxxx   e       x",
"xx          xx          x",
"xxxxxxx        xxxxx    x",
"xxxxxxxxxxx             x",
"x               xxxxxxxxx",
"xxxxx      xxxxxx       x",
"xxxxxxxxx   xxxxx       x",
"x e                    tx",
"xxxxxxxxxxxx   xxxxxxxxxx",
"xxxxxxxxxxxxxxxxxxxxxxxxx",
]



level_2 = [
"xxxxxxxxxxxxxxxxxxxxxxxxx",
"xp                 xxxxxx",
"x   xxxxxxx         e   x",
"x        xxxxxxx    xxxxx",
"xxxxx    xx        xxxxxx",
"xxxxxxxxxx              x",
"xx         x    xxx     x",
"xxxxxx     xxxxxxx      x",
"x                xxxx   x",
"x     xxxxxxx    xxxx   x",
"xxxxxxxxxxxxx    xxxx   x",
"x e       xxxxx   xxxx  x",
"xxxxx            xxt    x",
"x            xxxxxxxx   x",
"xxxxxxxxx         xxx   x",
"xxxxxxxxxxxxx           x",
"xx          xx          x",
"xxxxxxx        xxxxx    x",
"xxxxxxxxxxx             x",
"x           e   xxxxxxxxx",
"xxxxx       xx          x",
"xxxxxxxxxxxxxxxxx       x",
"x                      tx",
"xxxxxxxxxxxxxxxxxxxxxxxxx",
"xxxxxxxxxxxxxxxxxxxxxxxxx",
]

level_3 = [
"xxxxxxxxxxxxxxxxxxxxxxxxx",
"xp                 xxxxxx",
"x   xxxxxxx             x",
"x         xxxxxxxxxxxxxxx",
"xxxxx    xx        xxxxxx",
"xxxxx    x              x",
"xx              xxx     x",
"xxxxxx     xxxxxxx      x",
"x                xxxx   x",
"x     xxxxxxx    xxxx   x",
"xxxxxxxxxxxxx    xxxx   x",
"x       xxxxx    xxxx   x",
"xxxxx             xx    x",
"xxxxxxxxxxxxxxxxxxxxx   x",
"xxxxxxxxx  e            x",
"xxxxxxxxxxxxx           x",
"xxt           xx        x",
"xxxxxxx        xxxxx    x",
"xxxxxxxxxxx             x",
"x e              xxxxxxxx",
"xxxxx      xx           x",
"xxxxxxxxxxxxxxxxx       x",
"x                      tx",
"xxxxxxxxxxxxxxxxxxxxxxxxx",
"xxxxxxxxxxxxxxxxxxxxxxxxx",
]


treasures = []
enemies = []

levels.append(level_1)
levels.append(level_2)
levels.append(level_3)

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
              
            if character == "x":
                pen.goto(screen_x, screen_y)
                pen.shape("square")
                pen.stamp()
                walls.append((screen_x, screen_y)) 
                
            if character == "p":
                player.goto(screen_x, screen_y)

            if character == "t":
                treasures.append(Treasure(screen_x, screen_y))
                
            if character == "e":
                enemies.append(Enemy(screen_x, screen_y))
                
    for enemy in enemies:
        turtle.ontimer(enemy.move, t=250)
            

def clean_maze():
    pen.clearstamps()
    walls.clear()
    enemies.clear()
    player.clear()
    treasures.clear()

    
pen = Pen()
player = Player()
walls = []
level_index = 1
setup_maze(levels[level_index])

turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")

while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print ("player Gold: {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)

    for enemy in enemies:        
        if player.is_collision(enemy):
            print ("player dies!")

    w.update()
    
    if len(treasures) == 0:
        level_index += 1
        if level_index >= len(levels):
            print ("game over!")
            break
        clean_maze()
        setup_maze(levels[level_index])