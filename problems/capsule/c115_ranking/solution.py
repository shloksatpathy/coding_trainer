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
students.sort(key=lambda s: (-s.score, s.name))
for i in range(n):
    print(f"{i + 1}. {students[i].name} {students[i].score}")
