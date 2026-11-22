import random

R = random.Random(76)
print('100000')
print(*(R.randint(-1000000000, 1000000000) for _ in range(100000)))
