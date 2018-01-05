import pygame, math, random
from TowerDefense.Enemies.Enemy import Enemy
from pygame.math import Vector2 as Vector2


class Bank(pygame.sprite.Sprite):

    def __init__(self, spawnPos, degrees, levelReference, *sprite_groups):
        super().__init__(*sprite_groups)

        self.levelReference = levelReference
        self.direction = degrees
        self.position = spawnPos
        self.bankImage = pygame.image.load("TowerDefense/Images/Bank2.png").convert_alpha()
        self.bankOutline = self.getOutline(self.bankImage, [0, 0, 0])
        self.bankImage.blit(self.bankOutline, (0, 0))
        self.rotate()

        self.offset = Vector2(80, 40).rotate(self.direction)
        self.lootCenterPos = self.position + self.offset

    def update(self, deltaTime):
        for enemy in self.GetAllEnemiesInRadius(self.lootCenterPos, 50):
            if enemy.hasStolenGoldFromBank == False:
                enemy.playLaughSound()
                enemy.hasStolenGoldFromBank = True

                self.levelReference.gold -= enemy.goldToSteal
                enemy.totalGoldOnEnemy += enemy.goldToSteal


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def rotate(self):

        self.image = pygame.transform.rotate(self.bankImage, -self.direction + 90)  # the image is rotated the wrong way so the plus 90 fixed this
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def getOutline(self, image, color=(0, 0, 0), threshold=127):
        mask = pygame.mask.from_surface(image, threshold)
        outline_image = pygame.Surface(image.get_size()).convert_alpha()
        outline_image.fill((0, 0, 0, 0))
        for point in mask.outline():
            outline_image.set_at(point, color)
        return outline_image

    def GetAllEnemiesInRadius(self, centerPos, radius):

        enemiesInRadius = []

        for enemy in self.levelReference.enemySprites:
            distanceToEnemy = centerPos.get_distance(enemy.position)

            if distanceToEnemy <= radius:
                enemiesInRadius.append(enemy)

        return enemiesInRadius
