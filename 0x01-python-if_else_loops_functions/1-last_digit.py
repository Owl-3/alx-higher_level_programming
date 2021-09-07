#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    num = number * -1
    num = num % 10
    num = num * -1
else:print("Last digit of {}".format(number), end=' ')
if num > 5:
    print("is {} and is greater than 5".format(num))
elif num == 0: 
