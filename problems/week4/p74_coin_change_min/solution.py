k, amount = map(int, input().split())
coins = list(map(int, input().split()))
INF = amount + 1
best = [0] + [INF] * amount
for x in range(1, amount + 1):
    for c in coins:
        if c <= x and best[x - c] + 1 < best[x]:
            best[x] = best[x - c] + 1
print(best[amount] if best[amount] < INF else -1)
