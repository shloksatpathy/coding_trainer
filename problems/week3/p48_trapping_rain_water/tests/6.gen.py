import random

R = random.Random(48)
print('100000')
print(*(R.randint(0, 10000) for _ in range(100000)))
