import sys, pygame, math
from pygame.locals import *

class ImageCirculateAroundPoint():
    def __init__(self, circulatingImage, screen, width=0, height=0, posX=0, posY=0):
        circulatingImage = pygame.image.load(circulatingImage).convert_alpha()
        circulatingImage = pygame.transform.scale(circulatingImage, (width, height))
        pos = pygame.mouse.get_pos()
        angle = 360 - math.atan2(pos[1] - posY, pos[0] - posX) * 180 / math.pi
        rotimage = pygame.transform.rotate(circulatingImage, angle)
        rect = rotimage.get_rect(center=(posX, posY))
        screen.blit(rotimage, rect)