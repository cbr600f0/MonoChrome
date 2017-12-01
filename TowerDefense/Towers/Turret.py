import pygame
from pygame import gfxdraw
from Vector2D import Vector2D

class Turret(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.turretName = "Base Turret Test"
        self.position = Vector2D(800, 450)
        self.direction = 0 # What is the angle of this turret(Used for rotating the turret)