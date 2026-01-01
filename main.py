import pygame
import sys
from grid import Grid
from blocks import *


pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
dark_blue = (44, 44, 127)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python tetris version 1")
clock = pygame.time.Clock()

game_grid = Grid()
block = ZBlock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Drawing
    screen.fill(dark_blue)
    game_grid.draw(screen)
    block.draw(screen)

    pygame.display.update()
    clock.tick(60)

