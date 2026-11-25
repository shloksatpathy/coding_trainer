from dataclasses import dataclass


@dataclass
class Student:
    name: str
    score: int


n = int(input())
students = []
for i in range(n):
    name, score = input().split()
    students.append(Student(name, int(score)))
top = students[0]
total = 0
for s in students:
    total += s.score
    if s.score > top.score:
        top = s
print(f"top: {top.name} ({top.score})")
print(f"average: {total / n:.2f}")
print("above:", end="")
found = 0
for s in students:
    if s.score * n > total:
        print(f" {s.name}", end="")
        found += 1
if found == 0:
    print(" none", end="")
print()
