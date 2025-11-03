import turtle as t
from random import randint, choice

gridSize = 6
gridSpaces = [] # open/closed list is layed out top bottom left right
spaceSize = 50

t.speed(0)

def randomList():
    outList = []
    options = ["open", "closed", "open"]

    while outList == ["closed", "closed", "closed", "closed"] or outList == []:
        outList = []

        for i in range(4):
            outList.append(choice(options))

    return outList

for x in range(gridSize):
    for y in range(gridSize):
        gridSpaces.append([[x * 50, y * 50], randomList()])

def drawLine(startPos, distance, rotation):
    t.teleport(startPos[0], startPos[1])
    t.left(rotation)
    t.forward(distance)
    t.right(rotation)

print(gridSpaces)

def drawMaze(gridSpaces, spaceSize, gridSize):
    drawLine([-(spaceSize / 2), -(spaceSize / 2)], spaceSize * gridSize, 0)
    drawLine([-(spaceSize / 2), (spaceSize * gridSize) - (spaceSize / 2)], spaceSize * gridSize, 0)
    drawLine([-(spaceSize / 2), -(spaceSize / 2)], (spaceSize * (gridSize - 1)), 90)
    drawLine([-(spaceSize / 2), -(spaceSize / 2)], (spaceSize * (gridSize - 1)), 90)

    for i in gridSpaces:
        x = i[0][0]
        y = i[0][1]

        if i[1][0] == "closed":
            drawLine([x - (spaceSize / 2), y + (spaceSize / 2)], spaceSize, 0)
        if i[1][1] == "closed":
            drawLine([x - (spaceSize / 2), y - (spaceSize / 2)], spaceSize, 0)
        if i[1][2] == "closed":
            drawLine([x - (spaceSize / 2), y + (spaceSize / 2)], spaceSize, 270)
        if i[1][2] == "closed":
            drawLine([x + (spaceSize / 2), y + (spaceSize / 2)], spaceSize, 270)

drawMaze(gridSpaces, spaceSize, gridSize)

t.mainloop()