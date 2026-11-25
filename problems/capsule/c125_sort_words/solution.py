n = int(input())
words = input().split()
words.sort(key=lambda w: (len(w), w))
for w in words:
    print(w)
