import pygame
from Vector2 import Vector2

class Player1 (pygame.sprite.Sprite):
    def __init__(self, *sprite_groups):
        super().__init__(*sprite_groups)

        self.x = 60
        self.y = 420

        self.player1Surface = pygame.Surface((30, 180)).convert_alpha()
        self.player1Surface.fill((255, 255, 255))

        self.image = self.player1Surface
        self.rect = self.player1Surface.get_rect()
        self.rect.center = Vector2(self.x, self.y)


    def update(self, deltaTime):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.y -= 500 * deltaTime
        if pressed[pygame.K_s]:
            self.y += 500 * deltaTime
        if self.y < 140:
            self.y = 140
        if self.y > 810:
            self.y = 810
        self.rect.center = Vector2(self.x, self.y)
