import pygame, math

class ShopTurretSquare():

    def __init__(self, xPos, yPos, turretObject, price, turretName):

        self.price = price
        self.turretObject = turretObject
        self.turretName = turretName
        self.xPos = xPos
        self.yPos = yPos
        self.outlineColor = (0, 0, 0)
        self.isDragginTurret = False

        self.turretSquareSurface = pygame.Surface([120, 120], pygame.SRCALPHA, 32).convert_alpha()
        self.turretSquareRect = self.turretSquareSurface.get_rect()
        pygame.draw.rect(self.turretSquareSurface, [50, 30, 14], pygame.Rect(1, 1, 118, 118), 3)

        self.turretPlaceHolderImage = self.turretObject.turretImage.copy().convert_alpha()
        self.outlineTurretImage = self.getOutline(self.turretPlaceHolderImage, [0, 0, 0])
        self.turretPlaceHolderImage.blit(self.outlineTurretImage, (0, 0))

        self.turretSquareSurface.blit(self.turretPlaceHolderImage, (self.turretSquareRect.centerx - self.turretPlaceHolderImage.get_rect().centerx, self.turretSquareRect.centery - self.turretPlaceHolderImage.get_rect().centery))#(36, 10)

        self.dragginTurretImage = self.turretPlaceHolderImage.copy().convert_alpha()

        self.redTurretImage = self.turretPlaceHolderImage.copy()
        self.colorSurface(self.redTurretImage, (110, 0, 0, 0))

        self.collisionRect = None

    def draw(self, surface, playerGold, isHovering):

        if isHovering and playerGold >= self.price:
            pygame.draw.rect(self.turretSquareSurface, [65, 45, 29], pygame.Rect(1, 1, 118, 118))
        else:
            pygame.draw.rect(self.turretSquareSurface, [80, 60, 44], pygame.Rect(1, 1, 118, 118))


        placeHolderImageToDisplay = self.turretPlaceHolderImage
        if playerGold < self.price:
            placeHolderImageToDisplay = self.redTurretImage

        self.turretSquareSurface.blit(placeHolderImageToDisplay, ( self.turretSquareRect.centerx - self.turretPlaceHolderImage.get_rect().centerx, self.turretSquareRect.centery - self.turretPlaceHolderImage.get_rect().centery))  # (36, 10)
        pygame.draw.rect(self.turretSquareSurface, [50, 30, 14], pygame.Rect(1, 1, 118, 118), 3)

        if self.isDragginTurret:
            mousePos = pygame.mouse.get_pos()
            dragImageRect = None

            imagePos = (mousePos[0] - self.turretPlaceHolderImage.get_rect().centerx, mousePos[1] - self.turretPlaceHolderImage.get_rect().centery)
            dragImageRect = surface.blit(self.dragginTurretImage, imagePos)

            self.collisionRect = pygame.Rect(dragImageRect.x, dragImageRect.y, self.turretObject.collisionRect.width, self.turretObject.collisionRect.height)

            #Turret Range
            pygame.draw.circle(surface, [0, 0, 0], mousePos, self.turretObject.range, 2)

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

    def changeOutlineColor(self, color):
        self.outlineTurretImage = self.getOutline(self.turretPlaceHolderImage, color)
        self.dragginTurretImage.blit(self.outlineTurretImage, (0, 0))



