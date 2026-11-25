from dataclasses import dataclass


@dataclass
class Time:
    h: int
    m: int


def to_minutes(t):
    return t.h * 60 + t.m


def parse(text):
    h, m = text.split(":")
    return Time(int(h), int(m))


a, b = input().split()
d = to_minutes(parse(b)) - to_minutes(parse(a))
print(f"{d // 60}:{d % 60:02d}")
