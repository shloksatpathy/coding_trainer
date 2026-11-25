line = input()
count = [0] * 26
for ch in line.lower():
    if "a" <= ch <= "z":
        count[ord(ch) - ord("a")] += 1
letters = []
for i in range(26):
    if count[i] > 0:
        letters.append(i)
letters.sort(key=lambda i: (-count[i], i))
for i in letters:
    print(f"{chr(ord('a') + i)}: {count[i]}")
