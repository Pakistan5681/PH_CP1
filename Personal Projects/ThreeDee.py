import pygame as py

py.init()
screen = py.display.set_mode((1280, 720))
clock = py.time.Clock()
running = True

red = (255, 0, 0)

tri = [[0, 0, 0], [0, 2, 0], [1, 1, 0], red, ]


while True:
    py.draw.polygon(screen, )