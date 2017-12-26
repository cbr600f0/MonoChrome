import sys, pygame, math, random, SceneManager
from random import randint
from pygame import gfxdraw
from pygame.math import Vector2 as Vector2
from BubbleShooter2.LightBall import LightBall

class Player(pygame.sprite.Sprite):

    def __init__(self, allSprites, lightBallSprites, lightBallImages, *sprite_groups):
        super().__init__(*sprite_groups)

        self.allSprites = allSprites
        self.lightBallSprites = lightBallSprites

        self.lightBallImages = lightBallImages

        self.playerImage = pygame.image.load("BubbleShooter2\Images\Player.png").convert_alpha()
        self.playerImage = pygame.transform.scale(self.playerImage, (100, 100))
        self.angle = 0
        self.position = Vector2(800, 360)

        self.image = self.playerImage
        self.rect = self.playerImage.get_rect()
        self.rect.center = self.position

        self.lightBallInTheAir = False


        self.rotate()
        mousePos = pygame.mouse.get_pos()
        velocityVector = Vector2(mousePos) - self.position

        offset = Vector2(50, 0).rotate(self.angle)

        self.positionShootingFrom = Vector2(self.position) + offset
        self.currentLightBall = None
        self.loadNewLightBall()

        self.eventHandler = None

    def update(self, deltaTime, allSprites, lightBallSprites):
        self.allSprites = allSprites
        self.lightBallSprites = lightBallSprites
        self.rotate()
        mousePos = pygame.mouse.get_pos()
        velocityVector = Vector2(mousePos) - self.position

        offset = Vector2(70, 0).rotate(self.angle)

        self.positionShootingFrom = Vector2(self.position) + offset
        if (self.lightBallInTheAir == False):
            self.currentLightBall.position = self.positionShootingFrom

        if (self.eventHandler is not None and self.lightBallInTheAir == False):
            for event in self.eventHandler:
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                    self.lightBallInTheAir = True
                    self.currentLightBall.velocityVector = velocityVector.normalize()
                    self.currentLightBall.canMove = True



    def rotate(self):

        x, y = Vector2(pygame.mouse.get_pos()) - self.position
        angle = math.degrees(math.atan2(y, x))

        self.image = pygame.transform.rotozoom(self.playerImage, -angle + 90, 1)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.angle = angle

    def loadNewLightBall(self):
        lightBallColor, lightBallImage = random.choice(list(self.lightBallImages.items()))
        self.currentLightBall = LightBall(self.positionShootingFrom, self, lightBallImage, lightBallColor, False, None, self.allSprites, self.lightBallSprites)