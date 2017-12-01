import pygame
from TowerDefense.Towers.Turret import Turret
from Vector2D import Vector2D

class AkimboRevolverTurret(Turret):

    def __init__(self):
        Turret.__init__(self)
        self.PosToFollow = Vector2D(0, 0)
        self.turretWidth = 58
        self.turretHeight = 114

        self.turretImage = pygame.image.load("TowerDefense\Images\Turrets\AkimboRevolverTurret.png")
        self.turretImage = pygame.transform.scale(self.turretImage, (self.turretWidth, self.turretHeight))

        self.image = self.turretImage
        self.rect = self.turretImage.get_rect()
        self.rect.move_ip(self.position)

    def update(self):
        self.rotate()

    def rotate(self):

        #  Move towards mouse pos and stop the cube when its at the mouse position
        mousePos = Vector2D(pygame.mouse.get_pos())
        MouseLookAt = self.PosToFollow - Vector2D((self.rect.centerx, self.rect.centery))
        self.direction = -MouseLookAt.angle + 90
        self.image = pygame.transform.rotate(self.turretImage, self.direction)  # the image is rotated the wrong way so the plus 90 fixed this
        self.rect = self.image.get_rect()
        self.rect.center = self.position
