line = input()
count = 0
for ch in line:
    if ch.lower() in "aeiou":
        count += 1
print(count)
