import pygame
import sys
from game import Game

pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
dark_blue = (44, 44, 127)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python tetris version 1")
clock = pygame.time.Clock()

game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                game.move_down()
            if event.key == pygame.K_UP:
                game.rotate()


    #Drawing
    screen.fill(dark_blue)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)

