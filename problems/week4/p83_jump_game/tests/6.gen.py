import random

R = random.Random(83)
print('100000')
print(*(R.randint(1, 50) for _ in range(100000)))
