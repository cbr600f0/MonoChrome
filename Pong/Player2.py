import pygame
from Vector2 import Vector2

class Player2 (pygame.sprite.Sprite):
    def __init__(self, *sprite_groups):
        super().__init__(*sprite_groups)

        self.x = 1540
        self.y = 420

        self.player2Surface = pygame.Surface((30, 180)).convert_alpha()
        self.player2Surface.fill((255, 255, 255))

        self.image = self.player2Surface
        self.rect = self.player2Surface.get_rect()
        self.rect.center = Vector2(self.x, self.y)


    def update(self, deltaTime, ballcollideSprites):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.y -= 500 * deltaTime
        if pressed[pygame.K_DOWN]:
            self.y += 500 * deltaTime
        if self.y < 140:
            self.y = 140
        if self.y > 810:
            self.y = 810
        self.rect.center = Vector2(self.x, self.y)
