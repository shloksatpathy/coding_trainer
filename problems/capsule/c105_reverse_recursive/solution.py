def back(w, i):
    if i == len(w):
        return
    back(w, i + 1)
    print(w[i], end="")


w = input()
back(w, 0)
print()
