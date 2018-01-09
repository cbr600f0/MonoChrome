import sys, pygame, math
from pygame.locals import *

class ImageRotateTowardsMouse():
    def __init__(self, rotatingImage, screen, width=0, height=0, posX=0, posY=0):
        rotatingImage = pygame.image.load(rotatingImage).convert_alpha()
        rotatingImage = pygame.transform.scale(rotatingImage, (width, height))
        pos = pygame.mouse.get_pos()
        angle = 360 - math.atan2(pos[1] - posY, pos[0] - posX) * 180 / math.pi
        rotimage = pygame.transform.rotate(rotatingImage, angle)
        rect = rotimage.get_rect(center=(posX, posY))
        screen.blit(rotimage, rect)