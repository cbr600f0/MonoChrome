import pygame
from Vector2D import Vector2D

class Enemy(pygame.sprite.Sprite):

    def __init__(self, pos, *sprite_groups):
        super().__init__(*sprite_groups)

        self.name = "Base Enemy"
        self.position = pos
        self.direction = 0 # What is the angle of this enemy(used for rotating)
        self.health = 100
        self.movementSpeed = 200