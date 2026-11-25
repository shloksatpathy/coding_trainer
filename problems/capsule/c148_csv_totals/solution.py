n = int(input())
totals = {}
overall = 0
for i in range(n):
    name, dept, amount = input().split(",")
    totals[dept] = totals.get(dept, 0) + int(amount)
    overall += int(amount)
for dept in totals:
    print(f"{dept}: {totals[dept]}")
print(f"overall: {overall}")
