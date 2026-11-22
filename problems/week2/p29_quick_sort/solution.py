import sys
sys.setrecursionlimit(10000)
n = int(input())
a = list(map(int, input().split()))
calls = []

def partition(lo, hi):
    pivot, i = a[hi], lo - 1
    for j in range(lo, hi):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[hi] = a[hi], a[i + 1]
    calls.append(list(a) if not calls else None)
    return i + 1

def quick(lo, hi):
    if lo < hi:
        p = partition(lo, hi)
        quick(lo, p - 1)
        quick(p + 1, hi)

quick(0, n - 1)
print(*(calls[0] if calls else a))
print(*a)
print(f"partitions={len(calls)}")
