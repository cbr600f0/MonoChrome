import pygame, math
from TowerDefense.Towers.Turret import Turret
from TowerDefense.Towers.Projectiles.SniperBullet import SniperBullet as Bullet
from pygame.math import Vector2 as Vector2


class SniperTurret(Turret):

    def __init__(self, pos, levelReference, *sprite_groups):
        Turret.__init__(self, pos, levelReference, *sprite_groups)

        self.bulletTimer = 0
        self.posToFollow = Vector2(0, 0)
        self.turretWidth = 50
        self.turretHeight = 98

        self.damage = 40
        self.nextLevelDamage = 80

        self.fireRate = 0.35 # shots per second
        self.nextLevelFireRate = 0.4

        self.range = 300
        self.nextLevelRange = 320

        self.name = "Rifle Cowboy"
        self.description = "A cowboy with his rifle, deals massive damage with high range at the cost of firerate."

        self.upgradeCost = 350
        self.buyPrice = 250
        self.totalGoldSpendOnTurret = self.buyPrice

        self.turretImage = pygame.image.load("TowerDefense\Images\Turrets\SniperTurret.png").convert_alpha()
        self.turretImage = pygame.transform.scale(self.turretImage, (self.turretWidth, self.turretHeight))

        self.outlineTurretImage = self.getOutline(self.turretImage, [0, 0, 0])
        self.turretImage.blit(self.outlineTurretImage, (0, 0))

        self.image = self.turretImage
        self.rect = self.turretImage.get_rect()
        self.rect.center = self.position

        self.collisionRect = pygame.Rect(self.rect.x, self.rect.y, self.turretWidth, self.turretHeight)

        self.gunShotSound = pygame.mixer.Sound("TowerDefense/Sounds/sniperGunshot.wav")
        self.gunShotSound.set_volume(0.010)

        self.offset = Vector2(50, 14).rotate(self.direction)

    def update(self, deltaTime):
        if not self.isUpgrading:
            enemyToShoot = self.levelReference.GetClosestEnemyToDestination(self.position, self.range, self.levelReference.enemySprites)

            if enemyToShoot is not None:

                self.posToFollow = enemyToShoot.position
                self.rotate()
                self.bulletTimer += deltaTime

                if self.bulletTimer > 1 / self.fireRate:
                    self.gunShotSound.play()

                    try:
                        self.offset = Vector2(50, 14).rotate(self.direction)
                    except:
                        self.offset = Vector2(0, 0)

                    posToShootFrom = Vector2(self.position.x, self.position.y) + self.offset
                    self.shoot(posToShootFrom, enemyToShoot)

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
            self.nextLevelRange = 340
            self.nextLevelFireRate = 0.45

            self.nextLevelUpgradeCost = 480
            self.upgradeCost = 620

        elif self.turretLevel == 3:
            self.nextLevelDamage = 400
            self.nextLevelFireRate = 0.5

            self.nextLevelRange = 370
            self.upgradeCost = 1000




