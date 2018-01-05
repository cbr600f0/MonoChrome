import pygame
from Vector2 import Vector2


class AkimboRevolverTurretBullet(pygame.sprite.Sprite):

    def __init__(self, pos, damage, enemyToFollow, *sprite_groups):
        super().__init__(*sprite_groups)

        self.enemyToFollow = enemyToFollow

        self.position = Vector2(pos)

        self.velocity = 600
        self.damage = damage
        self.direction = 0

        self.bulletImage = pygame.Surface((4, 6)).convert_alpha()
        self.bulletImage.fill((0, 0, 0))

        self.bulletMask = pygame.mask.from_surface(self.bulletImage)

        self.image = self.bulletImage
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def update(self, deltaTime):

        if self.enemyToFollow is not None:

            #  Move towards enemy
            moveToPositionVector = self.enemyToFollow.position - self.position
            moveToPositionVector.length = self.velocity * deltaTime

            if moveToPositionVector.length > self.enemyToFollow.position.get_distance(self.position):
                moveToPositionVector.length = self.enemyToFollow.position.get_distance(self.position)

            self.position += moveToPositionVector
            self.rotate()

            if pygame.sprite.collide_mask(self, self.enemyToFollow):
                self.enemyToFollow.takeDamage(self.damage)
                self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def rotate(self):

        #  Move towards PosToFollow
        posToFollowLookAt = self.enemyToFollow.position - self.position
        self.direction = -posToFollowLookAt.angle - 90
        self.image = pygame.transform.rotozoom(self.bulletImage, self.direction, 1)  # the image is rotated the wrong way so the plus 90 fixed this
        self.rect = self.image.get_rect()
        self.rect.center = self.position