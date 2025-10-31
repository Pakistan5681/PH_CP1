import pygame as py
import math as m

py.init()
screen = py.display.set_mode((1280, 720))
clock = py.time.Clock()
running = True

red = (255, 0, 0)

cameraPos = [0, 0, -10]
cameraRotation = [0, 0, 0]

defaultRenderDistance = 10 # The distance at which an object will be rendered at set size
distanceShrink = 2

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

def project(vertex, cameraPos, screen):
    distance = vertex.z - cameraPos[2]
    if vertex.z == 0: vertex.z = 1  # prevent divide-by-zero

    x = (vertex.x * distance) / vertex.z
    y = (vertex.y * distance) / vertex.z

    print(f"x: {x}, y: {y}")
    return [x, y]

def drawFace(face, screen, cameraPosition, pyScreen):
    vert1 = project(face.vertOne, cameraPosition, pyScreen)
    vert2 = project(face.vertTwo, cameraPosition, pyScreen)
    vert3 = project(face.vertThree, cameraPosition, pyScreen)

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

    return Vertex(newVertexLocal[0], newVertexLocal[1], newVertexLocal[2])

def rotateFace(face, rotationType, centerPoint, angle):
    face.vertOne = rotateVertex(face.vertOne, centerPoint, rotationType, angle)
    face.vertTwo = rotateVertex(face.vertTwo, centerPoint, rotationType, angle)
    face.vertThree = rotateVertex(face.vertThree, centerPoint, rotationType, angle)

    return face

vert1 = Vertex(500, 500, 0)
vert2 = Vertex(700, 500, 0)
vert3 = Vertex(600, 700, 0)

face = Face(vert1, vert2, vert3, red)

while running:
    screen.fill("purple")
    clock.tick(60)

    face.vertOne.x += 1

    drawFace(face, screen, cameraPos, screen)
    py.display.flip()



