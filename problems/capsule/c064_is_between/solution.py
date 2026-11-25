def is_between(x, lo, hi):
    return lo <= x and x <= hi


lo, hi = map(int, input().split())
n = int(input())
for w in input().split():
    if is_between(int(w), lo, hi):
        print("yes")
    else:
        print("no")
