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
        self.ball.fill((0, 0, 0))
        pygame.Surface.convert_alpha(self.ball)
        pygame.draw.ellipse(self.ball, [153, 255, 153], pygame.Rect(0, 0, 50, 50))  # ball

        # set velocity to x to -1000 and y to 100
        self.velocityVector = Vector2(-1000, 300)

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
        if self.position.y >= 750:
            self.velocityVector = self.velocityVector.reflect(Vector2(0, 1))



        for collidedSprite in pygame.sprite.spritecollide(self, ballcollideSprites, False):
            if self.rect.top <= collidedSprite.rect.bottom and self.rect.top >= collidedSprite.rect.bottom - 5:  # Moving up; Hit the bottom side of the wall
                print("collided with the bottom of paddle")

                self.velocityVector = self.velocityVector.reflect(Vector2(0, -1))

            elif self.rect.bottom >= collidedSprite.rect.top and self.rect.bottom <= collidedSprite.rect.top + 5:  # Moving up; Hit the bottom side of the wall
                print("collided with the top of paddle")

                self.velocityVector = self.velocityVector.reflect(Vector2(0, 1))

            elif self.rect.left <= collidedSprite.rect.right and self.rect.left <= collidedSprite.rect.right + 10:
                print("collided with the right of paddle")

                self.velocityVector = self.velocityVector.reflect(Vector2(-1, 0))

            elif self.rect.right >= collidedSprite.rect.left and self.rect.right >= collidedSprite.rect.left - 10:
                print("collided with the left of paddle")

                self.velocityVector = self.velocityVector.reflect(Vector2(1, 0))

        self.position += self.velocityVector * deltaTime
        self.rect.center = self.position