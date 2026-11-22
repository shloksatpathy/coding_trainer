import sys
sys.setrecursionlimit(10000)

def sort(a):
    if len(a) <= 1:
        return a, 0
    mid = len(a) // 2
    left, x = sort(a[:mid])
    right, y = sort(a[mid:])
    merged, inv, i, j = [], x + y, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv += len(left) - i
            j += 1
    merged += left[i:] + right[j:]
    return merged, inv

n = int(input())
a, inv = sort(list(map(int, input().split())))
print(*a)
print(f"inversions={inv}")
