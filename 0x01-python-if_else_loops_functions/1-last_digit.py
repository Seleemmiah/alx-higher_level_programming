#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    last = -last
if last > 5:
    result = "greater than 5"
elif last == 0:
    result = "0"
else:
    result = "less than 6 and not 0"
print(f"Last digit o {number:d}", f"is {last:d} and is", result)
