import pygame, math, random
from Vector2 import Vector2


class TntTurretDynamite(pygame.sprite.Sprite):

    def __init__(self, damage, fuseTime, velocity, AOE, pos, posToGoTO, dynamiteImages, levelReference, *sprite_groups):
        super().__init__(*sprite_groups)

        self.posToGoTO = Vector2(posToGoTO)
        self.position = Vector2(pos)

        self.levelReference = levelReference

        self.velocity = velocity
        self.damage = damage
        self.areaOfEffect = AOE
        self.direction = 0

        self.dynamiteImages = dynamiteImages
        self.dynamiteImageIndex = 0

        self.tntImage = dynamiteImages[0].convert_alpha()
        self.tntImage = pygame.transform.scale(self.tntImage, (16, 58))

        self.outlineDynamite = self.getOutline(self.tntImage, [0, 0, 0])
        self.tntImage.blit(self.outlineDynamite, (0, 0))

        self.AOESurface = pygame.Surface((self.areaOfEffect * 2, self.areaOfEffect * 2), pygame.SRCALPHA, 32)
        self.AOESurfaceRect = self.AOESurface.get_rect()

        self.rotate()
        self.reacherDestination = False

        self.detonationTimer = 0
        self.detonationTime = fuseTime

        self.hasDetonated = False

        self.changeImageTimer = 0
        self.changeImageTime = self.detonationTime / 4

        self.pauseTimer = 0
        self.pauseTime = 0.4

        self.explosionSound = pygame.mixer.Sound("TowerDefense/Sounds/explosion" + str(random.randint(1, 2)) + ".wav")
        self.explosionSound.set_volume(0.032)

    def update(self, deltaTime, allSprites, turretSprites, enemySprites, projectileSprites):

        if self.reacherDestination == False:

            #  Move towards enemy
            moveToPositionVector = self.posToGoTO - self.position
            moveToPositionVector.length = self.velocity * deltaTime

            if moveToPositionVector.length > self.posToGoTO.get_distance(self.position):
                moveToPositionVector.length = self.posToGoTO.get_distance(self.position)
                self.reacherDestination = True

            self.position += moveToPositionVector
            self.rect = self.image.get_rect()
            self.rect.center = self.position

        if self.reacherDestination:
            self.changeImageTimer += deltaTime
            if self.changeImageTimer >= self.changeImageTime and self.dynamiteImageIndex < 4:
                self.dynamiteImageIndex += 1
                self.tntImage = self.dynamiteImages[self.dynamiteImageIndex].convert_alpha()

                if self.dynamiteImageIndex == 4:
                    self.tntImage = pygame.transform.scale(self.tntImage, (118, 83))
                else:
                    self.tntImage = pygame.transform.scale(self.tntImage, (16, 58))

                self.outlineDynamite = self.getOutline(self.tntImage, [0, 0, 0])
                self.tntImage.blit(self.outlineDynamite, (0, 0))

                if self.dynamiteImageIndex < 4:
                    self.image = pygame.transform.rotozoom(self.tntImage, self.direction, 1)
                else:
                    self.image = pygame.transform.rotozoom(self.tntImage, 0, 1)

                self.rect = self.image.get_rect()
                self.rect.center = self.position
                self.changeImageTimer = 0

            if self.hasDetonated == False:

                self.detonationTimer += deltaTime
                if self.detonationTimer >= self.detonationTime:
                    self.hasDetonated = True
                    self.explosionSound.play()
                    for enemyHit in self.levelReference.GetAllEnemiesInRadius(self.position, self.areaOfEffect, enemySprites):
                        enemyHit.takeDamage(self.damage)
            else:
                self.pauseTimer += deltaTime
                if self.pauseTimer >= self.pauseTime:
                    self.kill()

    def draw(self, screen):

        if self.hasDetonated == False:
            pygame.draw.circle(self.AOESurface, [255, 0, 0, 4], self.AOESurfaceRect.center, self.areaOfEffect)
            pygame.draw.circle(self.AOESurface, [0, 0, 0, 60], self.AOESurfaceRect.center, self.areaOfEffect, 1)
            screen.blit(self.AOESurface, (self.position.x - self.areaOfEffect, self.position.y - self.areaOfEffect))

        screen.blit(self.image, self.rect)

    def rotate(self):

        #  Move towards PosToFollow
        posToFollowLookAt = self.posToGoTO - self.position
        self.direction = -posToFollowLookAt.angle
        self.image = pygame.transform.rotozoom(self.tntImage, self.direction, 1)  # the image is rotated the wrong way so the plus 90 fixed this
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def getOutline(self, image, color=(0, 0, 0), threshold=127):
        mask = pygame.mask.from_surface(image, threshold)
        outline_image = pygame.Surface(image.get_size()).convert_alpha()
        outline_image.fill((0, 0, 0, 0))

        # outline_image = pygame.transform.rotozoom(outline_image, 0, 1)

        for point in mask.outline():
            outline_image.set_at(point, color)
        return outline_image
