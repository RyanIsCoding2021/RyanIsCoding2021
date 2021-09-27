import turtle as t
import random

s = t.Screen()
s.title("rect")
t.speed(0)


colorlist = ["black", "blue", "green", "red"]

def drawRect(width, height):
    for i in range(2):
        t.color(colorlist[random.randint(0, 3)])
        t.fd(width)
        t.lt(90)
        t.fd(height)
        t.lt(90)
            
# def drawRect(width, height):
#     for i in range(4):
#         if i == 0:
#             t.fd(width)
#             t.lt(90)
#         elif i == 1:
#             t.fd(height)
#             t.lt(90)
#         elif i == 2:
#             t.fd(width)
#             t.lt(90)
#         elif i == 3:
#             t.fd(height)
#             t.lt(90)

# def drawRect(size):
#     for i in range(4):
#         t.fd(size)
#         t.lt(90)


for i in range(40):
    # drawRect(size=random.randint(20, 500))    
    drawRect(random.randint(100, 200), random.randint(100, 200))
    
    
    
    
    
    

s.mainloop()