import time

thingsPerSecond = 1
things = 0

while True:
    things += thingsPerSecond
    print(things)

    time.sleep(1)