import pygame
from Vector2 import Vector2

class Block (pygame.sprite.Sprite):
    def __init__(self, x, y, *sprite_groups):
        super().__init__(*sprite_groups)

        self.x = x
        self.y = y

        self.player1Surface = pygame.Surface((50, 250)).convert_alpha()
        self.player1Surface.fill((255, 255, 255))

        self.image = self.player1Surface
        self.rect = self.player1Surface.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


    def update(self, deltaTime, ballcollideSprites):
        self.rect.x = self.x
        self.rect.y = self.y
