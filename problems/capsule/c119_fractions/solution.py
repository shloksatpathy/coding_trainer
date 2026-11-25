from dataclasses import dataclass


@dataclass
class Fraction:
    num: int
    den: int


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def add(f, g):
    num = f.num * g.den + g.num * f.den
    den = f.den * g.den
    k = gcd(num, den)
    return Fraction(num // k, den // k)


def parse(text):
    a, b = text.split("/")
    return Fraction(int(a), int(b))


x, y = input().split()
s = add(parse(x), parse(y))
print(f"{s.num}/{s.den}")
