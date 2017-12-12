import pygame
import SceneManager
from ButtonClass import Button
from Vector2 import Vector2

class Paddle (pygame.sprite.Sprite):

    def __init__(self, *sprite_groups):
        super().__init__(*sprite_groups)

        self.x = 800  # player
        self.y = 400  # player

        self.paddleSurface = pygame.Surface((240, 30)).convert_alpha()
        self.paddleSurface.fill((255, 255, 255))
        #pygame.draw.rect(self.paddleSurface, [255, 255, 255], pygame.Rect(self.x, self.y, 240, 30))  # paddle

        self.image = self.paddleSurface
        self.rect = self.paddleSurface.get_rect()
        self.rect.center = Vector2(self.x, self.y)


    def update(self, deltaTime, allSprites, ballSprites, ballcollideSprites):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            self.x += 950 * deltaTime
        if pressed[pygame.K_LEFT]:
            self.x -= 950 * deltaTime
        if self.x <= 120:
            self.x = 120
        if self.x >= 1480:
            self.x = 1480
        self.rect.center = Vector2(self.x, self.y)