import pygame
from Vector2 import Vector2

class Enemy(pygame.sprite.Sprite):

    def __init__(self, pos, *sprite_groups):
        super().__init__(*sprite_groups)

        self.name = "Base Enemy"
        self.position = pos
        self.direction = 0  # What is the angle of this enemy(used for rotating)
        self.health = 100
        self.movementSpeed = 200
        self.hasDied = False

    def takeDamage(self, damageTaken):
        raise NotImplemented

    def die(self):
        raise NotImplemented