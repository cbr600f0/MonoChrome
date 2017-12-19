import pygame

class ShopTurretSquare():

    def __init__(self, xPos, yPos, turretName, turretRange, price):

        self.price = price
        self.turretName = turretName
        self.xPos = xPos
        self.yPos = yPos
        self.turretRange = turretRange

        self.isDragginTurret = False

        self.turretSquareSurface = pygame.Surface([120, 120], pygame.SRCALPHA, 32).convert_alpha()
        pygame.draw.rect(self.turretSquareSurface, [50, 30, 14], pygame.Rect(1, 1, 118, 118), 3)

        if self.turretName == "Akimbo":
            self.turretImage = pygame.image.load("TowerDefense\Images\Turrets\AkimboRevolverTurret.png").convert_alpha()
            self.turretImage = pygame.transform.scale(self.turretImage, (48, 98))

            self.turretSquareSurface.blit(self.turretImage, (36, 10))

        elif self.turretName == "Tnt":
            self.turretImage = pygame.image.load("TowerDefense/Images/Turrets/tntTurret.png").convert_alpha()
            self.turretImage = pygame.transform.scale(self.turretImage, (86, 74))# 45 39

            self.turretSquareSurface.blit(self.turretImage, (18, 18))

        self.redTurretImage = self.turretImage.copy()
        self.colorSurface(self.redTurretImage, (110, 0, 0, 0))
        self.turretSquareRect = self.turretSquareSurface.get_rect()
        self.dragImageRect = None
        self.collisionRect = None

    def draw(self, surface, playerGold, isHovering):

        if isHovering and playerGold >= self.price:
            pygame.draw.rect(self.turretSquareSurface, [65, 45, 29], pygame.Rect(1, 1, 118, 118))
        #elif playerGold < self.price:
            #pygame.draw.rect(self.turretSquareSurface, [120, 0, 0], pygame.Rect(1, 1, 118, 118))
        else:
            pygame.draw.rect(self.turretSquareSurface, [80, 60, 44], pygame.Rect(1, 1, 118, 118))


        if self.turretName == "Akimbo":
            if playerGold < self.price:
                self.turretSquareSurface.blit(self.redTurretImage, (36, 10))
            else:
                self.turretSquareSurface.blit(self.turretImage, (36, 10))

        elif self.turretName == "Tnt":
            if playerGold < self.price:
                self.turretSquareSurface.blit(self.redTurretImage, (18, 18))
            else:
                self.turretSquareSurface.blit(self.turretImage, (18, 18))

        pygame.draw.rect(self.turretSquareSurface, [50, 30, 14], pygame.Rect(1, 1, 118, 118), 3)

        if self.isDragginTurret:
            mousePos = pygame.mouse.get_pos()

            if self.turretName == "Akimbo":
                imagePos = (mousePos[0] - 24,    mousePos[1] - 49)

                self.dragImageRect = surface.blit(self.turretImage, imagePos)
                self.collisionRect = pygame.draw.rect(surface, [0, 0, 0], pygame.Rect(self.dragImageRect.center[0] - 30, self.dragImageRect.center[1] - 47, 60, 94), 2)

            elif self.turretName == "Tnt":
                imagePos = (mousePos[0] - 43, mousePos[1] - 37)

                self.dragImageRect = surface.blit(self.turretImage, imagePos)
                self.collisionRect = pygame.draw.rect(surface, [0, 0, 0], pygame.Rect(self.dragImageRect.center[0] - 38, self.dragImageRect.center[1] - 38, 76, 68), 2)

            #Turret Range
            pygame.draw.circle(surface, [0, 0, 0], mousePos, self.turretRange, 2)

        return surface.blit(self.turretSquareSurface, (self.xPos, self.yPos))

    def clicked(self):
        self.isDragginTurret = True

    def colorSurface(self, surface, color):
        """Fill all pixels of the surface with color, preserve transparency."""
        w, h = surface.get_size()
        r, g, b, _ = color
        for x in range(w):
            for y in range(h):
                a = surface.get_at((x, y))[3]
                surface.set_at((x, y), pygame.Color(r, g, b, a))

    def getOutline(self, image, color=(0, 0, 0), threshold=127):
        mask = pygame.mask.from_surface(image, threshold)
        outline_image = pygame.Surface(image.get_size()).convert_alpha()
        outline_image.fill((0, 0, 0, 0))
        for point in mask.outline():
            outline_image.set_at(point, color)
        return outline_image


