def calculate(x):
    sum = 0
    for i in range(x + 1):
        # 0, 1, 2, 3
        sum = sum + i
        print(i, end = ' + ')
    return sum

while True:

    x = int(input("enter number?"))
    print(x)
    sum = calculate(x)
    print("= {}".format(sum))