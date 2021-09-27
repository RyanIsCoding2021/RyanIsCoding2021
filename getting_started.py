import sys

if 1 + 1 == 2:
    print ("Hello!")
else:
    print ("goodbye!")
    
for count in range(10):
    if ((count % 2) == 0):
        print(count)
        print("is even")
    else:
        print(count)
        print("is odd")

import pgzrun

def draw():
    screen.draw.text("Hello", topleft=(10, 10), background="black")

pgzrun.go()

score = 0

print(score)


x = 2
y = x % 3
print(y)


name = "Martin"
print(name)
greeting = "Hello"
name = "Martin"
message = greeting + name
print(message)

age = 10
if age == 10:
    print("you are 10 years old.")
game_over = True
if game_over == True:
    print("game over!")
else:
    print("keep playing!")
    
ghosts = 5
if ghosts > 3:
    print("it's so spoooooky!!!")
elif ghosts > 0:
    print("get the ghosts!")
else:
    print("ghosts all gone!")


robots = ["bing", "bong", "boop"]
for robot in robots:
    print("I am a robot. my name is " + robot)

robots = ["bing", "bong", "boop"]
colors = ["red", "blue", "orange"]
index = 0
for each in robots:
    print("I am a robot. my name is " + robots[index] + ". I am " + colors[index])
    index = index + 1
    
answer = input("Throw a water balloon? (y/n)")
while answer == "y":
    print("Splash!!!")
    answer = input("Throw a water balloon? (y/n)")
print("goodbye!")


name = input("what is your name?")
print(name)
if name == "wei" or name == "ryan" or name == "xuan":
    print("come in!")
else:
    print("members only")
        
countdown = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
countdown.reverse()
print(countdown)