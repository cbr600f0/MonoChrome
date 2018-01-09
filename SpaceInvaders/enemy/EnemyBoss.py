import pygame, random
from random import randint
from Vector2 import Vector2
from SpaceInvaders.enemy.EnemyBullet import EnemyBullet

class EnemyBoss(pygame.sprite.Sprite):

    def __init__(self, pos, *sprite_groups):
        super().__init__(*sprite_groups)

        self.enemyImage = pygame.image.load("SpaceInvaders/images/Enemy5.png").convert_alpha()
        self.enemyImage = pygame.transform.scale(self.enemyImage, (450, 450))
        self.enemyMask = pygame.mask.from_surface(self.enemyImage)

        self.position = pos
        self.direction = 0  # What is the angle of this enemy(used for rotating)

        self.movementSideways = 0
        self.movementDirectionToRight = True
        self.movementDownwardsMax = 0

        self.timer = 0

        # Lives + Wave x 50
        self.health = 10
        self.originalHealth = self.health
        self.random = 0

        self.hasDied = False
        self.lastRow = False

        self.image = self.enemyImage
        self.rect = self.enemyImage.get_rect()
        self.rect.center = self.position

    def die(self):
        if self.hasDied is False:
            self.kill()
            self.hasDied = True

    def takeDamage(self):
        if self.hasDied is False:
            if self.health > 0:
                self.health -= 1
            else:
                self.die()

    def getLives(self):
        return self.health

    def getOriginalLives(self):
        return self.originalHealth

    def getBoss(self):
        return self

    def update(self, deltaTime, allSprites, enemySprites, playerSprites, bulletSprites, bossSprites):

        if self.hasDied is False:

            # add Timer
            self.timer += deltaTime

            # Shoot timer
            if self.timer >= 0.35:
                if randint(1, 25) == 1:
                    posToShootFrom = Vector2(self.position.x - 40, self.position.y - 100)  # Center of the sprite.
                    self.shoot(posToShootFrom, allSprites, bulletSprites)

                    posToShootFrom = Vector2(self.position.x - 20, self.position.y - 50)  # Center of the sprite.
                    self.shoot(posToShootFrom, allSprites, bulletSprites)

                    posToShootFrom = Vector2(self.position.x, self.position.y)  # Center of the sprite.
                    self.shoot(posToShootFrom, allSprites, bulletSprites)

                    posToShootFrom = Vector2(self.position.x + 20, self.position.y - 50)  # Center of the sprite.
                    self.shoot(posToShootFrom, allSprites, bulletSprites)

                    posToShootFrom = Vector2(self.position.x + 40, self.position.y - 100)  # Center of the sprite.
                    self.shoot(posToShootFrom, allSprites, bulletSprites)

            # Move timer
            if self.timer >= 0.5:
                self.random = random.randint(1, 25)
                if random.randint(1, 100) < 50:
                    if self.movementSideways <= 50:
                        self.position += Vector2(self.random, 0)
                        self.movementSideways += 1
                    else:
                        self.position -= Vector2(self.random, 0)
                        self.movementSideways -= 1
                else:
                    if self.movementSideways >= -50:
                        self.position -= Vector2(self.random, 0)
                        self.movementSideways -= 1
                    else:
                        self.position += Vector2(self.random, 0)
                        self.movementSideways += 1

                self.rect = self.image.get_rect()   # Move image
                self.rect.center = self.position    # Move image
                self.timer = 0

    def shoot(self, spawnPosition, allSprites, bulletSprites):
        EnemyBullet(spawnPosition, allSprites, bulletSprites)
