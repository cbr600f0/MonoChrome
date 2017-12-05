import pygame
import SceneManager
from ButtonClass import Button
from Vector2D import Vector2D

class Ball (pygame.sprite.Sprite):

    def __init__(self, pos, *sprite_groups):
        super().__init__(*sprite_groups)

        self.position = Vector2D(800, 450)

        self.enemyImage = pygame.Surface((50,50 )).convert_alpha()
        pygame.draw.ellipse(self.enemyImage, [153, 255, 153], pygame.Rect(0, 0, 50, 50))  # ball

        self.velocityVector = Vector2D(-1000, 100)

        self.image = self.enemyImage
        self.rect = self.enemyImage.get_rect()
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





