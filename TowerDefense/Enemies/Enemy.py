import pygame
from Vector2 import Vector2

class Enemy(pygame.sprite.Sprite):

    def __init__(self, positionsToFollow, *sprite_groups):
        super().__init__(*sprite_groups)

        self.name = "Base Enemy"
        self.description = "This is an enemy"
        self.direction = 0  # What is the angle of this enemy(used for rotating)
        self.health = 100
        self.movementSpeed = 80
        self.hasDied = False
        self.positionsToFollow = positionsToFollow
        self.destinationPosIndex = 0
        self.nextPositionToGoTo = None
        self.position = Vector2(positionsToFollow[0][0], positionsToFollow[0][1]) # Start on the line ofcourse

        self.scoreOnKill = 20
        self.goldOnKill = 100
        self.goldToSteal = 10
        self.hasStolenGoldFromBank = False
        self.distanceLeft = 0

    def takeDamage(self, damageTaken):
        raise NotImplemented

    def die(self):
        raise NotImplemented