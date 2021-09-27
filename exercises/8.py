list = [5, 4, 3, 2, 1]

for i in range (len (list)):
    for j in range(i, len(list)):
        print(list[i], end = ' ')
    print()

print()

"5 5 5 5 5"
"4 4 4 4"
"3 3 3"
"2 2"
"1"