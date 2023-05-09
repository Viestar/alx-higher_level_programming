#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_two = (str(number)[-1])
number_two = int(number_two)
if number_two > 5:
    print(f"Last digit of {number} is {number_two} and is greater than 5 ")
elif number == 0:
    print(f"Last digit of {number} is {number_two} and is Zero")
elif number < 6 and not 0:
    print(
        f"Last digit of {number} is {number_two} and is less than 6 and not 0")
