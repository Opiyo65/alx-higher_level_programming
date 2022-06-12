#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number == 0:
    if number < 0:
        print( f"{number} zero")
    else:
        print(f"{number} negative")
else:
    print(f"{number} positive")
