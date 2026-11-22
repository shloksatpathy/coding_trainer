s = input()
last = {}
lo = best = 0
for i, ch in enumerate(s):
    if ch in last and last[ch] >= lo:
        lo = last[ch] + 1
    last[ch] = i
    best = max(best, i - lo + 1)
print(best)
