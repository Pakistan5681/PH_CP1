import turtle as t
from random import randint, choice
from time import sleep

gridSize = 5
gridRows = []
gridCollumns = []
spaceSize = 80

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
    drawLineVertical(spaceSize * gridSize, 0, (spaceSize * (gridSize - 1)))
    drawLineVerticalEdgeCase(0, spaceSize * gridSize, (spaceSize * (gridSize - 1)))

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

            drawLineVertical(i * spaceSize, j * spaceSize, spaceSize)

def checkSolvable(rows, collumns, size, gridCount):
    mazeCheckers = [[0, 0]]
    indent = size / 2

    visitedSpaces = []

    solvable = False

    while bool(mazeCheckers):
        print(f"length: {len(mazeCheckers)}")
        for i in mazeCheckers:
            i[0].shape("circle")
            i[0].shapesize(0.5, 0.5, 0)

            if i[1] == [gridSize - 1, gridSize - 1]:
                solvable = True
                print("solved")
                return True

            i[0].teleport((i[1][0] * size) + indent, (i[1][1] * size) + indent)
                
            i[0].speed(10)
            if (i[1][1] + 1) * size < size * gridCount:
                if rows[i[1][1] + 1][i[1][0]] == "open" and not [i[1][0], i[1][1] + 1] in visitedSpaces: # checks if no line above
                    print("open") 
                    mazeCheckers.append([i[1][0], i[1][1] + 1])
                    visitedSpaces.append([i[1][0], i[1][1]])
                else:
                    print("closed")

            if rows[i[1][1] - 1][i[1][0]] == "open" and (i[1][1] - 1) * size > 0 and not [i[1][0], i[1][1] - 1] in visitedSpaces: # checks if no line below
                print("open") 
                mazeCheckers.append([i[1][0], i[1][1] - 1])
                visitedSpaces.append([i[1][0], i[1][1]])
            else:
                print("closed")

            if (i[1][0] + 1) * size < size * gridCount:
                if collumns[i[1][0] + 1][i[1][1]] == "open" and not [i[1][0] + 1, i[1][1]] in visitedSpaces: # checks if no line to right
                    print("open") 
                    mazeCheckers.append([i[1][0] + 1, i[1][1]])
                    visitedSpaces.append([i[1][0], i[1][1]])
                else:
                    print("closed")

            if collumns[i[1][0]][i[1][1]] == "open" and (i[1][0] - 1) * size > 0 and not [i[1][0] - 1, i[1][1]] in visitedSpaces: # checks if no line to left
                print("open") 
                mazeCheckers.append([i[1][0] - 1, i[1][1]])
                visitedSpaces.append([i[1][0], i[1][1]])
            else:
                print("closed")

            mazeCheckers.remove(i)  

    return solvable
            

drawMaze(gridRows, gridCollumns, spaceSize, gridSize)

while checkSolvable(gridRows, gridCollumns, spaceSize, gridSize) == False:
    t.clear()
    gridRows = []
    gridCollumns = []
    for x in range(gridSize):      
        gridRows.append(randomList(gridSize))
        gridCollumns.append(randomList(gridSize))
    drawMaze(gridRows, gridCollumns, spaceSize, gridSize)

t.mainloop()