import random

R = random.Random(61)
print('50000')
print(*(R.randint(-1000000000, 1000000000) for _ in range(50000)))
