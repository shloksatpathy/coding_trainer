import random

R = random.Random(46)
print('1500')
print(*(R.randint(-300, 300) for _ in range(1500)))
