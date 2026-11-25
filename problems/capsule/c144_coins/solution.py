amount = int(input())
total = 0
for coin in [200, 100, 50, 20, 10, 5, 2, 1]:
    k = amount // coin
    if k > 0:
        print(f"{coin} x {k}")
        amount -= k * coin
        total += k
print(f"coins: {total}")
