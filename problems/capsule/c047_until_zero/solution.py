count = 0
total = 0
while True:
    x = int(input())
    if x == 0:
        break
    count += 1
    total += x
print(f"count: {count}")
print(f"sum: {total}")
