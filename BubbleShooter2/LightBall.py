import sys, pygame, math, random, SceneManager
from pygame import gfxdraw
from pygame.math import Vector2 as Vector2

class LightBall(pygame.sprite.Sprite):

    def __init__(self, spawnPos, playerInstance, lightBallImage, lightBallColor, isOnRoute, routePositions, *sprite_groups):
        super().__init__(*sprite_groups)

        self.lightBallColor = lightBallColor
        self.lightBallImage = lightBallImage
        self.lightBallImage = pygame.transform.scale(self.lightBallImage, (40, 40))
        self.position = Vector2(spawnPos)
        self.velocity = 400
        self.velocityVector = Vector2(0, 0)

        self.image = self.lightBallImage
        self.rect = self.lightBallImage.get_rect()
        self.rect.center = self.position

        self.playerInstance = playerInstance

        self.canMove = False
        self.isLastInLine = False
        self.isOnRoute = isOnRoute
        self.routePositions = routePositions

    def update(self, deltaTime, allSprites, lightBallSprites):
        if (self.canMove == True):
            if (self.isOnRoute == False):
                self.position += self.velocityVector * self.velocity * deltaTime
            else:
                self.pushNextLightBall(lightBallSprites)

        self.rect = self.lightBallImage.get_rect()
        self.rect.center = self.position
        if(self.isOnRoute == False):
            if (self.position.x > 1650 or
                self.position.x < -50 or
                self.position.y > 950 or
                self.position.y < -50):
                self.playerInstance.lightBallInTheAir = False
                self.kill()
                self.playerInstance.loadNewLightBall()

    def pushNextLightBall(self, lightBallSprite):
        pass