import random

q1 = 0
score = 0

while True:
    x = random.randint(10, 300)
    y = random.randint(10, 300)
    answer = x + y
    q1 = input("what is {} + {}?".format(x, y))
    if q1 == "q":
        print("your score: ", score)
        break
    if int(q1) == answer:
        print("you got it!")
        score += 1
    elif int(q1) > answer:
        print("thats too high!")
    else:
        print("thats too low!")