import pygame, math
from pygame import gfxdraw
from Vector2 import Vector2

class Turret(pygame.sprite.Sprite):

    def __init__(self, pos, *sprite_groups):
        super().__init__(*sprite_groups)

        self.name = "Base Turret"
        self.position = pos
        self.direction = 0 # What is the angle of this turret(Used for rotating the turret)
        self.range = 200
        self.isFocusedByUser = False
        self.collisionRect = pygame.Rect(math.floor(self.position.x - 30), math.floor(self.position.y - 40), 60, 80)
        #pygame.Rect(self.dragImageRect.center[0] - 30, self.dragImageRect.center[1] - 50, 60, 100)
