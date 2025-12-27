import pygame
import sys


pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 700
dark_blue = (44, 44, 127)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python tetris version 1")
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Drawing
    screen.fill(dark_blue)
    pygame.display.update()
    clock.tick(60)

