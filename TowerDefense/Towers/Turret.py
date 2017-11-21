import pygame
from pygame import gfxdraw
from Vector2D import Vector2D

class Turret(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.turretWidth = 80
        self.turretHeight = 80

        self.surfaceMaster = pygame.Surface((self.turretWidth, self.turretHeight)).convert()
        self.surfaceMaster.set_colorkey([255, 0, 255])  # Makes the surface transparent

        self.turretBaseSurface = pygame.Surface((70, 70)).convert()



        self.rect = self.surfaceMaster.get_rect()
        self.rect.center = (320, 240)
        self.turnRate = 10
        self.direction = 0

        baseRect = pygame.Rect(0, 0, self.turretWidth, self.turretHeight)
        topBaseRect = pygame.Rect(baseRect.centerx - 35, baseRect.centery - 35, 70, 70)
        turretBarrelRect = pygame.Rect(topBaseRect.centerx, topBaseRect.centery - 5, 50, 10)

        pygame.draw.rect(self.surfaceMaster, [0, 0, 0], baseRect)
        pygame.draw.rect(self.surfaceMaster, [100, 100, 100], topBaseRect)
        pygame.gfxdraw.filled_circle(self.turretBaseSurface, topBaseRect.centerx, topBaseRect.centery, 20, [0, 0, 0])
        pygame.gfxdraw.aacircle(self.turretBaseSurface, topBaseRect.centerx, topBaseRect.centery, 20, [0, 0, 0])
        pygame.draw.rect(self.turretBaseSurface, [30, 30, 30], turretBarrelRect)


    def update(self):
        self.checkKeys()
        self.rotate()

    def checkKeys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction += self.turnRate
            if self.direction > 360:
                self.direction = self.turnRate
        if keys[pygame.K_RIGHT]:
            self.direction -= self.turnRate
            if self.direction < 0:
                self.direction = 360 - self.turnRate

    def rotate(self):

        #  Move towards mouse pos and stop the cube when its at the mouse position
        mousePos = Vector2D(pygame.mouse.get_pos())
        MouseLookAt = mousePos - Vector2D((self.rect.centerx, self.rect.centery))

        oldCenter = self.rect.center
        self.image = pygame.transform.rotate(self.surfaceMaster, -MouseLookAt.angle)
        self.rect = self.image.get_rect()
        self.rect.center = oldCenter

def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption ("Rotating Turret")

    background = pygame.Surface(screen.get_size())
    background.fill((0x00, 0xCC, 0x00))
    screen.blit(background, (0, 0))

    turret = Turret()
    allSprites = pygame.sprite.Group(turret)

    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
