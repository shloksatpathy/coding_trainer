n = int(input())
a = list(map(int, input().split()))
jumps = reach_end = farthest = 0
for i in range(n - 1):
    if i > farthest:
        break
    farthest = max(farthest, i + a[i])
    if i == reach_end:
        jumps += 1
        reach_end = farthest
print(jumps if farthest >= n - 1 or n == 1 else -1)
