import pygame, random, SceneManager
from ButtonClass import Button
from Vector2 import Vector2
from TowerDefense.Towers.AkimboRevolverTurret import AkimboRevolverTurret
from TowerDefense.Towers.TntTurret import TntTurret
from TowerDefense.Towers.SniperTurret import SniperTurret
from TowerDefense.Enemies.Robber import Robber
from TowerDefense.ShopTurretSquare import ShopTurretSquare
from TowerDefense.Towers.Turret import Turret


class Level1Scene(SceneManager.Scene):

    def __init__(self, *optionalInformation):
        super(Level1Scene, self).__init__()
        self.mark = 294334

        self.level1LinePositions = ([950, 980], [950, 500], [1090, 500], [1090, 180], [130, 180], [130, 800], [370, 800], [370, 500], [750, 500], [750, 980])
        self.level1BankPosition = (210, 636)
        self.bankImage = pygame.image.load("TowerDefense/Images/Bank2.png")
        #self.bankImage = pygame.transform.rotate(self.bankImage, 90)

        self.gold = 1000
        self.score = 0
        self.difficulty = "Normal"

        #Gameobject stuff
        self.allSprites = pygame.sprite.Group()

        self.enemySprites = pygame.sprite.Group()
        self.turretSprites = pygame.sprite.Group()
        self.bulletSprites = pygame.sprite.Group()

        #Spawner Stuff (Maybe make a seperate Spawner class)
        self.spawnerIsActive = True
        self.spawnTimer = 0
        self.spawnPauseTimer = 0
        self.pauseDuration = 7

        self.numberOfEnemiesToSpawn = 7
        self.numberOfEnemiesSpawnedThisRound = 0
        self.currentRound = 1

        # Interface Stuff
        self.mainBG = pygame.Surface((1600, 900))
        self.mainBG.fill([100, 80, 63])

        self.westernFont = pygame.font.Font("TowerDefense\WesternFont.otf", 28)
        self.backToMainMenuBtn = Button(False, self.westernFont, "Main menu", None, None, [120, 120, 120], [117, 100, 85], 100, 75, None, 60)
        self.nextRoundFont = pygame.font.Font("TowerDefense\WesternFont.otf", 36)
        self.nextRoundBtn = Button(False, self.nextRoundFont, "Next Round", None, None, [40, 40, 40], [0, 0, 0], 1360, 820, None, 60)

        self.difficultyLbl = self.westernFont.render("Difficulty: " + str(self.difficulty), True, [0, 0, 0])
        self.scoreLbl = self.westernFont.render("Score: " + str(self.score), True, [0, 0, 0])
        self.goldLbl = self.westernFont.render("Gold: " + str(self.gold), True, [0, 0, 0])
        self.roundLbl = self.westernFont.render("Round: " + str(self.currentRound), True, [0, 0, 0])

        self.akimboShopSquare = ShopTurretSquare(1390, 100, "Akimbo", 180, 200)
        self.tntShopSqaure = ShopTurretSquare(1390, 240, "Tnt", 210, 350)
        self.sniperShopSquare = ShopTurretSquare(1390, 380, "Sniper", 440, 600)

        self.akimboShopRect = None
        self.isHoveringOverAkimboShopRect = False
        self.tntShopRect = None
        self.isHoveringOverTntShopRect = False
        self.sniperShopRect = None
        self.isHoveringOverSniperShopRect = False

        self.turretToPlaceName = ""

        self.unableToPlaceRects = []

        self.rightHUDSideRect = pygame.Rect(1300, 73, 300, 827)
        self.upperHUDSideRect = pygame.Rect(0, 0, 1600, 70)

        self.unableToPlaceRects.append(self.rightHUDSideRect)
        self.unableToPlaceRects.append(self.upperHUDSideRect)

        self.getPathRects = True

    def render(self, screen):
        self.allSprites.clear(screen, self.mainBG)

        screen.blit(self.mainBG, (0, 0))

        self.renderPath(screen)

        for spriteToDraw in self.allSprites:
            spriteToDraw.draw(screen)

        screen.blit(self.bankImage, self.level1BankPosition)
        #self.allSprites.draw(screen)
        self.renderHud(screen)

        # self.backToMainMenuBtn.draw(screen)
        self.nextRoundBtn.draw(screen)

    def update(self, deltaTime):

        if self.spawnerIsActive:

            if self.numberOfEnemiesSpawnedThisRound < self.numberOfEnemiesToSpawn:
                self.spawnTimer += deltaTime

                if self.spawnTimer > 1:
                    Robber(self.level1LinePositions, self, self.allSprites, self.enemySprites)
                    self.numberOfEnemiesSpawnedThisRound += 1
                    self.spawnTimer = 0
            else:
                self.spawnerIsActive = False

        else:
            self.spawnPauseTimer += deltaTime
            if self.spawnPauseTimer >= self.pauseDuration:
                self.beginNextRound()

        self.allSprites.update(deltaTime, self.allSprites, self.turretSprites, self.enemySprites, self.bulletSprites)

        if self.akimboShopSquare.isDragginTurret and self.gold < self.akimboShopSquare.price or self.tntShopSqaure.isDragginTurret and self.gold < self.tntShopSqaure.price:
            self.turretToPlaceName = ""
            self.tntShopSqaure.isDragginTurret = False
            self.akimboShopSquare.isDragginTurret = False

        if self.backToMainMenuBtn.click():
            SceneManager.SceneManager.goToScene("TowerDefense.TowerDefenseMainMenuScene.TowerDefenseMainMenuScene")

        if self.nextRoundBtn.click():  # Probably remove the function to go to the next round
            pass

    def beginNextRound(self):
        self.numberOfEnemiesToSpawn += 1
        self.currentRound += 1
        self.numberOfEnemiesSpawnedThisRound = 0
        self.spawnTimer = 0
        self.spawnPauseTimer = 0
        self.spawnerIsActive = True

    def GetClosestEnemyInRadius(self, centerPos, radius, enemySprites):

        closestEnemyPosition = None
        closestEnemy = None

        for enemy in enemySprites:
            distanceToEnemy = centerPos.get_distance(enemy.position)

            if distanceToEnemy <= radius:
                if closestEnemyPosition is None:
                    closestEnemyPosition = distanceToEnemy
                    closestEnemy = enemy
                elif distanceToEnemy < closestEnemyPosition:
                    closestEnemyPosition = distanceToEnemy
                    closestEnemy = enemy

        return closestEnemy

    def GetAllEnemiesInRadius(self, centerPos, radius, enemySprites):

        enemiesInRadius = []

        for enemy in enemySprites:
            distanceToEnemy = centerPos.get_distance(enemy.position)

            if distanceToEnemy <= radius:
                enemiesInRadius.append(enemy)

        return enemiesInRadius

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousePos = pygame.mouse.get_pos()

                if self.sniperShopSquare.isDragginTurret == False and self.akimboShopSquare.isDragginTurret == False and self.tntShopSqaure.isDragginTurret == False:
                    spriteHasBeenFocused = False
                    for sprite in self.allSprites.sprites():

                        if sprite.rect.collidepoint(mousePos) and spriteHasBeenFocused == False:
                            sprite.isFocusedByUser = True
                            spriteHasBeenFocused = True
                        else:
                            sprite.isFocusedByUser = False

                isMouseClickInsideUnplaceableBounds = False
                for turret in self.turretSprites.sprites():
                    if self.turretToPlaceName == "Akimbo":
                        if turret.collisionRect.colliderect(self.akimboShopSquare.collisionRect):
                            isMouseClickInsideUnplaceableBounds = True
                            break

                    if self.turretToPlaceName == "Tnt":
                        if turret.collisionRect.colliderect(self.tntShopSqaure.collisionRect):
                            isMouseClickInsideUnplaceableBounds = True
                            break

                    if self.turretToPlaceName == "Sniper":
                        if turret.collisionRect.colliderect(self.sniperShopSquare.collisionRect):
                            isMouseClickInsideUnplaceableBounds = True
                            break

                if isMouseClickInsideUnplaceableBounds == False:
                    for unplaceableBounds in self.unableToPlaceRects:

                        if self.turretToPlaceName == "Akimbo":
                            if unplaceableBounds.colliderect(self.akimboShopSquare.collisionRect):
                                isMouseClickInsideUnplaceableBounds = True
                                break

                        if self.turretToPlaceName == "Tnt":
                            if unplaceableBounds.colliderect(self.tntShopSqaure.collisionRect):
                                isMouseClickInsideUnplaceableBounds = True
                                break

                        if self.turretToPlaceName == "Sniper":
                            if unplaceableBounds.colliderect(self.sniperShopSquare.collisionRect):
                                isMouseClickInsideUnplaceableBounds = True
                                break

                if isMouseClickInsideUnplaceableBounds == False:

                    if self.turretToPlaceName == "Akimbo":
                        AkimboRevolverTurret(Vector2(mousePos), self, self.allSprites, self.turretSprites)
                        self.turretToPlaceName = ""
                        self.akimboShopSquare.isDragginTurret = False

                    elif self.turretToPlaceName == "Tnt":
                        TntTurret(Vector2(mousePos), self, self.allSprites, self.turretSprites)
                        self.turretToPlaceName = ""
                        self.tntShopSqaure.isDragginTurret = False

                    elif self.turretToPlaceName == "Sniper":
                        SniperTurret(Vector2(mousePos), self, self.allSprites, self.turretSprites)
                        self.turretToPlaceName = ""
                        self.sniperShopSquare.isDragginTurret = False
                else:
                    self.turretToPlaceName = ""
                    self.tntShopSqaure.isDragginTurret = False
                    self.akimboShopSquare.isDragginTurret = False
                    self.sniperShopSquare.isDragginTurret = False

                if self.gold >= self.akimboShopSquare.price and self.akimboShopSquare.isDragginTurret == False and self.akimboShopRect.collidepoint(mousePos):
                    self.akimboShopSquare.clicked()
                    self.turretToPlaceName = "Akimbo"

                if self.gold >= self.tntShopSqaure.price and self.tntShopSqaure.isDragginTurret == False and self.tntShopRect.collidepoint(mousePos):
                    self.tntShopSqaure.clicked()
                    self.turretToPlaceName = "Tnt"

                if self.gold >= self.sniperShopSquare.price and self.sniperShopSquare.isDragginTurret == False and self.sniperShopRect.collidepoint(mousePos):
                    self.sniperShopSquare.clicked()
                    self.turretToPlaceName = "Sniper"

            if event.type == pygame.MOUSEMOTION:
                mousePos = pygame.mouse.get_pos()

                self.isHoveringOverAkimboShopRect = self.akimboShopRect.collidepoint(mousePos) # Mouse is hovering over this shop sqaure
                self.isHoveringOverTntShopRect = self.tntShopRect.collidepoint(mousePos) # Mouse is hovering over this shop sqaure
                self.isHoveringOverSniperShopRect = self.sniperShopRect.collidepoint(mousePos) # Mouse is hovering over this shop sqaure

                if self.turretToPlaceName is not "":
                    self.CheckHoverTurretCollision()

    def renderPath(self, screen):
        COLOR = [80, 60, 44]

        if self.getPathRects:
            for index, lineLocation in enumerate(self.level1LinePositions):
                if (index + 1 >= len(self.level1LinePositions)) == False:
                    self.unableToPlaceRects.append(pygame.draw.line(screen, COLOR, lineLocation, self.level1LinePositions[index + 1], 80))

            self.unableToPlaceRects.append(pygame.draw.rect(screen, [255, 0, 0], pygame.Rect(1090, 500, 80, 80))) # This is a rect to fix an open corner of level1
            self.unableToPlaceRects.append(pygame.draw.rect(screen, [255, 0, 0], pygame.Rect(370, 800, 80, 80))) # This is a rect to fix an open corner of level1

            self.getPathRects = False

            for index, linePos in enumerate(self.level1LinePositions):
                self.level1LinePositions[index][0] += 40
                self.level1LinePositions[index][1] += 40
        else:
            for lineRect in self.unableToPlaceRects:
                pygame.draw.rect(screen, COLOR, lineRect)

    def renderHud(self, screen):

        self.difficultyLbl = self.westernFont.render("Difficulty: " + str(self.difficulty), True, [0, 0, 0])
        self.scoreLbl = self.westernFont.render("Score: " + str(self.score), True, [0, 0, 0])
        self.roundLbl = self.westernFont.render("Round: " + str(self.currentRound), True, [0, 0, 0])
        self.goldLbl = self.westernFont.render("Gold: " + str(self.gold), True, [0, 0, 0])

        # Top
        pygame.draw.line(screen, [50, 30, 14], (0, 70), (1600, 70), 4) # Top Border
        pygame.draw.rect(screen, [80, 60, 44], self.upperHUDSideRect)

        screen.blit(self.difficultyLbl, (130, 7))

        pygame.draw.line(screen, [50, 30, 14], (500, 0), (500, 70), 4)

        screen.blit(self.scoreLbl, (670, 7))

        pygame.draw.line(screen, [50, 30, 14], (930, 0), (930, 70), 4)

        screen.blit(self.roundLbl, (1070, 7))

        screen.blit(self.goldLbl, (1400, 7))

        # Right
        pygame.draw.rect(screen, [80, 60, 44], self.rightHUDSideRect)

        pygame.draw.line(screen, [50, 30, 14], (1300, 0), (1300, 900), 4)

        # Right Bottom
        pygame.draw.line(screen, [50, 30, 14], (1300, 800), (1600, 800), 4)

        self.akimboShopRect = self.akimboShopSquare.draw(screen, self.gold, self.isHoveringOverAkimboShopRect)
        self.tntShopRect = self.tntShopSqaure.draw(screen, self.gold, self.isHoveringOverTntShopRect)
        self.sniperShopRect = self.sniperShopSquare.draw(screen, self.gold, self.isHoveringOverSniperShopRect)

    def CheckHoverTurretCollision(self):
        turretIsInsideSomething = False
        for turret in self.turretSprites.sprites():
            if self.turretToPlaceName == "Akimbo":
                if turret.collisionRect.colliderect(self.akimboShopSquare.collisionRect):
                    turretIsInsideSomething = True
                    break

            if self.turretToPlaceName == "Tnt":
                if turret.collisionRect.colliderect(self.tntShopSqaure.collisionRect):
                    turretIsInsideSomething = True
                    break

            if self.turretToPlaceName == "Sniper":
                if turret.collisionRect.colliderect(self.sniperShopSquare.collisionRect):
                    turretIsInsideSomething = True
                    break

        if turretIsInsideSomething == False:
            for unplaceableBounds in self.unableToPlaceRects:

                if self.turretToPlaceName == "Akimbo":
                    if unplaceableBounds.colliderect(self.akimboShopSquare.collisionRect):
                        turretIsInsideSomething = True
                        break

                if self.turretToPlaceName == "Tnt":
                    if unplaceableBounds.colliderect(self.tntShopSqaure.collisionRect):
                        turretIsInsideSomething = True
                        break

                if self.turretToPlaceName == "Sniper":
                    if unplaceableBounds.colliderect(self.sniperShopSquare.collisionRect):
                        turretIsInsideSomething = True
                        break

        if turretIsInsideSomething:
            if self.turretToPlaceName == "Akimbo":
                self.akimboShopSquare.changeOutlineColor((255, 0, 0))

            if self.turretToPlaceName == "Tnt":
                self.tntShopSqaure.changeOutlineColor((255, 0, 0))

            if self.turretToPlaceName == "Sniper":
                self.sniperShopSquare.changeOutlineColor((255, 0, 0))
        else:
            if self.turretToPlaceName == "Akimbo":
                self.akimboShopSquare.changeOutlineColor((0, 0, 0))

            if self.turretToPlaceName == "Tnt":
                self.tntShopSqaure.changeOutlineColor((0, 0, 0))

            if self.turretToPlaceName == "Sniper":
                self.sniperShopSquare.changeOutlineColor((0, 0, 0))