import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1920, 1080), FULLSCREEN)
gameIsRunning = True

clock = pygame.time.Clock()

while gameIsRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameIsRunning = False

    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        gameIsRunning = False

    keysPressed = pygame.key.get_pressed()

    screen.fill((0, 0, 0))

    pygame.display.flip()
    clock.tick(60)