import pygame
from pygame.math import Vector2
import SceneManager
from ButtonClass import Button
from DXBall.Paddle import Paddle

class Ball(pygame.sprite.Sprite):

    def __init__(self, pos, *sprite_groups):
        super().__init__(*sprite_groups)
        self.position = Vector2(800, 450)

        self.ball = pygame.Surface((50, 50)).convert_alpha()
        pygame.draw.ellipse(self.ball, [153, 255, 153], pygame.Rect(0, 0, 50, 50))  # ball

        self.velocityVector = Vector2(-1000, 100)

        self.image = self.ball
        self.rect = self.ball.get_rect()
        self.rect.move_ip(self.position)


    def update(self, deltaTime):
        self.position += self.velocityVector * deltaTime
        self.rect.center = self.position

        if self.position.x <= 25:
            self.velocityVector = self.velocityVector.reflect(Vector2(-1, 0))
        if self.position.x >= 1575:
            self.velocityVector = self.velocityVector.reflect(Vector2(1, 0))

        if self.position.y <= 25:
            self.velocityVector = self.velocityVector.reflect(Vector2(0, -1))
        if self.position.y >= 875:
            self.velocityVector = self.velocityVector.reflect(Vector2(0, 1))

