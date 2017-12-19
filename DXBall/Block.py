import pygame
from pygame.math import Vector2
import SceneManager

class Block(pygame.sprite.Sprite):

    def __init__(self, spawnPos, *sprite_groups):
        super().__init__(*sprite_groups)

        self.position = Vector2(spawnPos)
        #pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(100, 200, 100, 50))  # block
        self.blockSurface = pygame.Surface((100, 50))
        self.blockSurface.fill((255, 255, 255))

        self.image = self.blockSurface
        self.rect = self.blockSurface.get_rect()
        self.rect.center = self.position

    def update(self, deltaTime, allSprites, ballSprites, ballcollideSprites):
        pass



