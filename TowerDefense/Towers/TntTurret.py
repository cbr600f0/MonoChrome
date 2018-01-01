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

        self.range = 210
        self.nextLevelRange = 240

        self.areaOfEffect = 140
        self.nextLevelAOE = 150

        self.fireRate = 1.2 # shots per second
        self.nextLevelFireRate = 1.35

        self.fuseTime = 0.9
        self.nextLevelFuseTime = 0.75

        self.damage = 80
        self.nextLevelDamage = 120

        self.throwVelocity = 460
        self.name = "Dynamite Cowboy"
        self.description = "A cowboy with dynamite sticks, deals damage to all enemies hit in a radius"

        self.upgradeCost = 210
        self.buyPrice = 180
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

    def update(self, deltaTime, allSprites, turretSprites, enemySprites, projectileSprites):
        if not self.isUpgrading:
            enemyToFollow = self.levelReference.GetClosestEnemyInRadius(self.position, self.range, enemySprites)

            if enemyToFollow is not None:

                self.posToFollow = enemyToFollow.position
                self.rotate()
                self.attackTimer += deltaTime

                if self.attackTimer > 1 / self.fireRate:

                    if self.ShootLeftGun:
                        offset = Vector2(0, -34).rotate(self.direction)
                    else:
                        offset = Vector2(0, 34).rotate(self.direction)

                    posToShootFrom = Vector2(self.position.x, self.position.y) + offset  # Center of the sprite.
                    self.shoot(posToShootFrom, allSprites, projectileSprites, enemyToFollow.position)

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

    def shoot(self, spawnPosition, allSprites, projectileSprites, posToGoTO):
        TntTurretDynamite(self.damage, self.fuseTime, self.throwVelocity, self.areaOfEffect, spawnPosition, posToGoTO, self.dynamiteImages, self.levelReference, allSprites, projectileSprites)

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
            self.nextLevelDamage = 140
            self.nextLevelFireRate = 1.5
            self.nextLevelRange = 270

            self.nextLevelAOE = 160
            self.nextLevelFuseTime = 0.6

            self.upgradeCost = 350

        elif self.turretLevel == 3:
            self.nextLevelDamage = 190
            self.nextLevelFireRate = 1.8
            self.nextLevelRange = 310

            self.nextLevelAOE = 210
            self.nextLevelFuseTime = 0.4

            self.upgradeCost = 600


