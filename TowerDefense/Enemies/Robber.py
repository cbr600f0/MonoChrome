import pygame, math
from TowerDefense.Enemies.Enemy import Enemy
from Vector2 import Vector2


class Robber(Enemy):

    def __init__(self, positionsToFollow, levelReference, *sprite_groups):
        Enemy.__init__(self, positionsToFollow, *sprite_groups)

        self.health = 100
        self.enemyWidth = 65
        self.enemyHeight = 40
        self.movementSpeed = 110

        self.levelReference = levelReference

        self.goldToSteal = 100
        self.goldOnKill = 100
        self.scoreOnKill = 20

        self.enemyImage = pygame.image.load("TowerDefense\Images\Enemies\Robber.png").convert_alpha()
        self.enemyImage = pygame.transform.scale(self.enemyImage, (self.enemyWidth, self.enemyHeight))
        self.outlineEnemyImage = self.getOutline(self.enemyImage, [0, 0, 0])
        self.enemyImage.blit(self.outlineEnemyImage, (0, 0))
        self.enemyMask = pygame.mask.from_surface(self.enemyImage)

        #self.deathSound = pygame.mixer.Sound("TowerDefense/Sounds/RobloxDeathSound.ogg")

        self.image = self.enemyImage
        self.rect = self.enemyImage.get_rect()
        self.rect.center = self.position

        self.destinationPosIndex += 1
        self.nextPositionToGoTo = Vector2(self.positionsToFollow[self.destinationPosIndex][0],
                                          self.positionsToFollow[self.destinationPosIndex][1])

    def update(self, deltaTime, allSprites, turretSprites, enemySprites, projectileSprites):

        if self.hasDied is False:

            moveToPositionVector = self.nextPositionToGoTo - self.position

            if self.position.get_distance(self.nextPositionToGoTo) > 0:
                moveToPositionVector.length = 1

            if moveToPositionVector.length > self.nextPositionToGoTo.get_distance(self.position):
                moveToPositionVector.length = self.nextPositionToGoTo.get_distance(self.position)

                if self.destinationPosIndex + 1 < len(self.positionsToFollow):
                    self.destinationPosIndex += 1
                    self.nextPositionToGoTo = Vector2(self.positionsToFollow[self.destinationPosIndex][0],
                                                      self.positionsToFollow[self.destinationPosIndex][1])
                    self.rotate()
                else:
                    self.levelReference.gold -= self.goldToSteal  # Reached the end
                    self.hasDied = True
                    self.kill()

            self.position += moveToPositionVector * self.movementSpeed * deltaTime

            self.image = pygame.transform.rotate(self.enemyImage, self.direction)
            self.rect = self.image.get_rect()
            self.rect.center = self.position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def rotate(self):

        #  Move towards PosToFollow
        PosToFollowLookatVector = self.nextPositionToGoTo - self.position
        self.direction = -PosToFollowLookatVector.angle - 90 # this is NOT the correct way to do this check how AkimboRevolverTurret does rotating!

        self.image = pygame.transform.rotate(self.enemyImage, self.direction)  # the image is rotated the wrong way so the plus 90 fixed this
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def takeDamage(self, damageTaken):

        if self.hasDied is False:
            self.health -= damageTaken

            if self.health <= 0:
                self.die()

    def die(self):
        if self.hasDied is False:

            self.levelReference.gold += self.goldOnKill
            self.levelReference.score += self.scoreOnKill

            #self.deathSound.play()
            self.kill()
            self.hasDied = True

    def getOutline(self, image, color=(0, 0, 0), threshold=127):
        mask = pygame.mask.from_surface(image, threshold)
        outline_image = pygame.Surface(image.get_size()).convert_alpha()
        outline_image.fill((0, 0, 0, 0))
        for point in mask.outline():
            outline_image.set_at(point, color)
        return outline_image
