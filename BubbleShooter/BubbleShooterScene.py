import sys, pygame, math
from pygame.locals import *
from BubbleShooter.Methods.ImageRotateTowardsMouse import ImageRotateTowardsMouse
class BubbleShooterScene():
    def __init__(self):
        pygame.init()
        # Sets the screen resolution and creates a variable to set other images' position
        screen = pygame.display.set_mode((1600, 900))
        # shows the mouse
        pygame.mouse.set_visible(True)
        # loads the background and changes it to fit the screen
        backgroundImage = pygame.image.load('BubbleShooter\Images\BackgroundDiscoGrid.png').convert_alpha()
        backgroundImage = pygame.transform.scale(backgroundImage, (1600, 900))
        backgroundImageRect = backgroundImage.get_rect()
        screen.blit(backgroundImage, backgroundImageRect)
        # Calls the method that makes an image rotatable
        DiscoBallImage = 'BubbleShooter\Images\Player.png'
        ImageRotateTowardsMouse(DiscoBallImage, screen, 100, 100, 800, 400)

    def render(self, screen):
        pass

    def handle_events(self, events):
        pass

    def update(self, deltaTime):
        pass