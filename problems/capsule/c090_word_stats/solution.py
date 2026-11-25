words = input().split()
longest = words[0]
shortest = words[0]
total = 0
for w in words:
    if len(w) > len(longest):
        longest = w
    if len(w) < len(shortest):
        shortest = w
    total += len(w)
print(f"words: {len(words)}")
print(f"longest: {longest}")
print(f"shortest: {shortest}")
print(f"average: {total / len(words):.2f}")
