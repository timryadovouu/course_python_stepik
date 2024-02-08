import random

counter = 0
for _ in range(100000):
    x = random.uniform(0.0, 1.0)
    y = random.uniform(0.0, 1.0)
    if x ** 2 + y ** 2 <= 1:
        counter += 1
print(4 * counter / 100000)
