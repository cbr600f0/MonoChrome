import pygame
from Vector2 import Vector2

class Player1 (pygame.sprite.Sprite):
    def __init__(self, *sprite_groups):
        super().__init__(*sprite_groups)

        self.x = 30
        self.y = 330

        self.player1Surface = pygame.Surface((50, 50)).convert_alpha()
        pygame.draw.rect(self.player1Surface, [255, 255, 255], pygame.Rect(self.x, self.y, 30, 180))

        self.image = self.player1Surface
        self.rect = self.player1Surface.get_rect()
        self.rect.center = Vector2(self.x, self.y)


    def update(self, deltaTime):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.y -= 500 * deltaTime
        if pressed[pygame.K_s]:
            self.y += 500 * deltaTime
        if self.y < 50:
            self.y = 50
        if self.y > 720:
            self.y = 720

        self.rect = self.player1Surface.get_rect()
        self.rect.center = Vector2(self.x, self.y)
