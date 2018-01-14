import pygame

from SpaceInvaders.player.PlayerBullet import PlayerBullet
from Vector2 import Vector2


class Player(pygame.sprite.Sprite):

    def __init__(self, pos, *sprite_groups):
        super().__init__(*sprite_groups)

    # player image settings
        self.playerImageSize = 100
        self.playerImage = pygame.image.load("SpaceInvaders/images/Player.png").convert_alpha()
        self.playerImage = pygame.transform.scale(self.playerImage, (self.playerImageSize, self.playerImageSize))
        self.playerMask = pygame.mask.from_surface(self.playerImage)

    # Player settings
        self.speed = 500
        self.fireRateTimer = 0
        self.position = pos
        self.direction = 0  # What is the angle of this enemy(used for rotating)
        self.lives = 3

        self.hasDied = False

    # Image settings
        self.image = self.playerImage
        self.rect = self.playerImage.get_rect()
        self.rect.center = self.position

    def takeDamage(self):
        self.lives -= 1

    def getLives(self):
        return self.lives

    def die(self):
        pass
        #raise NotImplemented

        if self.hasDied is False:
            self.kill()
            self.hasDied = True

    def setAudio(self, audio):
        self.audio = audio

    def update(self, deltaTime, allSprites, enemySprites, playerSprites, bulletSprites, bossSprites):

        if self.hasDied is False:

            self.fireRateTimer += deltaTime

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                if self.fireRateTimer > 0.6:
                    posToShootFrom = Vector2(self.position.x, self.position.y)  # Center of the sprite.
                    self.shoot(posToShootFrom, allSprites, bulletSprites)
                    self.fireRateTimer = 0

            if pressed[pygame.K_LEFT]:
                if (self.position.x > (self.playerImageSize / 2)):  # Left border
                    self.position.x -= (self.speed * deltaTime)

            if pressed[pygame.K_RIGHT]:
                if (self.position.x < 1550):                        # Right border
                    self.position.x += (self.speed * deltaTime)

            self.rect = self.image.get_rect()  # Move image
            self.rect.center = self.position  # Move image

    def shoot(self, spawnPosition, allSprites, bulletSprites):
        bulletToShoot = PlayerBullet(spawnPosition, allSprites, bulletSprites)
        if self.audio == True:
            # Audio settings
            self.bulletSound = pygame.mixer.Sound("SpaceInvaders/audio/laser.ogg")
            self.bulletSound.play(0)