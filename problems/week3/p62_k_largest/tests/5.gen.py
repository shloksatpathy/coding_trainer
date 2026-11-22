import random

R = random.Random(62)
print('100000 10')
print(*(R.randint(-1000000000, 1000000000) for _ in range(100000)))
