import sys, pygame, math, random, SceneManager
from pygame.locals import *
from BubbleShooter.Methods.ImageRotateTowardsMouse import ImageRotateTowardsMouse
from BubbleShooter.Methods.ImageCirculateAroundPoint import ImageCirculateAroundPoint
from BubbleShooter.Methods.LightShooter import LightShooter
class BubbleShooterScene(SceneManager.Scene):
    def __init__(self):
        super(BubbleShooterScene, self).__init__()
        pygame.init()
        # shows the mouse
        pygame.mouse.set_visible(True)
        # Loads in the image and changes their size where needed
        self.backgroundImage = pygame.image.load('BubbleShooter\Images\BackgroundDiscoGrid.png').convert_alpha()
        self.backgroundImage = pygame.transform.scale(self.backgroundImage, (1600, 900))
        self.backgroundImageRect = self.backgroundImage.get_rect()
        self.enemyImage = 'BubbleShooter\Images\enemy1.png'
        self.DiscoBallImage = 'BubbleShooter\Images\Player.png'
        self.DiscoBallImageWidth = 100
        self.DiscoBallImageHeight = 100
        # Creates the player and their
        self.Player = {}
        self.Player['xStartPos'] = ((self.backgroundImageRect.width / 2) + self.DiscoBallImageWidth / 2)
        self.Player['yStartPos'] = ((self.backgroundImageRect.height / 2.5) + self.DiscoBallImageHeight / 2)
        self.Player['Image'] = self.enemyImage
        self.Player['xPos'] = self.Player['xStartPos']
        self.Player['yPos'] = self.Player['yStartPos']
        self.Player['Width'] = 40
        self.Player['height'] = 40
        self.Player['shoot'] = False

    def render(self, screen):
        screen.blit(self.backgroundImage, self.backgroundImageRect)
        ImageRotateTowardsMouse(self.DiscoBallImage, screen, self.DiscoBallImageWidth, self.DiscoBallImageHeight, (self.backgroundImageRect.width / 2), (self.backgroundImageRect.height / 2.5))
        ImageCirculateAroundPoint(self.enemyImage, screen, self.Player['Width'], self.Player['height'], self.Player['xPos'], self.Player['yPos'])

    def handle_events(self, events):
        if not self.Player['shoot']:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.Player['shoot'] = True

    def update(self, deltaTime):
        self.mousePositionX, self.mousePositionY = pygame.mouse.get_pos()
        if self.Player['shoot'] == True:
            self.Player['xPos'] += 3
            if self.Player['xPos'] >= 1600:
                self.Player['xPos'] = ((self.backgroundImageRect.width / 2) + self.Player['xStartPos'])
                self.Player['shoot'] = False
        else:
            if self.backgroundImageRect.width / 2 > self.mousePositionX:
                self.Player['xPos'] = self.Player['xStartPos'] - self.DiscoBallImageWidth
            else:
                self.Player['xPos'] = self.Player['xStartPos']
            if self.backgroundImageRect.height / 2.5 > self.mousePositionY:
                self.Player['yPos'] = self.Player['yStartPos'] - self.DiscoBallImageHeight
            else:
                self.Player['yPos'] = self.Player['yStartPos']
