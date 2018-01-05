import pygame, math, random
from Vector2 import Vector2


class Moneybag(pygame.sprite.Sprite):

    def __init__(self, spawnPos, degrees, levelReference, goldValue, *sprite_groups):
        super().__init__(*sprite_groups)

        self.levelReference = levelReference
        self.goldValue = goldValue
        self.direction = degrees
        self.position = spawnPos
        self.moneybagImage = pygame.image.load("TowerDefense/Images/Enemies/MoneybagSepia.png").convert_alpha()
        self.moneybagOutline = self.getOutline(self.moneybagImage, [0, 0, 0])
        self.moneybagImage.blit(self.moneybagOutline, (0, 0))
        self.rotate()

    def update(self, deltaTime):
        mousePos = Vector2(pygame.mouse.get_pos())

        if self.position.get_distance(mousePos) < 200:
            moveToPositionVector = mousePos - self.position
            moveToPositionVector.length = 60 * deltaTime
            self.position += moveToPositionVector

        if self.rect.collidepoint(mousePos):
            self.levelReference.gold += self.goldValue # add a sound when a moneybag is picked up
            self.kill()

        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def rotate(self):

        self.image = pygame.transform.rotate(self.moneybagImage, -self.direction + 90)  # the image is rotated the wrong way so the plus 90 fixed this
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def getOutline(self, image, color=(0, 0, 0), threshold=127):
        mask = pygame.mask.from_surface(image, threshold)
        outline_image = pygame.Surface(image.get_size()).convert_alpha()
        outline_image.fill((0, 0, 0, 0))
        for point in mask.outline():
            outline_image.set_at(point, color)
        return outline_image
