import sys, pygame, math, random, SceneManager
from pygame import gfxdraw
from Vector2 import Vector2

class LightBall(pygame.sprite.Sprite):

    def __init__(self, spawnPos, playerInstance, lightBallImage, lightBallColor, isOnRoute, routePositions, *sprite_groups):
        super().__init__(*sprite_groups)

        self.lightBallColor = lightBallColor
        self.lightBallImage = lightBallImage
        self.lightBallImage = pygame.transform.scale(self.lightBallImage, (40, 40))
        self.position = Vector2(spawnPos)
        self.velocity = 400
        self.movementSpeed = 290
        self.velocityVector = Vector2(0, 0)

        self.image = self.lightBallImage
        self.rect = self.lightBallImage.get_rect()
        self.rect.center = self.position

        self.playerInstance = playerInstance

        self.canMove = False
        self.isLastInLine = False
        self.isOnRoute = isOnRoute
        self.routePositions = routePositions

        self.destinationPosIndex = 0
        self.destinationPosIndex += 1
        self.nextPositionToGoTo = None

        if self.isOnRoute:
            self.nextPositionToGoTo = Vector2(self.routePositions[self.destinationPosIndex][0], self.routePositions[self.destinationPosIndex][1])

    def update(self, deltaTime, allSprites, lightBallSprites):
        if (self.canMove):
            if (self.isOnRoute == False): # Shooting
                self.position += self.velocityVector * self.velocity * deltaTime
            else: # Walking

                moveToPositionVector = self.nextPositionToGoTo - self.position

                if self.position.get_distance(self.nextPositionToGoTo) > 0:
                    moveToPositionVector.length = 1

                if moveToPositionVector.length > self.nextPositionToGoTo.get_distance(self.position):
                    moveToPositionVector.length = self.nextPositionToGoTo.get_distance(self.position)

                    if self.destinationPosIndex + 1 < len(self.routePositions):
                        self.destinationPosIndex += 1
                        self.nextPositionToGoTo = Vector2(self.routePositions[self.destinationPosIndex][0],
                                                         self.routePositions[self.destinationPosIndex][1])
                    else:# Reached the end
                        self.kill()

                self.position += moveToPositionVector * self.movementSpeed * deltaTime

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