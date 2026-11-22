a, b = input().split()
count = [0] * 26
for ch in a:
    count[ord(ch) - 97] += 1
for ch in b:
    count[ord(ch) - 97] -= 1
print("Yes" if all(x == 0 for x in count) else "No")
