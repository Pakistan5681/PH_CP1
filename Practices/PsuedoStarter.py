import turtle as t

t.tracer(0, 0)
t.speed(1000)

def draw_branch(length):
    if length > 5:
        for i in range(3):
            t.forward(length)
            draw_branch(length/3)
            t.back(length)
            t.back(60)

t.speed(0)
t.color("#80C2D8")
t.penup()
t.teleport(0, 0)
t.pendown()

def draw_snowflake():
    for i in range(6):
        draw_branch(100)
        t.left(60)

draw_snowflake()
t.update()
t.mainloop()