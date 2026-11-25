def show(label, values):
    if len(values) == 0:
        print(f"{label}: none")
    else:
        print(f"{label}: " + " ".join(str(x) for x in sorted(values)))


first = input().split()
second = input().split()
a = set()
for w in first[1:]:
    a.add(int(w))
b = set()
for w in second[1:]:
    b.add(int(w))
show("union", a | b)
show("both", a & b)
show("only first", a - b)
