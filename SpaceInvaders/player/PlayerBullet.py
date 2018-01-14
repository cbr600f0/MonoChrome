import pygame
from Vector2 import Vector2

class PlayerBullet(pygame.sprite.Sprite):

    def __init__(self, pos, *sprite_groups):
        super().__init__(*sprite_groups)

    # Bullet image set
        self.playerBulletImage = pygame.image.load("SpaceInvaders/images/Bullet_Player.png").convert_alpha()
        self.playerBulletImage = pygame.transform.scale(self.playerBulletImage, (8, 23))
        self.bulletMask = pygame.mask.from_surface(self.playerBulletImage)

    # Bullet settings
        self.speed = 500
        self.damage = 100
        self.position = pos
        self.direction = 0  # What is the angle of this enemy(used for rotating)

    # image settings
        self.image = self.playerBulletImage
        self.rect = self.playerBulletImage.get_rect()
        self.rect.center = self.position

    def update(self, deltaTime, allSprites, enemySprites, playerSprites, bulletSprites, bossSprites):

        self.position.y -= (self.speed * deltaTime)

    # outside screen
        if self.position.y < -4:
            self.kill()

        # Update image
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        # Collision
        for enemyHit in pygame.sprite.spritecollide(self, enemySprites, False):
            enemyHit.die()
            self.kill()

        for bossSettings in pygame.sprite.RenderUpdates(bossSprites):
            self.boss = bossSettings.getBoss()

            if pygame.sprite.collide_mask(self, self.boss):
                bossSettings.takeDamage()
                self.kill()
