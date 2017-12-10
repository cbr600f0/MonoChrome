import pygame
import SceneManager
from ButtonClass import Button
from Vector2 import Vector2

class Ball (pygame.sprite.Sprite):
    def __init__(self, pos, *sprite_groups):
        super().__init__(*sprite_groups)

        self.position = Vector2(800, 450)

        self.ball = pygame.Surface((50, 50)).convert_alpha()
        pygame.draw.rect(self.ball, [255, 255, 255], pygame.Rect(0, 0, 60, 60))

        self.velocityVector = Vector2(-1000, 100)

        self.image = self.ball
        self.rect = self.ball.get_rect()
        self.rect.move_ip(self.position)


    def update(self, deltaTime):
        self.position += self.velocityVector * deltaTime
        self.rect.center = self.position

        if self.position.x <= 25:
            self.velocityVector = Vector2(-self.velocityVector.x, self.velocityVector.y)
        if self.position.x >= 1575:
            self.velocityVector = Vector2(-self.velocityVector.x, self.velocityVector.y)

        if self.position.y <= 25:
            self.velocityVector = Vector2(-self.velocityVector.y, self.velocityVector.x)
        if self.position.y >= 875:
            self.velocityVector = Vector2(-self.velocityVector.y, self.velocityVector.x)