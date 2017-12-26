import pygame
from pygame.math import Vector2
import SceneManager
from ButtonClass import Button
from DXBall.Paddle import Paddle

class Ball(pygame.sprite.Sprite):

    def __init__(self, pos, *sprite_groups):
        super().__init__(*sprite_groups)

        self.position = Vector2(750, 400)

        self.ball = pygame.Surface((50, 50))
        self.ball = self.ball.convert_alpha()
        pygame.draw.ellipse(self.ball, [153, 255, 153], pygame.Rect(0, 0, 50, 50))  # ball

        # set velocity to x to -1000 and y to 100
        self.velocityVector = Vector2(-800, 300)

        self.image = self.ball
        self.rect = self.ball.get_rect()
        self.rect.center = self.position


    def update(self, deltaTime, allSprites, ballSprites, ballcollideSprites):

        if self.position.x <= 25:
            self.velocityVector = self.velocityVector.reflect(Vector2(-1, 0))
        if self.position.x >= 1575:
            self.velocityVector = self.velocityVector.reflect(Vector2(1, 0))

        if self.position.y <= 90:
            self.velocityVector = self.velocityVector.reflect(Vector2(0, -1))
        if self.position.y >= 850:
            #self.velocityVector = Vector2(0, 600)
            self.position.x = 800
            self.position.y = 450


        collidedSprite = pygame.sprite.spritecollideany(self, ballcollideSprites)
        if collidedSprite is not None:
            if isinstance(collidedSprite, Paddle):
                self.velocityVector = self.velocityVector.reflect(Vector2(0, -1))
                pass
            else:
                self.velocityVector = self.velocityVector.reflect(Vector2(0, -1))
                collidedSprite.kill()

        self.position += self.velocityVector * deltaTime
        self.rect.center = self.position