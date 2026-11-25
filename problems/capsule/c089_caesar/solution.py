line = input()
k = int(input())
for ch in line:
    if ch.islower():
        print(chr((ord(ch) - ord("a") + k) % 26 + ord("a")), end="")
    elif ch.isupper():
        print(chr((ord(ch) - ord("A") + k) % 26 + ord("A")), end="")
    else:
        print(ch, end="")
print()
