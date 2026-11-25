line = input()
last = {}
start = 0
best = 0
for i in range(len(line)):
    ch = line[i]
    if ch in last and last[ch] >= start:
        start = last[ch] + 1
    last[ch] = i
    if i - start + 1 > best:
        best = i - start + 1
print(best)
