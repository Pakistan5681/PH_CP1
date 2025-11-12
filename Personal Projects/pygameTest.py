import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode((400, 300))
surface = pygame.Surface((400, 300))
clock = pygame.time.Clock()

t = 0
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    pixels = pygame.surfarray.pixels3d(surface)
    w, h = surface.get_size()
    
    # Make arrays match the surface shape (width, height)
    x = np.arange(w).reshape(w, 1)  # shape (400, 1)
    y = np.arange(h).reshape(1, h)  # shape (1, 300)

    pixels[:, :, 0] = (np.sin((x + t) / 10) * 127 + 128).astype(np.uint8)
    pixels[:, :, 1] = (np.sin((y + t) / 20) * 127 + 128).astype(np.uint8)
    pixels[:, :, 2] = (np.sin((x + y + t) / 30) * 127 + 128).astype(np.uint8)

    del pixels  # release surface lock
    screen.blit(surface, (0, 0))
    pygame.display.flip()
    t += 1
    clock.tick(60)
