import pygame
import SceneManager
from ButtonClass import Button
from Vector2D import Vector2D

class Paddle (pygame.sprite.Sprite):

    def __init__(self, pos, *sprite_groups):
        super().__init__(*sprite_groups)
        #hoi
        self.position = Vector2D(800, 450)

        self.Paddle = pygame.Surface((50,50 )).convert_alpha()
        pygame.draw.rect(self.Paddle, [255, 255, 255], pygame.Rect(self.x, self.y, 240, 30))  # paddle

        self.velocityVector = Vector2D(-1000, 100)

        self.image = self.Paddle
        self.rect = self.Paddle.get_rect()
        self.rect.move_ip(self.position)


    def update(self, deltaTime):
        self.position += self.velocityVector * deltaTime
        self.rect.center = self.position

        if self.position.x <= 25:
            self.velocityVector = Vector2D(-self.velocityVector.x, self.velocityVector.y)
        if self.position.x >= 1575:
            self.velocityVector = Vector2D(-self.velocityVector.x, self.velocityVector.y)

        if self.position.y <= 25:
            self.velocityVector = Vector2D(-self.velocityVector.y, self.velocityVector.x)
        if self.position.y >= 875:
            self.velocityVector = Vector2D(-self.velocityVector.y, self.velocityVector.x)





