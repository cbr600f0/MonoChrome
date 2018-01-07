import pygame, math, random
from TowerDefense.Towers.Turret import Turret
from TowerDefense.Towers.Projectiles.AkimboRevolverTurretBullet import AkimboRevolverTurretBullet as Bullet
from pygame.math import Vector2 as Vector2

class AkimboRevolverTurret(Turret):

    def __init__(self, pos, levelReference, *sprite_groups):
        Turret.__init__(self, pos, levelReference, *sprite_groups)

        self.bulletTimer = 0
        self.posToFollow = Vector2(0, 0)
        self.turretWidth = 48
        self.turretHeight = 98

        self.damage = 1
        self.nextLevelDamage = 90

        self.fireRate = 30.3 # shots per second
        self.nextLevelFireRate = 1.5

        self.range = 1800
        self.nextLevelRange = 200

        self.name = "Akimbo Cowboy"
        self.description = "A cowboy with 2 revolvers, shoots fast with short range and medium damage."

        self.upgradeCost = 120
        self.buyPrice = 100
        self.totalGoldSpendOnTurret = self.buyPrice

        self.turretImage = pygame.image.load("TowerDefense\Images\Turrets\AkimboRevolverTurret.png").convert_alpha()
        self.turretImage = pygame.transform.scale(self.turretImage, (self.turretWidth, self.turretHeight))

        self.outlineTurretImage = self.getOutline(self.turretImage, [0, 0, 0])
        self.turretImage.blit(self.outlineTurretImage, (0, 0))

        self.image = self.turretImage
        self.rect = self.turretImage.get_rect()
        self.rect.center = self.position

        self.ShootLeftGun = True

        self.collisionRect = pygame.Rect(self.rect.x, self.rect.y, self.turretWidth, self.turretHeight)

        self.gunShotSound = pygame.mixer.Sound("TowerDefense/Sounds/revolverShot.wav")
        self.gunShotSound.set_volume(0.009)

    def update(self, deltaTime):
        if not self.isUpgrading:
            enemyToShoot = self.levelReference.GetClosestEnemyInRadius(self.position, self.range, self.levelReference.enemySprites)
            if enemyToShoot is not None:

                self.posToFollow = enemyToShoot.position
                self.rotate()
                self.bulletTimer += deltaTime

                if self.bulletTimer > 1 / self.fireRate:
                    self.gunShotSound.play()

                    if self.ShootLeftGun: # ERROR Offset can give you an error check THIS!!
                        offset = Vector2(48, -14).rotate(self.direction)
                    else:
                        offset = Vector2(48, 14).rotate(self.direction)

                    posToShootFrom = Vector2(self.position.x, self.position.y) + offset  # Center of the sprite.
                    self.shoot(posToShootFrom, enemyToShoot)

                    self.ShootLeftGun = not self.ShootLeftGun
                    self.bulletTimer = 0
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

    def shoot(self, spawnPosition, enemyToFollow):
        Bullet(spawnPosition, self.damage, enemyToFollow, self.levelReference.allSprites, self.levelReference.projectileSprites)

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

        if self.turretLevel == 2:
            self.nextLevelDamage = 160
            self.nextLevelFireRate = 1.9
            self.nextLevelRange = 250
            self.nextLevelUpgradeCost = 250
            self.upgradeCost = 350

        elif self.turretLevel == 3:
            self.nextLevelDamage = 130
            self.nextLevelFireRate = 3.1
            self.nextLevelRange = 330
            self.upgradeCost = 600




