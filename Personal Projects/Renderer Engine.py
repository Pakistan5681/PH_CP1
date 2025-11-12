import pygame as py
import math as m
import numpy as np

py.init()
screen = py.display.set_mode((1280 * 1.5, 720 * 1.5))
clock = py.time.Clock()
running = True

fov = np.radians(60)
aspect = 16/9
near, far = 0.1, 100
f = 1 / np.tan(fov / 2)

pMatrix = np.array([
    [f/aspect, 0, 0, 0],
    [0, f, 0, 0],
    [0, 0, (far+near)/(near-far), (2*far*near)/(near-far)],
    [0, 0, -1, 0]
])

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
orange  = (255, 102, 0)
purple = (255, 0, 255)

cameraPos = [0, 0, 0]
cameraRotation = [0, 0, 0]
fov = 30

defaultRenderDistance = 10 # The distance at which an object will be rendered at set size
distanceShrink = 2

class Vertex:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def to_array(self):
        return np.array([self.x, self.y, self.z, 1.0])

    def project(self, projection_matrix, width, height):
        clip = projection_matrix @ self.to_array()

        ndc = clip[:3] / clip[3]

        x_screen = (ndc[0] + 1) * 0.5 * width
        y_screen = (1 - ndc[1]) * 0.5 * height
        z_screen = ndc[2]

        print(np.array([x_screen, y_screen]))

        return np.array([x_screen, y_screen])

class Face:
    def __init__(self, vertOne, vertTwo, vertThree, color):
        self.vertOne = vertOne
        self.vertTwo = vertTwo
        self.vertThree = vertThree
        self.color = color

    def draw(self, projectMatrix, screen):
        pointOne = self.vertOne.project(projectMatrix, screen.get_width(), screen.get_height())
        pointTwo = self.vertTwo.project(projectMatrix, screen.get_width(), screen.get_height())
        pointThree = self.vertThree.project(projectMatrix, screen.get_width(), screen.get_height())

        a = (pointOne[0], pointOne[1])
        b = (pointTwo[0], pointTwo[1])
        c = (pointThree[0], pointThree[1])

        pixels = py.surfarray.pixels3d(screen)

        min_x = int(max(min(a[0], b[0], c[0]), 0))
        max_x = int(min(max(a[0], b[0], c[0]), screen.get_width()))
        min_y = int(max(min(a[1], b[1], c[1]), 0))
        max_y = int(min(max(a[1], b[1], c[1]), screen.get_height()))

        x, y = np.meshgrid(np.arange(min_x, max_x), np.arange(min_y, max_y))

        x1, y1 = a
        x2, y2 = b
        x3, y3 = c

        den = ( (y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3) )
        α = ((y2 - y3)*(x - x3) + (x3 - x2)*(y - y3)) / den
        β = ((y3 - y1)*(x - x3) + (x1 - x3)*(y - y3)) / den
        γ = 1 - α - β

        mask = (α >= 0) & (β >= 0) & (γ >= 0)

        pixels[min_x:max_x, min_y:max_y][mask.T] = self.color

        del pixels

class Shape:
    def __init__(self, faces):
        self.faces = faces

    def move(self, moveVertex):
        for i in self.faces:
            moveFace(i, moveVertex)

    def rotate(self, rotationType, centerVertex, angle):
        for i in self.faces:
            rotateFace(i, rotationType, centerVertex, angle)
    
    def draw(self, screen, projectMatrix):
        zPositions = []
        zConnections = {}
        for i in self.faces:
            zAverage = (i.vertOne.z + i.vertTwo.z + i.vertThree.z) / 3
            zConnections[zAverage] = i
            zPositions.append(zAverage)

        zPositions.sort()

        for i in zPositions:
            zConnections[i].draw(projectMatrix, screen)
            

def drawNoProjection(vertex):
    x = vertex.x
    y = vertex.y

    return [x,y]

def drawFace(face, screen, projectMatrix):
    vert1 = face.vertOne.project(projectMatrix, screen.get_width(), screen.get_height())
    vert2 = face.vertTwo.project(projectMatrix, screen.get_width(), screen.get_height())
    vert3 = face.vertThree.project(projectMatrix, screen.get_width(), screen.get_height())

    py.draw.polygon(screen, face.color, [vert1, vert2, vert3])

def moveVertex(vertex, movementVertex):
    vertex.x += movementVertex.x
    vertex.y += movementVertex.y
    vertex.z += movementVertex.z

    return(Vertex(vertex.x, vertex.y, vertex.z))

def moveFace(face, movementVertex):
    face.vertOne = moveVertex(face.vertOne, movementVertex)
    face.vertTwo = moveVertex(face.vertTwo, movementVertex)
    face.vertThree = moveVertex(face.vertThree, movementVertex)

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

vert1 = Vertex(0, 0, -50)
vert2 = Vertex(10, -10, -40)
vert3 = Vertex(-10, -10, -40)
vert4 = Vertex(0, -10, -60)

face1 = Face(vert1, vert2, vert3, red)
face2 = Face(vert1, vert2, vert4, blue)
face3 = Face(vert1, vert3, vert4, green)
face4 = Face(vert2, vert3, vert4, yellow)

pyramid = Shape([face1, face2, face3, face4])

while running:
    screen.fill("black")
    clock.tick(60)

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    pyramid.rotate("y", Vertex(0, -5, -50), 1)
    pyramid.rotate("x", Vertex(0, -5, -50), 1)
    pyramid.draw(screen, pMatrix)

    py.display.flip()
