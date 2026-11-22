from bisect import bisect_left
n = int(input())
tails = []
for x in map(int, input().split()):
    i = bisect_left(tails, x)
    if i == len(tails):
        tails.append(x)
    else:
        tails[i] = x
print(len(tails))
