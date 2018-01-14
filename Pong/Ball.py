import pygame, math
from pygame.math import Vector2
import SceneManager
from DXBall.Paddle import Paddle
from Pong.Player1 import Player1
from Pong.Player2 import Player2
from Pong.Block import Block

class Ball(pygame.sprite.Sprite):

    def __init__(self, *sprite_groups):
        super().__init__(*sprite_groups)

        self.position = Vector2(720, 390)

        self.width = 60
        self.height = 60

        self.ballSurface = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)
        self.ballSurface = self.ballSurface.convert_alpha()
        pygame.draw.ellipse(self.ballSurface, [255, 255, 255], pygame.Rect(0, 0, self.width, self.height))  # ball

        self.baseVelocity = 100
        self.currentVelocity = self.baseVelocity

        self.xVel = 8 # How fast is the ball going on the X-Axis (Left or Right)
        self.yVel = 3 # How fast is the ball going on the Y-Axis (Up or Down)

        self.image = self.ballSurface
        self.rect = self.ballSurface.get_rect()
        self.rect.topleft = (self.position.x, self.position.y)

    def update(self, deltaTime, ballcollideSprites):

        self.rect = pygame.Rect(self.rect)
        for ballCollideSprite in ballcollideSprites.sprites():
            if self.rect.colliderect(ballCollideSprite.rect):
                # where are we in comparison to this object?
                if ballCollideSprite.rect.collidepoint(self.rect.topleft):
                    # upper left corner is in
                    if ballCollideSprite.rect.collidepoint(self.rect.topright):
                        # top edge is in, move down by overlap
                        self.position.y = ballCollideSprite.rect.bottom
                        self.yVel = -self.yVel
                    elif ballCollideSprite.rect.collidepoint(self.rect.bottomleft):
                        # left edge is in, move right by overlap
                        self.position.x = ballCollideSprite.rect.right
                        self.xVel = abs(self.xVel) # abs stands for absolute value Example abs(-100) returns 100
                    else:
                        # no edge in. (at least on this side)
                        # find the overlap for x and y
                        ovx = abs(self.position.x - ballCollideSprite.rect.right)
                        ovy = abs(self.position.y - ballCollideSprite.rect.bottom)
                        if ovx >= ovy:  # came from bottom
                            self.position.y = ballCollideSprite.rect.bottom
                            self.yVel = -self.yVel
                        else:  # came from right
                            self.position.x = ballCollideSprite.rect.right
                            self.xVel = abs(self.xVel)
                elif ballCollideSprite.rect.collidepoint(self.rect.topright):
                    # upper right corner is in
                    if ballCollideSprite.rect.collidepoint(self.rect.bottomright):
                        # right edge is in, move left by overlap
                        self.position.x = ballCollideSprite.rect.left - self.rect.width
                        self.xVel = -abs(self.xVel)
                    else:
                        # no edge is in. (at least on this side)
                        # find the overlap for x and y
                        ovx = abs(self.rect.right - ballCollideSprite.rect.left)
                        ovy = abs(self.position.y - ballCollideSprite.rect.bottom)
                        if ovx >= ovy:  # came from bottom
                            self.position.y = ballCollideSprite.rect.bottom
                            self.yVel = -self.yVel
                        else:  # came from left
                            self.position.x = ballCollideSprite.rect.left - self.rect.width
                            self.xVel = -abs(self.xVel)
                elif ballCollideSprite.rect.collidepoint(self.rect.bottomright):
                    # bottom right corner is in
                    if ballCollideSprite.rect.collidepoint(self.rect.bottomleft):
                        # bottom edge is in
                        self.position.y = ballCollideSprite.rect.top - self.rect.height
                        self.yVel = -self.yVel
                    else:
                        # no edge is in. (at least on this side)
                        # find the overlap for x and y
                        ovx = abs(self.position.x - ballCollideSprite.rect.left - self.rect.width)
                        ovy = abs(self.position.y - ballCollideSprite.rect.top - self.rect.height)
                        if ovx <= ovy:  # came from top
                            self.position.y = ballCollideSprite.rect.top - self.rect.height
                            self.yVel = -self.yVel
                        else:  # came from left
                            self.position.x = ballCollideSprite.rect.left - self.rect.width
                            self.xVel = -abs(self.xVel)
                elif ballCollideSprite.rect.collidepoint(self.rect.bottomleft):
                    # bottom left corner is in
                    # we have eliminiated all sides
                    # find the overlap for x and y
                    ovx = abs(self.position.x - ballCollideSprite.rect.right)
                    ovy = abs(self.rect.bottom - ballCollideSprite.rect.top)
                    if ovx >= ovy:  # came from top
                        self.position.y = ballCollideSprite.rect.top - self.rect.height
                        self.yVel = -self.yVel
                    elif ovx < ovy:  # came from right
                        self.position.x = ballCollideSprite.rect.right
                        self.xVel = abs(self.xVel)

                if isinstance(ballCollideSprite, Player1): # Ball has hit the paddle
                    self.currentVelocity += 10
                    pass
                if isinstance(ballCollideSprite, Player2): # Ball has hit the paddle
                    self.currentVelocity += 10
                    pass
                if isinstance(ballCollideSprite, Block): # Ball has hit a block
                    self.currentVelocity += 20  # Destroys the block that was hit
                pass

        # Screen collision

        if self.position.y > 900 - self.height:
            pass
             #BALL IS BELOW SCREEN RESET THE BALL HERE
            self.position.y = 900 - self.height # sets the balls y position to 900
            self.yVel = -self.yVel

        if self.position.y < 60:
            self.position.y = 60
            self.yVel = -self.yVel

        self.position.x += self.xVel * (self.currentVelocity * deltaTime)
        self.position.y += self.yVel * (self.currentVelocity * deltaTime)
        self.rect.x = self.position.x
        self.rect.y = self.position.y










