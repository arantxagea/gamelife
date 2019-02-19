import sys
import random

import pygame
from pygame.locals import QUIT


black = (0, 0, 0)
white = (255, 255, 255)


def is_alive(x, y):
    return random.randint(1, 10) % 2 == 0


if __name__ == '__main__':
    pygame.init()
    surface = pygame.display.set_mode((600, 400))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        for x in range(32):
            for y in range(32):
                alive = is_alive(x, y)
                color = white if alive else black
                rectangle = (x * 10, y * 10, 10, 10)
                pygame.draw.rect(surface, color, rectangle)

        pygame.display.update()
        pygame.time.delay(500)
