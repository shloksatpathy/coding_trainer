words = input().split()
for i in range(len(words)):
    if i > 0:
        print("-", end="")
    print(words[i], end="")
print()
