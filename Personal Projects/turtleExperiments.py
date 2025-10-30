import turtle as t
import random as r

size = 150
circleSides = 3
iterations = 0

colors = ["blue", "red", "yellow", "green", "purple", "orange"]

jeff = t.Turtle()
jeff_two = t.Turtle()
jeff_three = t.Turtle()
jeff_four = t.Turtle()

jeff.speed(5681 * 20)
jeff.penup()
jeff.goto(0, 0)
jeff.pendown()

jeff_two.speed(5681 * 20)
jeff_two.penup()
jeff_two.goto(0, 0)
jeff_two.pendown()

for i in range(100):
    t.color(r.choice(colors))
    t.pensize(3)

    while iterations < circleSides:
        jeff.forward(size)
        jeff.right(360 / circleSides)
        jeff_two.forward(size)
        jeff_two.left(360/circleSides)
        iterations += 1

    circleSides += 1
   
    iterations = 0

t.mainloop()