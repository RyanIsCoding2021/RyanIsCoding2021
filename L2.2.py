# Lesson 2.2

from tkinter import *
import random
import time

tk = Tk()
canvas = Canvas(tk, width=800, height=600)
tk.title("Drawing")
canvas.pack()

class ball:
    def __init__(self, color, size):
        self.shape = canvas.create_rectangle(10, 10, size, size, fill=color)
        self.xspeed = random.randrange(-10, 10)
        self.yspeed = random.randrange(-10, 10)

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        if pos[3] >= 600 or pos[1] <=0:
            self.yspeed = -self.yspeed
        if pos[2] >= 800 or pos[0] <=0:
            self.xspeed = -self.xspeed
            
colors = ['red', 'green', 'blue', 'orange', 'yellow', 'cyan', 'magenta',
          'dodgerblue', 'turquoise', 'grey', 'gold', 'pink', 'white']
            
balls = []
for i in range(500):
    balls.append(ball(random.choice(colors), random.randrange(50, 100)))
 
        
while True:
    for ball in balls:
        ball.move()
    tk.update()
    time.sleep(0.01)
    
tk.mainloop()