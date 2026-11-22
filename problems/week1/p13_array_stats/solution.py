n = int(input())
a = list(map(int, input().split()))
print(min(a), max(a), sum(a), f"{sum(a) / n:.2f}")
