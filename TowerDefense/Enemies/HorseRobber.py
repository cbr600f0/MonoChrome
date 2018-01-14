import pygame, math, random
from TowerDefense.Enemies.Enemy import Enemy
from Vector2 import Vector2
from TowerDefense.Enemies.Robber import Robber
from TowerDefense.Moneybag import Moneybag


class HorseRobber(Enemy):

    def __init__(self, bonusSpeed, health, goldOnKill, scoreOnKill, robber, positionsToFollow, levelReference, *sprite_groups):
        Enemy.__init__(self, positionsToFollow, *sprite_groups)

        self.currentRobber = robber
        self.horseHealth = health
        self.robberHealth = robber.health

        self.enemyWidth = 68
        self.enemyHeight = 114
        self.movementSpeed = 140 + bonusSpeed
        self.hasRobber = True

        self.levelReference = levelReference

        self.goldOnHorseKill = goldOnKill
        self.scoreOnHorseKill = scoreOnKill

        self.goldToSteal = robber.goldToSteal
        self.goldOnKill = robber.goldOnKill
        self.scoreOnKill = robber.scoreOnKill
        self.totalGoldOnEnemy = 0
        self.name = "Robber on a Horse"
        self.description = "A bank robber on a horse, Fast movement lower gold stealing capacity but, the robber has to get killed before the horse."

        #Horse with robber
        self.horseWithRobberImage = pygame.image.load("TowerDefense\Images\Enemies\HorseRobber.png").convert_alpha()
        self.horseWithRobberImage = pygame.transform.scale(self.horseWithRobberImage, (self.enemyWidth, self.enemyHeight))

        self.outlineEnemyImage = self.getOutline(self.horseWithRobberImage, [0, 0, 0])
        self.horseWithRobberImage.blit(self.outlineEnemyImage, (0, 0))

        #Horse without robber
        self.horseImage = pygame.image.load("TowerDefense\Images\Enemies\Horse.png").convert_alpha()
        self.horseImage = pygame.transform.scale(self.horseImage, (self.enemyWidth, self.enemyHeight))

        self.outlineEnemyImage = self.getOutline(self.horseImage, [0, 0, 0])
        self.horseImage.blit(self.outlineEnemyImage, (0, 0))
        self.horseMask = pygame.mask.from_surface(self.horseImage)

        self.hasGoldImage = pygame.image.load("TowerDefense\Images\Enemies\RobberOnHorseMoneybag.png").convert_alpha()
        self.hasGoldImage = pygame.transform.scale(self.hasGoldImage, (86, self.enemyHeight))

        self.outlinehasGoldImage = self.getOutline(self.hasGoldImage, [0, 0, 0])
        self.hasGoldImage.blit(self.outlinehasGoldImage, (0, 0))

        self.currentImage = self.horseWithRobberImage
        self.mask = self.horseMask

        self.painSound = pygame.mixer.Sound("TowerDefense/Sounds/enemyPain.wav")
        self.painSound.set_volume(0.008)

        self.deathSound = pygame.mixer.Sound("TowerDefense/Sounds/deathSound" + str(random.randint(1, 2)) + ".wav")
        self.deathSound.set_volume(0.008)

        self.laughSound = pygame.mixer.Sound("TowerDefense/Sounds/laugh" + str(random.randint(1, 2)) + ".wav")
        self.laughSound.set_volume(0.008)

        self.goldDropSound = pygame.mixer.Sound("TowerDefense/Sounds/goldDrop.wav")
        self.goldDropSound.set_volume(0.0088)

        self.image = self.currentImage
        self.rect = self.currentImage.get_rect()
        self.rect.center = self.position

        self.destinationPosIndex += 1
        self.nextPositionToGoTo = Vector2(self.positionsToFollow[self.destinationPosIndex][0],
                                          self.positionsToFollow[self.destinationPosIndex][1])

        self.hasChangedImageToGoldBags = False

        previousPos = Vector2(self.position)
        for positionToGoTo in self.positionsToFollow:
            self.distanceLeft += Vector2(positionToGoTo).get_distance(previousPos)
            previousPos = Vector2(positionToGoTo)

    def update(self, deltaTime):

        if self.hasDied is False:
            moveToPositionVector = self.nextPositionToGoTo - self.position

            if not moveToPositionVector.get_length() == 0:
                moveToPositionVector.length = self.movementSpeed * deltaTime

                if moveToPositionVector.length >= self.nextPositionToGoTo.get_distance(self.position) - moveToPositionVector.length:
                    self.position = Vector2(self.nextPositionToGoTo)

                    if self.destinationPosIndex + 1 < len(self.positionsToFollow):
                        self.destinationPosIndex += 1
                        self.nextPositionToGoTo = Vector2(self.positionsToFollow[self.destinationPosIndex][0],
                                                          self.positionsToFollow[self.destinationPosIndex][1])

                        self.rotate()
                    else:
                        self.kill()
                        self.hasDied = True
                else:
                    self.position += moveToPositionVector
                    self.distanceLeft -= self.movementSpeed * deltaTime


            if self.hasRobber:
                for collidedMoneybag in pygame.sprite.spritecollide(self, self.levelReference.moneybagSprites, False):
                    if collidedMoneybag.enemyCanPickupBag:
                        self.totalGoldOnEnemy += collidedMoneybag.goldValue
                        collidedMoneybag.kill()

                if self.totalGoldOnEnemy > 0 and not self.hasChangedImageToGoldBags:
                    self.hasChangedImageToGoldBags = True
                    self.currentImage = self.hasGoldImage
                    self.rotate()
            else:
                for enemy in self.levelReference.enemySprites.sprites():
                    if isinstance(enemy, Robber):
                        if pygame.sprite.collide_mask(enemy, self):
                            self.addRobber(enemy)
                            break

            self.rect = self.image.get_rect()
            self.rect.center = self.position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def rotate(self):

        #  Move towards PosToFollow
        PosToFollowLookatVector = self.nextPositionToGoTo - self.position
        self.direction = -PosToFollowLookatVector.angle - 90 # this is NOT the correct way to do this check how AkimboRevolverTurret does rotating!

        self.image = pygame.transform.rotate(self.currentImage, self.direction)  # the image is rotated the wrong way so the plus 90 fixed this
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def takeDamage(self, damageTaken):

        if self.hasDied is False:
            playDeathSound = False

            if self.hasRobber:
                self.robberHealth -= damageTaken
            else:
                self.horseHealth -= damageTaken

            if self.hasRobber and self.robberHealth <= 0: # The robber died
                self.removeRobber()
                playDeathSound = True
            elif not self.hasRobber and self.horseHealth <= 0: #The horse died
                playDeathSound = True
                self.die()

            if playDeathSound:
                self.deathSound.play()
            else:
                self.painSound.play()

    def die(self):
        if self.hasDied is False:
            self.laughSound.stop()

            self.levelReference.totalEnemiesKilled += 1
            self.levelReference.gold += self.goldOnHorseKill
            self.levelReference.score += self.scoreOnHorseKill

            self.kill()
            self.hasDied = True

    def removeRobber(self):
        self.name = "Loneley Horse"

        self.levelReference.totalEnemiesKilled += 1
        self.levelReference.gold += self.goldOnKill
        self.levelReference.score += self.scoreOnKill

        self.goldOnKill = self.goldOnHorseKill
        self.scoreOnKill = self.scoreOnHorseKill

        if self.totalGoldOnEnemy > 0:
            self.goldDropSound.play()
            Moneybag(Vector2(self.position), 90, self.levelReference, self.totalGoldOnEnemy, self.levelReference.allSprites, self.levelReference.moneybagSprites)

        self.totalGoldOnEnemy = 0
        self.robberHealth = 0
        self.hasRobber = False
        self.currentImage = self.horseImage
        self.rotate()
        self.movementSpeed = 260
        self.currentRobber = None

    def addRobber(self, robber):
        self.name = "Robber on a Horse"
        self.hasStolenGoldFromBank = robber.hasStolenGoldFromBank
        self.currentRobber = robber
        self.robberHealth = robber.health
        self.totalGoldOnEnemy = robber.totalGoldOnEnemy
        self.goldOnKill = robber.goldOnKill
        self.scoreOnKill = robber.scoreOnKill

        self.hasRobber = True
        self.currentImage = self.horseWithRobberImage
        self.rotate()
        self.movementSpeed = 170

        robber.hasDied = True
        robber.kill()

    def getOutline(self, image, color=(0, 0, 0), threshold=127):
        mask = pygame.mask.from_surface(image, threshold)
        outline_image = pygame.Surface(image.get_size()).convert_alpha()
        outline_image.fill((0, 0, 0, 0))
        for point in mask.outline():
            outline_image.set_at(point, color)
        return outline_image

    def playLaughSound(self):
        self.laughSound.play()
