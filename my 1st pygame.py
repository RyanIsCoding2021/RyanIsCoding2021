from pygame_functions import *
import time

screenSize(600, 600)
setAutoUpdate(False)

setBackgroundImage("images/road1.png")

testSprite  = makeSprite("images/links.gif",32)

moveSprite(testSprite,300,300,True)

showSprite(testSprite)
time.sleep(10)


nextFrame = clock()
frame=0
while True:
     if clock() > nextFrame:
         frame = (frame+1)%8
         nextFrame += 80

     if keyPressed("right"):
         changeSpriteImage(testSprite, 0*8+frame)
         scrollBackground(-5,0)
        
     elif keyPressed("down"):
         changeSpriteImage(testSprite, 1*8+frame)
         scrollBackground(0, -5)
        
     elif keyPressed("left"):
         changeSpriteImage(testSprite, 2*8+frame)
         scrollBackground(5,0)
        
     elif keyPressed("up"):
         changeSpriteImage(testSprite, 3*8+frame)
         scrollBackground(0,5)