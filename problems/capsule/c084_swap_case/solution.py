line = input()
for ch in line:
    if ch.isupper():
        print(ch.lower(), end="")
    elif ch.islower():
        print(ch.upper(), end="")
    else:
        print(ch, end="")
print()
