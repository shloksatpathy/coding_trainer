from dataclasses import dataclass


@dataclass
class Report:
    name: str
    scores: list


words = input().split()
r = Report(words[0], [int(words[1]), int(words[2]), int(words[3])])
total = 0
best = r.scores[0]
for s in r.scores:
    total += s
    if s > best:
        best = s
print(f"{r.name}: total {total}, average {total / 3:.2f}, best {best}")
