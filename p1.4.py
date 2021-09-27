import turtle

s = turtle.Screen()
s.title("drawer")

fred = turtle.Pen()
fred.shape("turtle")
fred

for i in range(4):
    fred.forward(100)
    fred.left(90)

fred.reset()   
for i in range(8):
    fred.forward(100)
    fred.left(225)

fred.reset()
for i in range(20):
    fred.forward(10 * i)
    fred.left(90)


    
fred.reset()
fred.speed(0)
for i in range(50):
    fred.circle(i * 3)
    fred.left(10)


fred.reset()
fred.speed(0)
fred.color("red")
fred.width(4)
for i in range(20):
    fred.circle(i*3, 180)
    fred.right(45)



fred.reset()
fred.speed(0)
fred.color("green")
fred.width(5)
for i in range(100):
    fred.forward(i*2)
    fred.circle(i*2, 90)
    fred.right(20)
    
s.exitonclick()