
num_stars = 0
for i in range (9): # lines
    if i < 5:
        num_stars += 1
    else:
        num_stars -= 1
    for j in range(num_stars): # stars
        print(end = '* ')
    print()

print()

"*"
"* *"
"* * *"
"* * * *"
"* * * * *"
"* * * *"
"* * *"
"* *"
"*"