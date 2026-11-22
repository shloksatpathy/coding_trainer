import random

R = random.Random(49)
print('200000 50000')
print(*(R.randint(-1000000, 1000000) for _ in range(200000)))
