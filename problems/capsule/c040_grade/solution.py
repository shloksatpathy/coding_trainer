s = int(input())
if s < 0 or s > 100:
    print("invalid")
else:
    if s >= 90:
        letter = "A"
    elif s >= 80:
        letter = "B"
    elif s >= 70:
        letter = "C"
    elif s >= 60:
        letter = "D"
    else:
        letter = "F"
    if s >= 60:
        print(letter, "pass")
    else:
        print(letter, "fail")
