import pygame
from Vector2 import Vector2

class Player2 (pygame.sprite.Sprite):
    def __init__(self, *sprite_groups):
        super().__init__(*sprite_groups)

        self.player2x = 1540
        self.player2y = 330

        self.player2 = pygame.draw.rect(self.player2, [255, 255, 255], pygame.Rect(self.player2x, self.player2y, 30, 180))


    def update(self, deltaTime):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.player2y -= 500 * deltaTime
        if pressed[pygame.K_DOWN]:
            self.player2y += 500 * deltaTime
        if self.player2y < 50:
            self.player2y = 50
        if self.player2y > 720:
            self.player2y = 720
