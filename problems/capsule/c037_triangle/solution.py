a, b, c = map(int, input().split())
if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("not a triangle")
elif a == b and b == c:
    print("equilateral")
elif a == b or b == c or a == c:
    print("isosceles")
else:
    print("scalene")
