def area(w, h):
    return w * h


def draw_box(w, h):
    for r in range(h):
        for col in range(w):
            print("*", end="")
        print()


w, h = map(int, input().split())
print(f"area: {area(w, h)}")
draw_box(w, h)
