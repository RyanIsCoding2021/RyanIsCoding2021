import random


WIDTH = 700
HEIGHT = 700
score = 0
game_over = False

player = Actor("player")
player.pos = 100, 100


tresure = Actor("treasure")
tresure.pos = 200, 200

def draw():
    screen.fill("green")
    player.draw()
    tresure.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10,10))
    
    if game_over:
        screen.fill("black")
        screen.draw.text("Final Score: + str(score), topleft=(10, 10), fontsize=60")


def place_tresure():
    tresure.pos = (random.randint(10, 700), random.randint(10, 700))

def time_up():
    global game_over
    game_over = True

def update():
    global score
    
    if keyboard.left:
        player.x = player.x - 4
    elif keyboard.right:
        player.x = player.x + 4
    elif keyboard.down:
        player.y = player.y + 4
    elif keyboard.up:
        player.y = player.y - 4
        
    tresure_collected = player.colliderect(tresure)
    
    if tresure_collected:
        score = score + 5
        place_tresure()

clock.schedule(time_up, 100.0)
place_tresure()


    