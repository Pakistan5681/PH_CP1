class gridCell():
    def __init__(self, position, ):
        pass

connections = [] #example [[[0, 0], [0, 1]], [[0, 0], [1, 0]]]
cellWidth = 10

for x in range(cellWidth):
    for y in range(cellWidth):
        grid.append([[x, y], ["closed", "closed", "closed", "closed"]])

print(grid)

def openCell():
    openDirection = "up"

    while True:
        if openDirection == "up":
            if grid