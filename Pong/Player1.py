import pygame
from Vector2 import Vector2

class Player1 (pygame.sprite.Sprite):
    def __init__(self, *sprite_groups):
        super().__init__(*sprite_groups)

        self.player1x = 30
        self.player1y = 330

        self.player1 = pygame.draw.rect(self.player1, [255, 255, 255], pygame.Rect(self.player1x, self.player1y, 30, 180))


    def update(self, deltaTime):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.player1y -= 500 * deltaTime
        if pressed[pygame.K_s]:
            self.player1y += 500 * deltaTime
        if self.player1y < 50:
            self.player1y = 50
        if self.player1y > 720:
            self.player1y = 720
