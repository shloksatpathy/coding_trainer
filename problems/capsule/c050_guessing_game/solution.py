secret, n = map(int, input().split())
found = False
for k in range(1, n + 1):
    g = int(input())
    if g < secret:
        print("too low")
    elif g > secret:
        print("too high")
    else:
        print(f"correct on guess {k}")
        found = True
        break
if not found:
    print(f"no luck, it was {secret}")
