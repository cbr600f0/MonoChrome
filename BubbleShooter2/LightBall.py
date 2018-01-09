import sys, pygame, math, random, SceneManager
from pygame import gfxdraw
from Vector2 import Vector2

class LightBall(pygame.sprite.Sprite):

    def __init__(self, spawnPos, playerInstance, lightBallImage, lightBallColor, isOnRoute, routePositions, *sprite_groups):
        super().__init__(*sprite_groups)

        self.lightBallImage = lightBallImage
        self.lightBallImage = pygame.transform.scale(self.lightBallImage, (40, 40))
        self.position = Vector2(spawnPos)
        self.velocity = 400
        self.movementSpeed = 200
        self.lightBallColor = lightBallColor
        self.lightBallImage = lightBallImage
        self.lightBallImage = pygame.transform.scale(self.lightBallImage, (40, 40))
        self.position = Vector2(spawnPos)
        self.velocity = 400
        self.movementSpeed = 200
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
            else:  # Walking

                moveToPositionVector = self.nextPositionToGoTo - self.position
                if moveToPositionVector.length != 0:
                    moveToPositionVector.length = self.movementSpeed * deltaTime

                    if moveToPositionVector.length > self.nextPositionToGoTo.get_distance(self.position) - moveToPositionVector.length:
                        moveToPositionVector.length = self.nextPositionToGoTo.get_distance(self.position)

                        if self.destinationPosIndex + 1 < len(self.routePositions):
                            self.destinationPosIndex += 1
                            self.nextPositionToGoTo = Vector2(self.routePositions[self.destinationPosIndex][0],
                                                             self.routePositions[self.destinationPosIndex][1])
                        else:# Reached the end
                            self.kill()

                    self.position += moveToPositionVector

        self.rect = self.lightBallImage.get_rect()
        self.rect.center = self.position

        if(self.isOnRoute == False):
            for collidedSprite in pygame.sprite.spritecollide(self, lightBallSprites, False):
                if collidedSprite is not self:
                    for i in range(len(lightBallSprites.sprites())):
                        if collidedSprite == lightBallSprites.sprites()[i]:
                            self.isOnRoute = True
                            self.nextPositionToGoTo = collidedSprite.nextPositionToGoTo
                            self.destinationPosIndex = collidedSprite.destinationPosIndex
                            for i in range(len(lightBallSprites.sprites())):
                                print(lightBallSprites.sprites()[i].lightBallColor)
                                if i < 3:
                                    lightBallSprites.sprites()[i], lightBallSprites.sprites()[i + 1] = lightBallSprites.sprites()[i + 1], lightBallSprites.sprites()[i]
                            print("-----------------------")
                            for i in range(len(lightBallSprites.sprites())):
                                print(lightBallSprites.sprites()[i].lightBallColor)
                            # self.playerInstance.lightBallInTheAir = False
                            # self.playerInstance.loadNewLightBall()
                            self.position = Vector2(collidedSprite.position)
                            break

            if (self.position.x > 1650 or
                self.position.x < -50 or
                self.position.y > 950 or
                self.position.y < -50):
                    self.playerInstance.lightBallInTheAir = False
                    self.kill()
                    self.playerInstance.loadNewLightBall()


# lightballsprites.position,