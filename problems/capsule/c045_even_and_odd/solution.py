n = int(input())
words = input().split()
even = 0
odd = 0
for w in words:
    if int(w) % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"even: {even}")
print(f"odd: {odd}")
