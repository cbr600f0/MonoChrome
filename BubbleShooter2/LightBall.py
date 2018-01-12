import sys, pygame, math, random, SceneManager
from pygame import gfxdraw
from Vector2 import Vector2

class LightBall(pygame.sprite.Sprite):

    def __init__(self, BubbleShooterScene, spawnPos, playerInstance, lightBallId, lightBallImage, lightBallColor, isOnRoute, routePositions, *sprite_groups):
        super().__init__(*sprite_groups)

        lightBallId += 1
        self.lightBallId = lightBallId
        self.lightBallImage = lightBallImage
        self.lightBallImage = pygame.transform.scale(self.lightBallImage, (40, 40))
        self.position = Vector2(spawnPos)
        self.velocity = 600
        self.movementSpeed = 100

        self.lightBallColor = lightBallColor
        self.velocityVector = Vector2(0, 0)

        self.bubbleShooterScene = BubbleShooterScene

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

        self.rearrangeList = []
        self.sameColors = 0

        if self.isOnRoute:
            self.nextPositionToGoTo = Vector2(self.routePositions[self.destinationPosIndex][0], self.routePositions[self.destinationPosIndex][1])

    def moveBallFurther(self, x):
        currentBall = self.rearrangeList[x]
        distanceToMove = 40

        moveToPositionVector = currentBall.nextPositionToGoTo - currentBall.position
        moveToPositionVector.length = distanceToMove

        if moveToPositionVector.length <= currentBall.nextPositionToGoTo.get_distance(currentBall.position):
            currentBall.position += moveToPositionVector
        else:
            if moveToPositionVector.length > currentBall.nextPositionToGoTo.get_distance(currentBall.position):
                excessDistance = moveToPositionVector.length - currentBall.nextPositionToGoTo.get_distance(currentBall.position)

                moveToPositionVector2 = currentBall.routePositions[currentBall.destinationPosIndex + 1] - currentBall.nextPositionToGoTo
                moveToPositionVector2.length = excessDistance

                currentBall.position = currentBall.nextPositionToGoTo + moveToPositionVector2
                currentBall.nextPositionToGoTo = Vector2(currentBall.routePositions[currentBall.destinationPosIndex + 1])
                currentBall.destinationPosIndex += 1

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

            #2 sprites (light balls) colliding with each other
            for collidedSprite in pygame.sprite.spritecollide(self, lightBallSprites, False):
                if collidedSprite is not self:
                    for i in range(len(lightBallSprites.sprites())):

                        #to find the collided sprite
                        if collidedSprite == lightBallSprites.sprites()[i]:

                            #The shot sprite will be changed to a route sprite
                            self.isOnRoute = True
                            self.nextPositionToGoTo = collidedSprite.nextPositionToGoTo
                            self.destinationPosIndex = collidedSprite.destinationPosIndex

                            #The list will be re-ordered due to the changed sprite
                            for y in range(len(lightBallSprites.sprites())):
                                self.rearrangeList.append(lightBallSprites.sprites()[y])
                                print(lightBallSprites.sprites()[y].lightBallColor)
                            print("-----------------------")
                            x = len(self.rearrangeList) - 2
                            self.rearrangeList.append(lightBallSprites.sprites()[len(lightBallSprites.sprites()) - 1])
                            while x >= 0:
                                if x > i:
                                    self.rearrangeList[x + 1] = self.rearrangeList[x]
                                    #Hier moet ik programeren, dat de balletjes ongeveer 45 pixels naar de volgende
                                    #destination word geduwd. (dit zodat er ruimte is voor de nieuwe bal)
                                    #current ball is self.rearrangeList[x]

                                    self.moveBallFurther(x)

                                elif x == i:
                                    p = i
                                    listOfPoppedBalls = []

                                    while p >= 0:
                                        if self.rearrangeList[p].lightBallColor == self.lightBallColor:
                                            self.sameColors += 1
                                            listOfPoppedBalls.append(self.rearrangeList[p])
                                        else:
                                            break
                                        p -= 1
                                    p = i
                                    while p <= len(self.rearrangeList):
                                        if self.rearrangeList[p].lightBallColor == self.lightBallColor:
                                            self.sameColors += 1
                                        else:
                                            break
                                        p += 1
                                    if self.sameColors >= 3:
                                        for z in range(len(lightBallSprites.sprites())):
                                            for y in range(len(listOfPoppedBalls)):
                                                if self.rearrangeList[z].lightBallId == listOfPoppedBalls[y].lightBallId:
                                                    self.rearrangeList[z].kill()
                                    else:
                                        self.rearrangeList[x + 1] = self

                                        self.position = Vector2(collidedSprite.position)
                                        self.moveBallFurther(x + 1)
                                elif x < i:
                                    if i == len(self.rearrangeList) - 2:
                                        self.rearrangeList[len(self.rearrangeList) - 1] = self

                                        self.position = Vector2(collidedSprite.position)
                                        self.moveBallFurther(len(self.rearrangeList) - 1)
                                    elif i == len(self.rearrangeList) - 3:
                                        self.rearrangeList[len(self.rearrangeList) - 1] = self.rearrangeList[len(self.rearrangeList) - 2]
                                        self.rearrangeList[len(self.rearrangeList) - 2] = self

                                        self.position = Vector2(collidedSprite.position)
                                        self.moveBallFurther(len(self.rearrangeList) - 2)

                                x -= 1
                            if self.sameColors >= 3:
                                pass
                            lightBallSprites.empty()
                            for y in range(len(self.rearrangeList)):
                                self.rearrangeList[y].add(lightBallSprites)
                            for i in range(len(lightBallSprites.sprites())):
                                print(lightBallSprites.sprites()[i].lightBallColor)

                            # self.playerInstance.lightBallInTheAir = False
                            # self.playerInstance.loadNewLightBall()
                            break
                break
            if (self.position.x > 1650 or
                self.position.x < -50 or
                self.position.y > 950 or
                self.position.y < -50):
                    self.playerInstance.lightBallInTheAir = False
                    self.kill()
                    self.playerInstance.loadNewLightBall()



# lightballsprites.position,