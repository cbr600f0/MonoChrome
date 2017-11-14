import pygame
from pygame.locals import *

#Starts the game by initializing pygame
pygame.init()
# Sets to screen size to a specified size and makes the screen fullscreen
screen = pygame.display.set_mode((1920, 1080), FULLSCREEN)
# A bool wich says if the game is running or not (if this bool becomes False the whole game will close)
gameIsRunning = True
# Gets a sort of timer from pygame (you can use clock to change the FPS with clock.tick for instance)
clock = pygame.time.Clock()

# The gameloop
while gameIsRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:# If the event QUIT is raised close the game
            gameIsRunning = False

    # This is a list, all of the keys that are pressed during this frame are added in this list
    keysPressed = pygame.key.get_pressed()

    # If a key is pressed down AND that key is ESCAPE make gameIsRunning false so that the game will close
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        gameIsRunning = False

    # Fills the screen with the color green
    screen.fill((0, 0, 0))

    # Updates the screen (this method draws the screen)
    pygame.display.flip()

    # How many frames must there be made per second (increase the number to get more FPS)
    clock.tick(60)