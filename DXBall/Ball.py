import pygame, math, random
import pygame.gfxdraw
from pygame.math import Vector2
import SceneManager
from DXBall.Paddle import Paddle
from DXBall.Block import Block

class Ball(pygame.sprite.Sprite):

    def __init__(self, pos, *sprite_groups):
        super().__init__(*sprite_groups)

        self.position = Vector2(305, 220)
        self.ballColor = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

        self.ballSurface = pygame.Surface((30, 30), pygame.SRCALPHA, 32)
        self.ballSurface = self.ballSurface.convert_alpha()
        pygame.gfxdraw.ellipse(self.ballSurface, self.ballColor, pygame.Rect(0, 0, 30, 30))  # ball

        self.xVel = 770
        self.yVel = 310

        self.image = self.ballSurface
        self.rect = self.ballSurface.get_rect()
        self.rect.topleft = (self.position.x, self.position.y)

    def draw(self, screen):
        pygame.draw.ellipse(self.ballSurface, self.ballColor, pygame.Rect(0, 0, 30, 30))
        screen.blit(self.image, self.rect)

    def update(self, deltaTime, allSprites, ballSprites, ballcollideSprites):

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

                self.ballColor = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

                if isinstance(ballCollideSprite, Paddle): # Ball has hit the paddle
                    pass
                if isinstance(ballCollideSprite, Block): # Ball has hit a block
                    ballCollideSprite.kill()  # Destroys the block that was hit
                break

        # Screen collision
        if self.rect.right > 1600:
            self.position.x = 1600 - self.rect.width
            self.xVel = -self.xVel
        if self.position.y > 900:
            pass
             #BALL IS BELOW SCREEN RESET THE BALL HERE
            self.position.y = 900 # sets the balls y position to 900
            self.yVel = -self.yVel
        if self.position.x < 0:
            self.position.x = 0
            self.xVel = -self.xVel
        if self.position.y < 70:
            self.position.y = 70
            self.yVel = -self.yVel

        self.position.x += self.xVel * deltaTime
        self.position.y += self.yVel * deltaTime
        self.rect.x = self.position.x
        self.rect.y = self.position.y








