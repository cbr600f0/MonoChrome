import pygame
from pygame import gfxdraw
from Vector2 import Vector2

class Turret(pygame.sprite.Sprite):

    def __init__(self, pos, *sprite_groups):
        super().__init__(*sprite_groups)

        self.name = "Base Turret"
        self.position = pos
        self.direction = 0 # What is the angle of this turret(Used for rotating the turret)
        self.range = 200