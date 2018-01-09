import pygame, random
from pygame.math import Vector2


class Block(pygame.sprite.Sprite):

    def __init__(self, spawnPos, *sprite_groups):
        super().__init__(*sprite_groups)
        self.position = Vector2(spawnPos)
        self.blockSurface = pygame.Surface((100, 50))
        self.blockSurface.fill((255, 255, 255))
        #self.blockSurface = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

        #pygame.draw.rect(self.blockSurface, [0, 0, 0], self.blockSurface.get_rect(), 2) use something like this to create a line around the block

        self.image = self.blockSurface
        self.rect = self.blockSurface.get_rect()
        self.rect.topleft = (self.position.x, self.position.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, deltaTime, allSprites, ballSprites, ballcollideSprites):
        pass



