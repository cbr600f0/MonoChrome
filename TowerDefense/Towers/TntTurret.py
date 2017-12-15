import pygame, math
from TowerDefense.Towers.Turret import Turret
from pygame.math import Vector2 as Vector2
from TowerDefense.Towers.Projectiles.TntTurretDynamite import TntTurretDynamite

class TntTurret(Turret):

    def __init__(self, pos, levelReference, *sprite_groups):
        Turret.__init__(self, pos, *sprite_groups)

        self.dynamiteImages = []

        self.dynamiteImages.append(pygame.image.load("TowerDefense\Images\Turrets\Projectiles\Dynamite_1.png").convert_alpha())
        self.dynamiteImages.append(pygame.image.load("TowerDefense\Images\Turrets\Projectiles\Dynamite_2.png").convert_alpha())
        self.dynamiteImages.append(pygame.image.load("TowerDefense\Images\Turrets\Projectiles\Dynamite_3.png").convert_alpha())
        self.dynamiteImages.append(pygame.image.load("TowerDefense\Images\Turrets\Projectiles\Dynamite_4.png").convert_alpha())
        self.dynamiteImages.append(pygame.image.load("TowerDefense\Images\Turrets\Projectiles\dynamiteExplosion.png").convert_alpha())

        self.attackTimer = 0
        self.levelReference = levelReference
        self.posToFollow = Vector2(0, 0)
        self.turretWidth = 86
        self.turretHeight = 74

        self.range = 210
        self.areaOfEffect = 110
        self.damage = 80
        self.throwVelocity = 360

        self.turretImage = pygame.image.load("TowerDefense\Images\Turrets\TntTurret.png").convert_alpha()
        # self.turretImage = pygame.transform.rotozoom(self.turretImage, self.direction, 2) This has more quality (the 2 makes the image bigger by X2)
        self.turretImage = pygame.transform.scale(self.turretImage, (self.turretWidth, self.turretHeight))
        self.outlineTurretImage = self.getOutline(self.turretImage, [0, 0, 0])
        self.turretImage.blit(self.outlineTurretImage, (0, 0))

        self.image = self.turretImage
        self.rect = self.turretImage.get_rect()
        self.rect.center = self.position

        self.ShootLeftGun = True

    def update(self, deltaTime, allSprites, turretSprites, enemySprites, projectileSprites):
        enemyToFollow = self.levelReference.GetClosestEnemyInRadius(self.position, self.range, enemySprites)

        if enemyToFollow is not None:

            self.posToFollow = enemyToFollow.position
            self.rotate()
            self.attackTimer += deltaTime

            if self.attackTimer > 1.8:

                if self.ShootLeftGun:
                    offset = Vector2(0, -34).rotate(self.direction)
                else:
                    offset = Vector2(0, 34).rotate(self.direction)

                posToShootFrom = Vector2(self.position.x, self.position.y) + offset  # Center of the sprite.
                self.shoot(posToShootFrom, allSprites, projectileSprites, enemyToFollow.position)

                self.ShootLeftGun = not self.ShootLeftGun
                self.attackTimer = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.isFocusedByUser:
            pygame.draw.circle(screen, [0, 0, 0], self.position, self.range, 2)

    def shoot(self, spawnPosition, allSprites, projectileSprites, posToGoTO):
        TntTurretDynamite(self.damage, self.throwVelocity, self.areaOfEffect, spawnPosition, posToGoTO, self.dynamiteImages, self.levelReference, allSprites, projectileSprites)

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



