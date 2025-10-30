import pygame as py
import math as m

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

def rotateVertex(vertex, centerPoint, rotationType, angle):
    angle = m.radians(angle)
    relativeVertex = [vertex.x - centerPoint.x, vertex.y - centerPoint.y, vertex.z - centerPoint.z]
    newVertexLocal = [0, 0, 0]

    if rotationType == "x":
        newVertexLocal[0] = relativeVertex[0]
        newVertexLocal[1] = (relativeVertex[1] * m.cos(angle)) - (relativeVertex[2] * m.sin(angle))
        newVertexLocal[2] = (relativeVertex[1] * m.sin(angle)) + (relativeVertex[2] * m.cos(angle))
    elif rotationType == "y":
        newVertexLocal[1] = relativeVertex[1]
        newVertexLocal[0] = (relativeVertex[0] * m.cos(angle)) + (relativeVertex[2] * m.sin(angle))
        newVertexLocal[2] = (-relativeVertex[0] * m.sin(angle)) + (relativeVertex[2] * m.cos(angle))
    elif rotationType == "z":
        newVertexLocal[2] = relativeVertex[1]
        newVertexLocal[0] = (relativeVertex[0] * m.cos(angle)) - (relativeVertex[1] * m.sin(angle))
        newVertexLocal[1] = (relativeVertex[0] * m.sin(angle)) + (relativeVertex[1] * m.cos(angle))
    else:
        print(f"{rotationType} is not a valid rotation")
    
    newVertexLocal[0] += centerPoint.x
    newVertexLocal[1] += centerPoint.y
    newVertexLocal[2] += centerPoint.z

    print(newVertexLocal)
    return Vertex(newVertexLocal[0], newVertexLocal[1], newVertexLocal[2])

def rotateFace(face, rotationType, centerPoint, angle):
    face.vertOne = rotateVertex(face.vertOne, centerPoint, rotationType, angle)
    face.vertTwo = rotateVertex(face.vertTwo, centerPoint, rotationType, angle)
    face.vertThree = rotateVertex(face.vertThree, centerPoint, rotationType, angle)

    return face

vert1 = Vertex(0, 0, 0)
vert2 = Vertex(200, 0, 0)
vert3 = Vertex(100, 200, 0)

face =  Face(vert1, vert2, vert3, red)

while running:
    screen.fill("purple")
    clock.tick(60)

    drawFace(face, screen)
    face = rotateFace(face, "z", Vertex(100, 200, 0), 1)
    face = rotateFace(face, "x", Vertex(100, 200, 0), 1)
    py.display.flip()



