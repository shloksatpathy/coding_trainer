s = input()
count = [0] * 26
for ch in s:
    count[ord(ch) - 97] += 1
print(next((i for i, ch in enumerate(s) if count[ord(ch) - 97] == 1), -1))
