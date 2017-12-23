import sys, pygame, math, random, SceneManager, Vector2
from pygame.locals import *
from BubbleShooter.Methods.ImageRotateTowardsMouse import ImageRotateTowardsMouse
from BubbleShooter.Methods.ImageCirculateAroundPoint import ImageCirculateAroundPoint
from BubbleShooter.Methods.LightShooter import LightShooter
class BubbleShooterScene(SceneManager.Scene):
    def __init__(self):
        super(BubbleShooterScene, self).__init__()
        pygame.init()
        # the mouse
        pygame.mouse.set_visible(True)
        self.mousePositionXOnClick = 0
        self.mousePositionYOnClick = 0
        # Loads in the images and changes it where needed
        self.backgroundImage = pygame.image.load('BubbleShooter\Images\BackgroundDiscoGrid.png').convert_alpha()
        self.backgroundImage = pygame.transform.scale(self.backgroundImage, (1600, 900))
        self.backgroundImageRect = self.backgroundImage.get_rect()
        self.BulletImage = 'BubbleShooter\Images\Enemy1.png'
        self.DiscoBallImage = 'BubbleShooter\Images\Player.png'
        self.DiscoBallImageWidth = 100
        self.DiscoBallImageHeight = 100
        self.DiscoballImagexPos = (self.backgroundImageRect.width / 2)
        self.DiscoballImageyPos = (self.backgroundImageRect.height / 2.5)
        self.DiscoballImageCenterX = (self.DiscoballImagexPos - (self.DiscoBallImageWidth / 2))
        self.DiscoBallImageCenterY = (self.DiscoballImageyPos - (self.DiscoBallImageHeight / 2))
        self.DiscoBallImageRect = pygame.image.load(self.DiscoBallImage).convert_alpha().get_rect
        # Creates the player and their functions
        self.Player = {}
        self.Player['Image'] = self.BulletImage
        self.Player['xStartPos'] = ((self.backgroundImageRect.width / 2) + self.DiscoBallImageWidth / 2)
        self.Player['yStartPos'] = ((self.backgroundImageRect.height / 2.5) + self.DiscoBallImageHeight / 2)
        self.Player['xPos'] = self.Player['xStartPos']
        self.Player['yPos'] = self.Player['yStartPos']
        self.Player['xClickPos'] = 0
        self.Player['yClickPos'] = 0
        self.Player['Width'] = 40
        self.Player['height'] = 40
        self.Player['shoot'] = False
        # Leftover / uncategorized:
        self.Velocity = 100

    def render(self, screen):
        screen.blit(self.backgroundImage, self.backgroundImageRect)
        ImageRotateTowardsMouse(self.DiscoBallImage, screen, self.DiscoBallImageWidth, self.DiscoBallImageHeight, self.DiscoballImagexPos, self.DiscoballImageyPos)
        ImageCirculateAroundPoint(self.Player['Image'], screen, self.Player['Width'], self.Player['height'], self.Player['xPos'], self.Player['yPos'])

    def handle_events(self, events):
        if not self.Player['shoot']:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.Player['shoot'] = True
                        self.mousePositionXOnClick, self.mousePositionYOnClick = pygame.mouse.get_pos()

    def update(self, deltaTime):
        self.mousePositionX, self.mousePositionY = pygame.mouse.get_pos()

        Vec2dOfMousePos = pygame.math.Vector2(self.mousePositionX, self.mousePositionY)
        Vec2dOfDiscoballPos = pygame.math.Vector2(self.DiscoballImagexPos, self.DiscoballImageyPos)
        # Vec2dOfDiscoballPos.as_polar(Vec2dOfMousePos)
        # MouseAngle = Vec2dOfMousePos.degrees(Vec2dOfDiscoballPos)
        # print("Mouse Angle: " + str(MouseAngle))

        x, y = Vec2dOfMousePos - Vec2dOfDiscoballPos
        angle = math.degrees(math.atan2(y, x))
        print(angle)

        # angle gebruiken ten opzichte van de discoball's X en Y as. (from_polar method)

        # print(str(self.DiscoballImagexPos) + "Lol" + str(self.DiscoballImageyPos))
        # if self.mousePositionX > self.DiscoballImagexPos:
        #     print("RIGHT!")
        # else:
        #     print("LEFT!")
        # if self.mousePositionY > self.DiscoballImageyPos:
        #     print("UNDER!")
        # else:
        #     print("ABOVE!")


        if self.Player['xPos'] == self.mousePositionXOnClick:
            print("Tada!!!")

        if self.Player['shoot'] == True:
            self.Player['xPos'] += ((self.mousePositionXOnClick - self.Player['xClickPos']) / self.Velocity * deltaTime)
            self.Player['yPos'] += ((self.mousePositionYOnClick - self.Player['yClickPos']) / self.Velocity * deltaTime)

            # print(self.mousePositionXOnClick)
            # print(self.mousePositionYOnClick)
            # print(self.Player['xPos'])
            # print(self.Player['yPos'])

            if self.Player['xPos'] >= 1600 or self.Player['xPos'] <= 0 or self.Player['yPos'] >= 900 or self.Player['yPos'] <= 0:
                self.Player['shoot'] = False
        else:
            # self.Player['xClickPos'] = self.Player['xPos']
            # self.Player['yClickPos'] = self.Player['yPos']
            # if self.backgroundImageRect.width / 2 > self.mousePositionX:
            #     self.Player['xPos'] = self.Player['xStartPos'] - self.DiscoBallImageWidth
            # else:
            #     self.Player['xPos'] = self.Player['xStartPos']
            # if self.backgroundImageRect.height / 2.5 > self.mousePositionY:
            #    self.Player['yPos'] = self.Player['yStartPos'] - self.DiscoBallImageHeight
            # else:
            #     self.Player['yPos'] = self.Player['yStartPos']

            pass

            # pygame.transform.rotozoom(pygame.image.load(self.Player['Image']).convert_alpha(), -angle + 90, 1)
            # from_polar() Sets x and y from a polar coordinates tuple.
            # from_polar((r, phi)) -> None Sets x and y from a tuple (r, phi) where r is the radial distance,
            # and phi is the azimuthal angle.