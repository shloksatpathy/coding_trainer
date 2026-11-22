import random

R = random.Random(51)
print('100000 5000000')
print(*(R.randint(1, 1000) for _ in range(100000)))
