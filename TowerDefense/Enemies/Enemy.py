import pygame
from pygame import gfxdraw
from Vector2D import Vector2D

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.name = "Base Turret Test"
        self.position = Vector2D(0, 0)
        self.direction = 0 # What is the angle of this enemy(used for rotating)