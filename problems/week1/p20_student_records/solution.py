def grade(m):
    if m >= 90:
        return "A"
    if m >= 75:
        return "B"
    if m >= 60:
        return "C"
    return "F"

n = int(input())
students = []
for _ in range(n):
    name, roll, marks = input().split()
    students.append((name, int(roll), int(marks)))
for name, roll, marks in sorted(students, key=lambda s: (-s[2], s[1])):
    print(name, roll, marks, grade(marks))
