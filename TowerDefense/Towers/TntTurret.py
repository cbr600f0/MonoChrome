import pygame, math
from TowerDefense.Towers.Turret import Turret
from pygame.math import Vector2 as Vector2
from TowerDefense.Towers.Projectiles.TntTurretDynamite import TntTurretDynamite

class TntTurret(Turret):

    def __init__(self, pos, levelReference, *sprite_groups):
        Turret.__init__(self, pos, levelReference, *sprite_groups)

        self.dynamiteImages = []

        self.dynamiteImages.append(pygame.image.load("TowerDefense\Images\Turrets\Projectiles\Dynamite_1.png").convert_alpha())
        self.dynamiteImages.append(pygame.image.load("TowerDefense\Images\Turrets\Projectiles\Dynamite_2.png").convert_alpha())
        self.dynamiteImages.append(pygame.image.load("TowerDefense\Images\Turrets\Projectiles\Dynamite_3.png").convert_alpha())
        self.dynamiteImages.append(pygame.image.load("TowerDefense\Images\Turrets\Projectiles\Dynamite_4.png").convert_alpha())
        self.dynamiteImages.append(pygame.image.load("TowerDefense\Images\Turrets\Projectiles\dynamiteExplosion.png").convert_alpha())

        self.attackTimer = 0
        self.posToFollow = Vector2(0, 0)
        self.turretWidth = 86
        self.turretHeight = 74

        self.range = 130
        self.nextLevelRange = 140

        self.areaOfEffect = 110
        self.nextLevelAOE = 120

        self.fireRate = 0.6 # shots per second
        self.nextLevelFireRate = 0.65

        self.fuseTime = 0.8
        self.nextLevelFuseTime = 0.7

        self.damage = 10
        self.nextLevelDamage = 18

        self.throwVelocity = 510
        self.name = "Dynamite Cowboy"
        self.description = "A cowboy with dynamite sticks, deals damage to all enemies hit in a radius"

        self.upgradeCost = 210
        self.buyPrice = 150
        self.totalGoldSpendOnTurret = self.buyPrice

        self.turretImage = pygame.image.load("TowerDefense\Images\Turrets\TntTurret.png").convert_alpha()
        self.turretImage = pygame.transform.scale(self.turretImage, (self.turretWidth, self.turretHeight))
        self.outlineTurretImage = self.getOutline(self.turretImage, [0, 0, 0])
        self.turretImage.blit(self.outlineTurretImage, (0, 0))

        self.image = self.turretImage
        self.rect = self.turretImage.get_rect()
        self.rect.center = self.position

        self.collisionRect = pygame.Rect(self.rect.x, self.rect.y, self.turretWidth, self.turretHeight)

        self.ShootLeftGun = True
        self.offset = Vector2(0, -34).rotate(self.direction)

    def update(self, deltaTime):
        if not self.isUpgrading:
            enemyToFollow = self.levelReference.GetClosestEnemyToDestination(self.position, self.range, self.levelReference.enemySprites)

            if enemyToFollow is not None:

                self.posToFollow = enemyToFollow.position
                self.rotate()
                self.attackTimer += deltaTime

                if self.attackTimer > 1 / self.fireRate:

                    try:
                        if self.ShootLeftGun:
                            self.offset = Vector2(0, -34).rotate(self.direction)
                        else:
                            self.offset = Vector2(0, 34).rotate(self.direction)
                    except:
                        self.offset = Vector2(0, 0)

                    posToShootFrom = Vector2(self.position.x, self.position.y) + self.offset
                    self.shoot(posToShootFrom, enemyToFollow.position)

                    self.ShootLeftGun = not self.ShootLeftGun
                    self.attackTimer = 0
        else:
            if self.upgradeTimer < self.upgradeDuration:
                self.upgradeTimer += deltaTime
            else:
                self.__upgradedTurret()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        if self.isFocusedByUser:
            pygame.draw.circle(screen, [0, 0, 0], self.position, self.range, 2)

        if self.isUpgrading:
            upgradeBarWidth = 60
            upgradeBarProgressWidth = (self.upgradeTimer / self.upgradeDuration * 60)

            pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(self.rect.centerx - (upgradeBarWidth / 2), self.rect.centery - 10, upgradeBarWidth, 10))
            pygame.draw.rect(screen, [70, 50, 34], pygame.Rect(self.rect.centerx - (upgradeBarWidth / 2), self.rect.centery - 10, upgradeBarProgressWidth, 10))
            pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(self.rect.centerx - (upgradeBarWidth / 2), self.rect.centery - 10, upgradeBarWidth, 10), 2)

    def shoot(self, spawnPosition, posToGoTO):
        TntTurretDynamite(self.damage, self.fuseTime, self.throwVelocity, self.areaOfEffect, spawnPosition, posToGoTO, self.dynamiteImages, self.levelReference, self.levelReference.allSprites, self.levelReference.projectileSprites)

    def rotate(self):

        x, y = Vector2(self.posToFollow.x, self.posToFollow.y) - self.position
        angle = math.degrees(math.atan2(y, x))

        self.image = pygame.transform.rotozoom(self.turretImage, -angle + 90, 1)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.direction = angle

    def getOutline(self, image, color=(0, 0, 0), threshold=127):
        mask = pygame.mask.from_surface(image, threshold)
        outline_image = pygame.Surface(image.get_size()).convert_alpha()
        outline_image.fill((0, 0, 0, 0))

        #outline_image = pygame.transform.rotozoom(outline_image, 0, 1)

        for point in mask.outline():
            outline_image.set_at(point, color)
        return outline_image

    def __upgradedTurret(self):
        self.upgradeTimer = 0
        self.isUpgrading = False
        self.turretLevel += 1

        self.damage = self.nextLevelDamage
        self.fireRate = self.nextLevelFireRate
        self.range = self.nextLevelRange
        self.areaOfEffect = self.nextLevelAOE
        self.fuseTime = self.nextLevelFuseTime

        if self.turretLevel == 2:
            self.nextLevelDamage = 32
            self.nextLevelFireRate = 0.7
            self.nextLevelRange = 150

            self.nextLevelAOE = 130
            self.nextLevelFuseTime = 0.6

            self.upgradeCost = 360

        elif self.turretLevel == 3:
            self.nextLevelDamage = 52
            self.nextLevelFireRate = 0.85
            self.nextLevelRange = 170

            self.nextLevelAOE = 150
            self.nextLevelFuseTime = 0.45

            self.upgradeCost = 720


