import pygame, random
from random import randint
from Vector2 import Vector2
from SpaceInvaders.enemy.EnemyBullet import EnemyBullet

class Enemy(pygame.sprite.Sprite):

    def __init__(self, pos, image, *sprite_groups):
        super().__init__(*sprite_groups)

        self.enemyImage1 = pygame.image.load("SpaceInvaders/images/Enemy1.png").convert_alpha()
        self.enemyImage1 = pygame.transform.scale(self.enemyImage1, (50, 50))
        self.enemyMask = pygame.mask.from_surface(self.enemyImage1)

        self.enemyImage2 = pygame.image.load("SpaceInvaders/images/Enemy2.png").convert_alpha()
        self.enemyImage2 = pygame.transform.scale(self.enemyImage2, (50, 50))
        self.enemyImage3 = pygame.image.load("SpaceInvaders/images/Enemy3.png").convert_alpha()
        self.enemyImage3 = pygame.transform.scale(self.enemyImage3, (50, 50))
        self.enemyImage4 = pygame.image.load("SpaceInvaders/images/Enemy4.png").convert_alpha()
        self.enemyImage4 = pygame.transform.scale(self.enemyImage4, (50, 50))
        self.enemyImage5 = pygame.image.load("SpaceInvaders/images/Enemy5.png").convert_alpha()
        self.enemyImage5 = pygame.transform.scale(self.enemyImage5, (50, 50))

        self.position = pos
        self.direction = 0  # What is the angle of this enemy(used for rotating)

        self.movementSideways = 21
        self.movementDirectionToRight = True
        self.movementDownwardsMax = 9

        self.movementTimer = 0

        self.hasDied = False

        if image == 0:
            self.image = self.enemyImage1
            self.rect = self.enemyImage1.get_rect()
        elif image == 1:
            self.image = self.enemyImage2
            self.rect = self.enemyImage2.get_rect()
        elif image == 2:
            self.image = self.enemyImage3
            self.rect = self.enemyImage3.get_rect()
        elif image == 3:
            self.image = self.enemyImage4
            self.rect = self.enemyImage4.get_rect()
        elif image == 4:
            self.image = self.enemyImage5
            self.rect = self.enemyImage5.get_rect()

        self.rect.center = self.position

    def die(self):
        if self.hasDied is False:
            self.kill()
            self.hasDied = True

    def update(self, deltaTime, allSprites, enemySprites, playerSprites, bulletSprites):

        if self.hasDied is False:

            # add Timer
            self.movementTimer += deltaTime

            # Timer
            if self.movementTimer >= 1:

                if randint(1, 50) == 1:
                    posToShootFrom = Vector2(self.position.x, self.position.y)  # Center of the sprite.
                    self.shoot(posToShootFrom, allSprites, bulletSprites)

                if self.movementSideways > 0:

                    if self.movementDirectionToRight:
                        self.position += Vector2(50, 0)
                    else:
                        self.position -= Vector2(50, 0)

                    self.movementSideways -= 1
                else:
                    if self.movementDownwardsMax > 0:
                        self.position += Vector2(0, 50)

                        self.movementDirectionToRight = not self.movementDirectionToRight
                        self.movementSideways = 21
                        self.movementDownwardsMax -= 1
                    else:
                        # Game Over
                        pass

                self.rect = self.image.get_rect()   # Move image
                self.rect.center = self.position    # Move image
                self.movementTimer = 0

    def shoot(self, spawnPosition, allSprites, bulletSprites):
        bulletToShoot = EnemyBullet(spawnPosition, allSprites, bulletSprites)
