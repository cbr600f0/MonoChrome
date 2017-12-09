import pygame, math
from TowerDefense.Towers.Turret import Turret
#from Vector2 import Vector2
from TowerDefense.Towers.Projectiles.AkimboRevolverTurretBullet import AkimboRevolverTurretBullet as Bullet
from pygame.math import Vector2 as Vector2

class AkimboRevolverTurret(Turret):

    def __init__(self, pos, *sprite_groups):
        Turret.__init__(self, pos, *sprite_groups)

        self.bulletTimer = 0

        self.posToFollow = Vector2(0, 0)
        self.turretWidth = 58
        self.turretHeight = 114

        self.turretImage = pygame.image.load("TowerDefense\Images\Turrets\AkimboRevolverTurret.png").convert_alpha()
        # self.turretImage = pygame.transform.rotozoom(self.turretImage, self.direction, 2) This has more quality (the 2 makes the image bigger by X2)
        self.turretImage = pygame.transform.scale(self.turretImage, (self.turretWidth, self.turretHeight))

        self.image = self.turretImage
        self.rect = self.turretImage.get_rect()
        self.rect.move_ip(self.position)

        self.ShootLeftGun = True

    def update(self, deltaTime, allSprites, turretSprites, enemySprites, projectileSprites):
        enemyToShoot = self.getEnemiesInArea(self.position, self.range, enemySprites)

        if enemyToShoot is not None:

            self.posToFollow = enemyToShoot.position
            self.rotate()
            self.bulletTimer += deltaTime
            if self.bulletTimer > 0.6:

                if self.ShootLeftGun:
                    offset = Vector2(50, -16).rotate(self.direction)
                else:
                    offset = Vector2(50, 16).rotate(self.direction)
                    pass

                posToShootFrom = Vector2(self.position.x, self.position.y) + offset  # Center of the sprite.
                self.shoot(posToShootFrom, allSprites, projectileSprites, enemyToShoot)
                self.bulletTimer = 0
                self.ShootLeftGun = not self.ShootLeftGun

    def shoot(self, spawnPosition, allSprites, projectileSprites, enemyToFollow):
        bulletToShoot = Bullet(spawnPosition, enemyToFollow, allSprites, projectileSprites)

    def rotate(self):

        x, y = Vector2(self.posToFollow.x, self.posToFollow.y) - self.position
        angle = math.degrees(math.atan2(y, x))

        self.image = pygame.transform.rotozoom(self.turretImage, -angle + 90, 1)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.direction = angle

    def getEnemiesInArea(self, position, radius, enemySprites):
        closestEnemyPosition = None
        closestEnemy = None
        for enemy in enemySprites:
            distanceToEnemy = self.position.get_distance(enemy.position)
            if closestEnemyPosition is None:
                closestEnemyPosition = distanceToEnemy
                closestEnemy = enemy
            elif  distanceToEnemy < closestEnemyPosition:
                closestEnemyPosition = distanceToEnemy
                closestEnemy = enemy

        return closestEnemy



