from random import randint

numbers = []

for i in range(67):
    numbers.append(randint(-10000, 10000))

def divide(number):
    return number / 2

divided = list(map(divide, numbers))

for i, num in enumerate(numbers):
    print(f"{num} divided by 2 is {divided[i]}")