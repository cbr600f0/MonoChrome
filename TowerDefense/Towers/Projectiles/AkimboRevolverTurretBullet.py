import pygame
from Vector2D import Vector2D


class AkimboRevolverTurretBullet(pygame.sprite.Sprite):

    def __init__(self, pos, enemyToFollow, *sprite_groups):
        super().__init__(*sprite_groups)

        self.position = Vector2D(pos)
        self.velocity = 600
        self.damage = 50
        self.direction = 0

        self.bulletImage = pygame.Surface((8, 14)).convert_alpha()
        self.bulletImage.fill((0, 0, 0))
        self.bulletMask = pygame.mask.from_surface(self.bulletImage)

        self.image = self.bulletImage
        self.enemyToFollow = enemyToFollow
        self.rect = self.image.get_rect()

    def update(self, deltaTime, allSprites, turretSprites, enemySprites, projectileSprites):

        if self.enemyToFollow is not None:

            #  Move towards enemy
            moveToPositionVector = self.enemyToFollow.position - self.position

            if self.position.get_distance(self.enemyToFollow.position) > 0:
                moveToPositionVector.length = 1

            if moveToPositionVector.length > self.enemyToFollow.position.get_distance(self.position):
                moveToPositionVector.length = self.enemyToFollow.position.get_distance(self.position)

            self.position += moveToPositionVector * self.velocity * deltaTime
            self.rotate()

            if pygame.sprite.collide_mask(self, self.enemyToFollow):
                self.enemyToFollow.takeDamage(self.damage)
                self.kill()

    def rotate(self):

        #  Move towards PosToFollow
        posToFollowLookAt = self.enemyToFollow.position - self.position
        self.direction = -posToFollowLookAt.angle - 90
        self.image = pygame.transform.rotozoom(self.bulletImage, self.direction, 1)  # the image is rotated the wrong way so the plus 90 fixed this
        self.rect = self.image.get_rect()
        self.rect.center = self.position