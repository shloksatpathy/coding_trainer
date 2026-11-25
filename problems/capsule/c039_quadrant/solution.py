x, y = map(int, input().split())
if x == 0 and y == 0:
    print("origin")
elif y == 0:
    print("x-axis")
elif x == 0:
    print("y-axis")
elif x > 0:
    if y > 0:
        print("Q1")
    else:
        print("Q4")
else:
    if y > 0:
        print("Q2")
    else:
        print("Q3")
