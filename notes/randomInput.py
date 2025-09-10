import random
import time

while True:
    print(random.random())
    print(random.randint(-1000, 1000))

    time.sleep(1)

    name = input("WHAT BE THINE NAME: \n").strip().title()
