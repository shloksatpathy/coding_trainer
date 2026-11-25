n = int(input())
words = input().split()
lo = int(words[0])
hi = int(words[0])
for w in words:
    x = int(w)
    if x < lo:
        lo = x
    if x > hi:
        hi = x
print(f"min: {lo}")
print(f"max: {hi}")
