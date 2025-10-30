import pygame as py

py.init()
screen = py.display.set_mode((1280, 720))
clock = py.time.Clock()
running = True

red = (255, 0, 0)

cameraPos = [0, 0, -10]
cameraRotation = [0, 0, 0]

class Vertex:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Face:
    def __init__(self, vertOne, vertTwo, vertThree, color):
        self.vertOne = vertOne
        self.vertTwo = vertTwo
        self.vertThree = vertThree
        self.color = color

def drawFace(face, screen):
    vert1 = [face.vertOne.x, face.vertOne.y]
    vert2 = [face.vertTwo.x, face.vertTwo.y]
    vert3 = [face.vertThree.x, face.vertThree.y]

    py.draw.polygon(screen, face.color, [vert1, vert2, vert3])

def rotateVertex(vertex, centerPoint):
    relativeVertex = [vertex.x - centerPoint.x, vertex.y - centerPoint.y, vertex.z - centerPoint.z]

vert1 = Vertex(0, 0, 0)
vert2 = Vertex(2, 0, 0)
vert3 = Vertex(1, 2, 0)

face =  Face(vert1, vert2, vert3, red)

while running:
    screen.fill("purple")

    drawFace(face, screen)

    py.display.flip()



