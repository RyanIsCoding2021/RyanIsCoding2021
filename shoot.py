import random
apple = Actor("apple")


def draw():
    screen.clear()
    apple.draw()
    
    
def place_apple():
    apple.x = random.randint(10, 800)
    apple.y = random.randint(10, 600)

    
def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shot!")
        place_apple()
    else:
        print("you missed!")
        quit()
    
place_apple()
