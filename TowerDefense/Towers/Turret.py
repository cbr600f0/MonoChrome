import pygame, math
from pygame import gfxdraw
from Vector2 import Vector2

class Turret(pygame.sprite.Sprite):

    def __init__(self, pos, levelReference, *sprite_groups):
        super().__init__(*sprite_groups)

        self.levelReference = levelReference
        self.name = "Base Turret"
        self.position = pos

        self.direction = 0 # What is the angle of this turret(Used for rotating the turret)
        self.isFocusedByUser = False
        self.collisionRect = pygame.Rect(0, 0, 0, 0) # has to be implemented by the class that inherets this class
        self.description = "A BASE TURRET"

        self.damage = 10
        self.nextLevelDamage = 0

        self.fireRate = 1
        self.nextLevelFireRate = 0

        self.range = 200
        self.nextLevelRange = 0

        self.upgradeTimer = 0
        self.upgradeDuration = 1

        self.turretLevel = 1
        self.turretMaxLevel = 4

        self.upgradeCost = 120

        self.buyPrice = 100
        self.isUpgrading = False
        self.totalGoldSpendOnTurret = self.buyPrice

    def upgradeTurret(self):
        if self.levelReference.gold >= self.upgradeCost and not self.isUpgrading and self.turretLevel < self.turretMaxLevel:
            self.isUpgrading = True
            self.levelReference.gold -= self.upgradeCost
            self.totalGoldSpendOnTurret += self.upgradeCost

    def __upgradedTurret(self):
        pass

    def sellTurret(self):
        self.levelReference.gold += math.floor(self.totalGoldSpendOnTurret * 0.4)
        self.kill()
