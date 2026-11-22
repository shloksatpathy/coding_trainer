import random

R = random.Random(30)
print('100000 50000')
print(*(R.randint(-1000000000, 1000000000) for _ in range(100000)))
