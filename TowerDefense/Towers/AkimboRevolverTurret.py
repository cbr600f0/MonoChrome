import pygame, math
from TowerDefense.Towers.Turret import Turret
from TowerDefense.Towers.Projectiles.AkimboRevolverTurretBullet import AkimboRevolverTurretBullet as Bullet
from pygame.math import Vector2 as Vector2

class AkimboRevolverTurret(Turret):

    def __init__(self, pos, levelReference, *sprite_groups):
        Turret.__init__(self, pos, *sprite_groups)

        self.bulletTimer = 0
        self.levelReference = levelReference
        self.posToFollow = Vector2(0, 0)
        self.turretWidth = 48
        self.turretHeight = 98
        self.range = 280

        self.turretImage = pygame.image.load("TowerDefense\Images\Turrets\AkimboRevolverTurret.png").convert_alpha()
        self.turretImage = pygame.transform.scale(self.turretImage, (self.turretWidth, self.turretHeight))

        self.outlineTurretImage = self.getOutline(self.turretImage, [0, 0, 0])
        self.turretImage.blit(self.outlineTurretImage, (0, 0))

        self.image = self.turretImage
        self.rect = self.turretImage.get_rect()
        self.rect.center = self.position

        self.ShootLeftGun = True

    def update(self, deltaTime, allSprites, turretSprites, enemySprites, projectileSprites):
        enemyToShoot = self.levelReference.GetClosestEnemyInRadius(self.position, self.range, enemySprites)

        if enemyToShoot is not None:

            self.posToFollow = enemyToShoot.position
            self.rotate()
            self.bulletTimer += deltaTime

            if self.bulletTimer > 0.5:

                if self.ShootLeftGun:
                    offset = Vector2(48, -14).rotate(self.direction)
                else:
                    offset = Vector2(48, 14).rotate(self.direction)

                posToShootFrom = Vector2(self.position.x, self.position.y) + offset  # Center of the sprite.
                self.shoot(posToShootFrom, allSprites, projectileSprites, enemyToShoot)

                self.ShootLeftGun = not self.ShootLeftGun
                self.bulletTimer = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.isFocusedByUser:
            pygame.draw.circle(screen, [0, 0, 0], self.position, self.range, 2)

    def shoot(self, spawnPosition, allSprites, projectileSprites, enemyToFollow):
        Bullet(spawnPosition, enemyToFollow, allSprites, projectileSprites)

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




