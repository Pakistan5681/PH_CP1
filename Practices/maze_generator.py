import turtle as t
from random import randint, choice

gridSize = 10
gridRows = []
gridCollumns = []
spaceSize = 20

t.speed(0)

def randomList(gridSize):
    outList = []
    options = ["open", "closed"]

    for i in range(gridSize):
        outList.append(choice(options))

    return outList

for x in range(gridSize):
    gridRows.append(randomList(gridSize))
    gridCollumns.append(randomList(gridSize))

def drawLineHorizontal(x, y, distance):
    t.teleport(x, y)
    t.forward(distance)

def drawLineVertical(x, y, distance):
    t.teleport(x, y)
    t.left(90)
    t.forward(distance)
    t.right(90)

def drawLineVerticalEdgeCase(x, y, distance):
    t.teleport(x, y)
    t.left(270)
    t.forward(distance)
    t.right(270)

def drawMaze(rows, collumns, spaceSize, gridSize):
    drawLineHorizontal(0, 0, spaceSize * gridSize)
    drawLineHorizontal(0, (spaceSize * gridSize), spaceSize * gridSize)
    drawLineVertical(0, 0, (spaceSize * (gridSize - 1)))
    drawLineVerticalEdgeCase((spaceSize * gridSize), spaceSize * gridSize, (spaceSize * (gridSize - 1)))

    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if rows[i][j] == "open":
                t.penup()
            else:
                t.pendown()

            drawLineHorizontal(j * spaceSize, i * spaceSize, spaceSize)

    for i in range(len(collumns)):
        for j in range(len(collumns[i])):
            if collumns[i][j] == "open":
                t.penup()
            else:
                t.pendown()

            drawLineVertical(j * spaceSize, i * spaceSize, spaceSize)

def checkSolvable(rows, collumns):
    mazeCheckers = [[t.Turtle(), [0, 0]]]

    for i in mazeCheckers:
        i[0].shape("circle")
        i[0].teleport(i[1][0], i[1][1])

        if rows[i[1][0]][i[1][1]] == "open": # checks if no line above
            pass 
            



drawMaze(gridRows, gridCollumns, spaceSize, gridSize)

t.mainloop()