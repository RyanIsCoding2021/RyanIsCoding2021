import math

WIDTH = 800
HEIGHT = 600
EGGS = 20
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
FONT_COLOR = (0, 0, 0)
EGG_TARGET = 20
PLAYER_START = (200, 300)
ATTACK_DISTANCE = 280
DRAGON_WAKE_TIME = 2
MOVE_DISTANCE = 4
EGGS_HIDE_TIME = 2

lives = 3
eggs_collectid = 0
game_over = False
game_complete = False
reset_required = False

easy_lair = {
    "dragon": Actor("dragon-asleep", pos=(679, 100)),
    "eggs": Actor("1egg", pos=(400, 100)),
    "egg_count": 1,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": 10,
    "sleep_counter": 0,
    "wake_counter": 0
}

medium_lair = {
    "dragon": Actor("dragon-asleep", pos=(679, 300)),
    "eggs": Actor("2eggs", pos=(400, 300)),
    "egg_count": 2,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": 7,
    "sleep_counter": 0,
    "wake_counter": 0
}

hord_lair = {
    "dragon": Actor("dragon-asleep", pos=(679, 500)),
    "eggs": Actor("3eggs", pos=(400, 500)),
    "egg_count": 3,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": 4,
    "sleep_counter": 0,
    "wake_counter": 0
}

lairs = [easy_lair, medium_lair, hord_lair]
p = Actor("p", pos=PLAYER_START)

def draw():
    global lairs, eggs_collectid, lives, game_complete
    screen.clear()
    screen.blit("bg", (0, 0))
    if game_over:
        screen.draw.text("GAME OVER!", fontsize=60, center=CENTER,  color=FONT_COLOR)
    elif game_complete:
        screen.draw.text("YOU WIN!", fontsize=60, center=CENTER,  color=FONT_COLOR)
    else:
        p.draw()
        draw_lairs(lairs)
        draw_counters(eggs_collectid, lives)
        
def draw_lairs(lairs_to_draw):
    for lair in lairs_to_draw:
        lair["dragon"].draw()
        if lair["egg_hidden"] is False:
            lair["eggs"].draw()
            
def draw_counters(eggs_collected, lives):
    screen.blit("egg-count", (0, HEIGHT - 49))
    screen.draw.text(str(eggs_collectid),
                     fontsize=40,
                     pos=(26, HEIGHT - 30),
                     color="#FFFFFF")
    screen.blit("life-count", (67, HEIGHT - 49))
    screen.draw.text(str(lives),
                     fontsize=40,
                     pos=(90, HEIGHT - 30),
                     color="#FFFFFF")
    screen.draw.text(str(lives),
                     fontsize=40,
                     pos=(90, HEIGHT - 30),
                     color="#FFFFFF")
    
def update():
    if keyboard.right:
        p.x += MOVE_DISTANCE
        if p.x > WIDTH:
            p.x = WIDTH
    elif keyboard.left:
        p.x -= MOVE_DISTANCE
        if p.x < 0:
            p.x = 0
    elif keyboard.down:
        p.y += MOVE_DISTANCE
        if p.y > HEIGHT:
            p.y = HEIGHT
    elif keyboard.up:
        p.y -= MOVE_DISTANCE
        if p.y < 0:
            p.y = 0
    check_for_collisions()
    
def check_for_collisions():
    global lairs, eggs_collectid, lives, reset_required, game_complete
    for lair in lairs:
        if lair["egg_hidden"] is False:
            check_for_egg_collisions(lair)
        if lair["dragon"].image == "dragon-awake" and reset_required is False:
            check_for_dragon_collisions(lair)
            

    
def update_lairs():
    global lairs, p, lives
    for lair in lairs:
        if lair["dragon"].image == "dragon-asleep":
            update_sleeping_dragon(lair)
        elif lair["dragon"].image == "dragon-awake":
            update_waking_dragon(lair)
        update_egg(lair)
            
clock.schedule_interval(update_lairs, 1)

def update_sleeping_dragon(lair):
    if lair["sleep_counter"] >= lair["sleep_length"]:
        lair["dragon"].image = "dragon-awake"
        lair["sleep_counter"] = 0
    else:
        lair["sleep_counter"] += 1
        
def update_waking_dragon(lair):
    if lair["wake_counter"] >= DRAGON_WAKE_TIME:
        lair["dragon"].image = "dragon-asleep"
        lair["wake_counter"] = 0
    else:
        lair["wake_counter"] += 1

def update_egg(lair):
    if lair["egg_hidden"] is True:
        if lair["egg_hide_counter"] >= EGGS_HIDE_TIME:
            lair["egg_hidden"] = False
            lair["egg_hide_counter"] = 0
        else:
            lair["egg_hide_counter"] += 1
            
def check_for_dragon_collisions(lair):
    x_distance = p.x - lair["dragon"].x
    y_distance = p.y - lair["dragon"].y
    distance = math.hypot(x_distance, y_distance)
    if distance < ATTACK_DISTANCE:
        handle_dragon_collisions()
        
def handle_dragon_collisions():
    global reset_required
    reset_required = True
    animate(p, pos=PLAYER_START, on_finished=subtract_life)
    
def check_for_egg_collisions(lair):
    global eggs_collectid, game_complete
    if p.colliderect(lair["eggs"]):
        lair["egg_hidden"] = True
        eggs_collectid += lair["egg_count"]
        if eggs_collectid >= EGG_TARGET:
            game_complete = True
            
def subtract_life():
    global lives, reset_required, game_over
    lives -= 1
    if lives == 0:
        game_over = True
    reset_required = False