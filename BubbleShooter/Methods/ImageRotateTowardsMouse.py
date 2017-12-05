import sys, pygame, math
from pygame.locals import *

class ImageRotateTowardsMouse():
    def __init__(self, rotatingImage, screen, width = 0, height = 0, posX = 0, posY = 0):
        """
        :param rotatingImage holds the path towards the images you want to rotate:
        :param screen is needed to draw the image to the screen:
        :param width, optional, resizes the width you want the image to have:
        :param height, optional, resizes the height you want the image to have:
        :param posX, optional, sets the x-as of the center of the image (Note: 0 will make the CENTER of the x-as 0):
        :param posY, optional, sets the y-as of the center of the image (Note: 0 will make the CENTER of the y-as 0):
        """
        rotatingImage = pygame.image.load(rotatingImage).convert_alpha()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                rotatingImage = pygame.transform.scale(rotatingImage, (width, height))
                pos = pygame.mouse.get_pos()
                angle = 360 - math.atan2(pos[1] - posY, pos[0] - posX) * 180 / math.pi
                rotimage = pygame.transform.rotate(rotatingImage, angle)
                rect = rotimage.get_rect(center=(posX, posY))
                screen.blit(rotimage, rect)
                pygame.display.update()