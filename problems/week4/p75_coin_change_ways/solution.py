k, amount = map(int, input().split())
coins = list(map(int, input().split()))
ways = [1] + [0] * amount
for c in coins:
    for x in range(c, amount + 1):
        ways[x] += ways[x - c]
print(ways[amount])
