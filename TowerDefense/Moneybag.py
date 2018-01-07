import pygame, math, random
from Vector2 import Vector2


class Moneybag(pygame.sprite.Sprite):

    def __init__(self, spawnPos, degrees, levelReference, goldValue, *sprite_groups):
        super().__init__(*sprite_groups)

        self.levelReference = levelReference
        self.goldValue = goldValue
        self.direction = degrees
        self.position = spawnPos
        self.size = (36, 42)
        self.weightStage = 1

        if self.goldValue >= 200 and self.goldValue < 400:
            self.size = (43, 50)
            self.weightStage = 2

        elif self.goldValue >= 400 and self.goldValue < 600:
            self.size = (50, 59)
            self.weightStage = 3

        elif self.goldValue >= 600:
            self.size = (57, 67)
            self.weightStage = 4

        self.moneybagImage = pygame.image.load("TowerDefense/Images/Enemies/MoneybagSepia.png").convert_alpha()
        self.moneybagImage = pygame.transform.scale(self.moneybagImage, self.size)

        self.moneybagOutline = self.getOutline(self.moneybagImage, [0, 0, 0])
        self.moneybagImage.blit(self.moneybagOutline, (0, 0))
        self.rotate()

        self.pickupTimer = 0
        self.timeTillPickup = 0.08
        self.enemyCanPickupBag = False

        self.lblFont = pygame.font.SysFont("monospace", 24)
        self.lblFont.set_bold(True)
        self.hasPickedUpMoney = False
        self.goldValueLbl = self.lblFont.render("+" + str(self.goldValue) + "G", True, [0, 130, 0])
        self.lblPosition = Vector2(self.position)
        self.lblTimer = 0
        self.lblDuration = 2
        self.dontShowAnything = False

    def update(self, deltaTime):

        if self.hasPickedUpMoney:
            self.lblTimer += deltaTime
            self.lblPosition += Vector2(0, -40 * deltaTime)

            if self.lblTimer >= self.lblDuration:
                self.kill()
                self.dontShowAnything = True
        else:
            if self.enemyCanPickupBag == False:
                self.pickupTimer += deltaTime
                if self.pickupTimer >= self.timeTillPickup:
                    self.enemyCanPickupBag = True

            mousePos = Vector2(pygame.mouse.get_pos())

            if self.position.get_distance(mousePos) < 200:
                dragSpeed = 80 - (self.weightStage * 10)
                moveToPositionVector = mousePos - self.position
                moveToPositionVector.length = dragSpeed * deltaTime
                self.position += moveToPositionVector

            if self.rect.collidepoint(mousePos):
                self.levelReference.gold += self.goldValue # add a sound when a moneybag is picked up
                self.hasPickedUpMoney = True
                self.enemyCanPickupBag = False
                self.lblPosition = Vector2(self.position) - Vector2(math.floor(self.size[0] / 2), math.floor(self.size[1] / 2))

            self.rect = self.image.get_rect()
            self.rect.center = self.position

    def draw(self, screen):
        if self.dontShowAnything == False:
            if self.hasPickedUpMoney == False:
                screen.blit(self.image, self.rect)
            else:
                screen.blit(self.goldValueLbl, self.lblPosition)


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
