import pygame
from TowerDefense.Enemies.Enemy import Enemy
from Vector2D import Vector2D


class Robber(Enemy):

    def __init__(self):
        Enemy.__init__(self)
        self.PosToFollow = Vector2D(0, 0)
        self.enemyWidth = 90
        self.enemyHeight = 56

        self.enemyImage = pygame.image.load("TowerDefense\Images\Enemies\Robber.png")
        self.enemyImage = pygame.transform.scale(self.enemyImage, (self.enemyWidth, self.enemyHeight))

        self.image = self.enemyImage
        self.rect = self.enemyImage.get_rect()
        self.rect.move_ip(self.position)

    def update(self, deltaTime):

        #  Move towards mouse pos and stop the cube when its at the mouse position
        self.PosToFollow = Vector2D(pygame.mouse.get_pos())

        moveToMousePosVector = self.PosToFollow - self.position

        if self.position.get_distance(self.PosToFollow) > 0:
            moveToMousePosVector.length = 1

        if moveToMousePosVector.length > self.PosToFollow.get_distance(self.position):
            moveToMousePosVector.length = self.PosToFollow.get_distance(self.position)

        self.position += moveToMousePosVector * 600 * deltaTime

        self.rotate()

    def rotate(self):

        #  Move towards PosToFollow
        PosToFollowLookatVector = self.PosToFollow - self.position
        self.direction = -PosToFollowLookatVector.angle - 90
        self.image = pygame.transform.rotate(self.enemyImage, self.direction)  # the image is rotated the wrong way so the plus 90 fixed this
        self.rect = self.image.get_rect()
        self.rect.center = self.position
