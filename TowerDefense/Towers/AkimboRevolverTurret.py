import pygame
from TowerDefense.Towers.Turret import Turret
from Vector2 import Vector2
from TowerDefense.Towers.Projectiles.AkimboRevolverTurretBullet import AkimboRevolverTurretBullet as Bullet


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
        enemyToShoot = None
        if len(enemySprites.sprites()) > 0:
            enemyToShoot = enemySprites.sprites()[0]

        if enemyToShoot is not None:

            self.posToFollow = enemyToShoot.position
            self.rotate()
            self.bulletTimer += deltaTime
            if self.bulletTimer > 0.7:

                if self.ShootLeftGun:
                    pass
                    #posToShootFrom = self.position
                else:
                    pass
                   #posToShootFrom = self.position
                    pass

                self.shoot(self.position, allSprites, projectileSprites, enemyToShoot)
                self.bulletTimer = 0
                self.ShootLeftGun = not self.ShootLeftGun

    def shoot(self, spawnPosition, allSprites, projectileSprites, enemyToFollow):
        bulletToShoot = Bullet(spawnPosition, enemyToFollow, allSprites, projectileSprites)

    def rotate(self):

        MouseLookAt = self.posToFollow - Vector2((self.rect.centerx, self.rect.centery))
        self.direction = -MouseLookAt.angle + 90
        self.image = pygame.transform.rotozoom(self.turretImage, self.direction, 1)  # the image is rotated the wrong way so the plus 90 fixed this
        self.rect = self.image.get_rect()
        self.rect.center = self.position
