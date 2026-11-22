import random

R = random.Random(63)
print('20000')
print(*(R.randint(-1000000, 1000000) for _ in range(20000)))
