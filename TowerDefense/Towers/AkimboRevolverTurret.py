import pygame, math
from TowerDefense.Towers.Turret import Turret
#from Vector2 import Vector2
from TowerDefense.Towers.Projectiles.AkimboRevolverTurretBullet import AkimboRevolverTurretBullet as Bullet
from pygame.math import Vector2 as Vector2

class AkimboRevolverTurret(Turret):

    def __init__(self, pos, levelReference, *sprite_groups):
        Turret.__init__(self, pos, *sprite_groups)

        self.bulletTimer = 0
        self.levelReference = levelReference
        self.posToFollow = Vector2(0, 0)
        self.turretWidth = 52
        self.turretHeight = 103

        self.turretImage = pygame.image.load("TowerDefense\Images\Turrets\AkimboRevolverTurret.png").convert_alpha()
        # self.turretImage = pygame.transform.rotozoom(self.turretImage, self.direction, 2) This has more quality (the 2 makes the image bigger by X2)
        self.turretImage = pygame.transform.scale(self.turretImage, (self.turretWidth, self.turretHeight))

        self.image = self.turretImage
        self.rect = self.turretImage.get_rect()
        self.rect.center = self.position

        self.ShootLeftGun = True

    def update(self, deltaTime, allSprites, turretSprites, enemySprites, projectileSprites):
        enemyToShoot = self.levelReference.getEnemiesInArea(self.position, self.range, enemySprites)

        if enemyToShoot is not None:

            self.posToFollow = enemyToShoot.position
            self.rotate()
            self.bulletTimer += deltaTime

            if self.bulletTimer > 0.5:

                if self.ShootLeftGun:
                    offset = Vector2(46, -14).rotate(self.direction)
                else:
                    offset = Vector2(46, 14).rotate(self.direction)

                posToShootFrom = Vector2(self.position.x, self.position.y) + offset  # Center of the sprite.
                self.shoot(posToShootFrom, allSprites, projectileSprites, enemyToShoot)

                self.ShootLeftGun = not self.ShootLeftGun
                self.bulletTimer = 0

    def shoot(self, spawnPosition, allSprites, projectileSprites, enemyToFollow):
        Bullet(spawnPosition, enemyToFollow, allSprites, projectileSprites)

    def rotate(self):

        x, y = Vector2(self.posToFollow.x, self.posToFollow.y) - self.position
        angle = math.degrees(math.atan2(y, x))

        self.image = pygame.transform.rotozoom(self.turretImage, -angle + 90, 1)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.direction = angle



