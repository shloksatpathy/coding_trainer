n = int(input())
h = list(map(int, input().split()))
lo, hi = 0, n - 1
left_max = right_max = water = 0
while lo < hi:
    if h[lo] < h[hi]:
        left_max = max(left_max, h[lo])
        water += left_max - h[lo]
        lo += 1
    else:
        right_max = max(right_max, h[hi])
        water += right_max - h[hi]
        hi -= 1
print(water)
