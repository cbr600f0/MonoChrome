import pygame, math, random
from TowerDefense.Enemies.Enemy import Enemy
from Vector2 import Vector2
from TowerDefense.Moneybag import Moneybag


class Robber(Enemy):

    def __init__(self, health, goldOnKill, scoreOnKill, goldToSteal, positionsToFollow, levelReference, *sprite_groups):
        Enemy.__init__(self, positionsToFollow, *sprite_groups)

        self.health = health
        self.enemyWidth = 65
        self.enemyHeight = 40
        self.movementSpeed = 90

        self.levelReference = levelReference

        self.goldToSteal = goldToSteal
        self.goldOnKill = goldOnKill
        self.scoreOnKill = scoreOnKill
        self.totalGoldOnEnemy = 0
        self.name = "Bank Robber"
        self.description = "A bank robber, an enemy with medium stats."

        self.enemyImage = pygame.image.load("TowerDefense\Images\Enemies\Robber.png").convert_alpha()
        self.enemyImage = pygame.transform.scale(self.enemyImage, (self.enemyWidth, self.enemyHeight))

        self.outlineEnemyImage = self.getOutline(self.enemyImage, [0, 0, 0])
        self.enemyImage.blit(self.outlineEnemyImage, (0, 0))
        self.robberMask = pygame.mask.from_surface(self.enemyImage)

        self.hasGoldImage = pygame.image.load("TowerDefense\Images\Enemies\MoneyBagRobber.png").convert_alpha()
        self.hasGoldImage = pygame.transform.scale(self.hasGoldImage, (80, 40))

        self.outlinehasGoldImage = self.getOutline(self.hasGoldImage, [0, 0, 0])
        self.hasGoldImage.blit(self.outlinehasGoldImage, (0, 0))

        self.currentImage = self.enemyImage
        self.mask = self.robberMask

        self.painSound = pygame.mixer.Sound("TowerDefense/Sounds/enemyPain.wav")
        self.painSound.set_volume(0.008)

        self.deathSound = pygame.mixer.Sound("TowerDefense/Sounds/deathSound" + str(random.randint(1, 2)) + ".wav")
        self.deathSound.set_volume(0.008)

        self.laughSound = pygame.mixer.Sound("TowerDefense/Sounds/laugh" + str(random.randint(1, 2)) + ".wav")#        self.laughSound = pygame.mixer.Sound("TowerDefense/Sounds/laugh" + str(random.randint(1, 2)) + ".wav")
        self.laughSound.set_volume(0.008)

        self.goldDropSound = pygame.mixer.Sound("TowerDefense/Sounds/goldDrop.wav")
        self.goldDropSound.set_volume(0.0088)

        self.image = self.enemyImage
        self.rect = self.enemyImage.get_rect()
        self.rect.center = self.position

        self.destinationPosIndex += 1
        self.nextPositionToGoTo = Vector2(self.positionsToFollow[self.destinationPosIndex][0],
                                          self.positionsToFollow[self.destinationPosIndex][1])

        self.hasChangedImageToGoldBags = False

        for positionToGoTo in self.positionsToFollow:
            self.distanceLeft += Vector2(positionToGoTo).get_distance(self.position)

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
                    self.distanceLeft -= moveToPositionVector.length
                    print(self.distanceLeft)

            for collidedMoneybag in pygame.sprite.spritecollide(self, self.levelReference.moneybagSprites, False):
                if collidedMoneybag.enemyCanPickupBag:
                    self.totalGoldOnEnemy += collidedMoneybag.goldValue
                    collidedMoneybag.kill()

            if self.totalGoldOnEnemy > 0 and not self.hasChangedImageToGoldBags:
                self.hasChangedImageToGoldBags = True
                self.currentImage = self.hasGoldImage
                self.rotate()

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

            self.health -= damageTaken
            if self.health <= 0:
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
            self.levelReference.gold += self.goldOnKill

            if self.totalGoldOnEnemy > 0:
                Moneybag(Vector2(self.position), 90, self.levelReference, self.totalGoldOnEnemy, self.levelReference.allSprites, self.levelReference.moneybagSprites)
                self.goldDropSound.play()

            self.levelReference.score += self.scoreOnKill
            self.kill()
            self.hasDied = True

    def getOutline(self, image, color=(0, 0, 0), threshold=127):
        mask = pygame.mask.from_surface(image, threshold)
        outline_image = pygame.Surface(image.get_size()).convert_alpha()
        outline_image.fill((0, 0, 0, 0))
        for point in mask.outline():
            outline_image.set_at(point, color)
        return outline_image

    def playLaughSound(self):
        self.laughSound.play()
