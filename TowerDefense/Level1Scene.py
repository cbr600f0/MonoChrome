import pygame, random, SceneManager
from ButtonClass import Button
from Vector2 import Vector2
from TowerDefense.Towers.AkimboRevolverTurret import AkimboRevolverTurret
from TowerDefense.Towers.TntTurret import TntTurret
from TowerDefense.Towers.SniperTurret import SniperTurret
from TowerDefense.ShopTurretSquare import ShopTurretSquare
from TowerDefense.Bank import Bank
from TowerDefense.Towers.Turret import Turret
from TowerDefense.Enemies.Enemy import Enemy
from TowerDefense.EnemyWaveSpawner import EnemyWaveSpawner
from TowerDefense.Enemies.Robber import Robber
from TowerDefense.Enemies.HorseRobber import HorseRobber


class Level1Scene(SceneManager.Scene):

    def __init__(self, *optionalInformation):
        super(Level1Scene, self).__init__()

        self.level1LinePositions = ([950, 980], [950, 500], [1090, 500], [1090, 226], [130, 226], [130, 800], [370, 800], [370, 500], [750, 500], [750, 920])
        self.gold = 400 #400
        self.score = 0
        self.difficulty = "Normal"
        self.totalEnemiesKilled = 0

        #Gameobject stuff
        self.allSprites = pygame.sprite.Group()

        self.enemySprites = pygame.sprite.Group()
        self.turretSprites = pygame.sprite.Group()
        self.bankSprite = pygame.sprite.GroupSingle()
        self.projectileSprites = pygame.sprite.Group()
        self.moneybagSprites = pygame.sprite.Group()

        self.bank = Bank(Vector2(440, 150), 90, self, self.bankSprite, self.allSprites)

        #Spawner Stuff (Maybe make a seperate Spawner class)
        self.spawnerIsActive = False
        self.spawnPauseTimer = 0
        self.pauseDuration = 30

        self.currentRound = 0

        # Interface Stuff
        self.mainBG = pygame.Surface((1600, 900))
        self.mainBG.fill([100, 80, 63])

        self.westernFont = pygame.font.Font("TowerDefense\WesternFont.otf", 28)
        self.gameOverFont = pygame.font.Font("TowerDefense\WesternFont.otf", 52)
        self.gameOverStatsFont = pygame.font.Font("TowerDefense\WesternFont.otf", 42)

        self.upgradeTurretStatsHeaderFont = pygame.font.SysFont("monospace", 19)
        self.upgradeTurretStatsHeaderFont.set_bold(True)
        self.upgradeTurretStatsHeaderFont.set_underline(True)

        self.upgradeTurretDescriptionFont = pygame.font.SysFont("monospace", 16)
        self.upgradeTurretDescriptionFont.set_italic(True)

        self.upgradeTurretUpgradeTextFont = pygame.font.SysFont("monospace", 17)
        self.upgradeTurretUpgradeTextFont.set_italic(True)
        self.upgradeTurretUpgradeTextFont.set_bold(True)

        self.upgradeTurretStatsFont = pygame.font.SysFont("monospace", 19)

        self.upgradeTurretSellButton = Button(False, self.upgradeTurretStatsFont, "SELL", [70, 50, 34], [50, 30, 14], [70, 50, 34], [0, 0, 0], 1326, 755, 115, 30)
        self.upgradeTurretUpgradeButton = Button(False, self.upgradeTurretStatsFont, "UPGRADE", [70, 50, 34], [50, 30, 14], [70, 50, 34], [0, 0, 0], 1462, 755, 115, 30)

        self.nextRoundFont = pygame.font.Font("TowerDefense\WesternFont.otf", 36)
        self.startGameBtn = Button(False, self.nextRoundFont, "Start Game", None, None, [40, 40, 40], [0, 0, 0], 1360, 820, None, 60)
        self.nextRoundBtn = Button(False, self.nextRoundFont, "Next Round", None, None, [40, 40, 40], [0, 0, 0], 1360, 820, None, 60)

        self.difficultyLbl = self.westernFont.render("Difficulty: " + str(self.difficulty), True, [0, 0, 0])
        self.scoreLbl = self.westernFont.render("Score: " + str(self.score), True, [0, 0, 0])
        self.goldLbl = self.westernFont.render("Gold: " + str(self.gold), True, [0, 0, 0])
        self.roundLbl = self.westernFont.render("Round: " + str(self.currentRound), True, [0, 0, 0])

        self.akimbo = AkimboRevolverTurret(Vector2(0 ,0), self)
        self.tnt = TntTurret(Vector2(0 ,0), self)
        self.sniper = SniperTurret(Vector2(0 ,0), self)

        self.akimboShopSquare = ShopTurretSquare(1326, 100, self.akimbo, "Akimbo")
        self.tntShopSqaure = ShopTurretSquare(1456, 100, self.tnt, "Tnt")
        self.sniperShopSquare = ShopTurretSquare(1390, 230, self.sniper, "Sniper")

        self.turretPlacementSound = pygame.mixer.Sound("TowerDefense/Sounds/turretPlacement.wav")
        self.turretPlacementSound.set_volume(0.008)

        self.currentShopSquare = None
        self.hoverTurretObject = None

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

        self.gameOver = False
        self.gameOverOverlay = pygame.Surface((600, 600))
        self.gameOverOverlay = self.gameOverOverlay.convert()
        self.gameOverOverlay.fill((50, 30, 14))

        self.gameOverLbl = self.gameOverFont.render("Game Over", True, [0, 0, 0])
        self.roundsSurvivedLbl = self.gameOverStatsFont.render("Final Round " + str(self.currentRound), True, [0, 0, 0])
        self.finalScoreLbl = self.gameOverStatsFont.render("Score " + str(self.score), True, [0, 0, 0])
        self.totalEnemiesKilledLbl = self.gameOverStatsFont.render("Enemies Killed " + str(self.totalEnemiesKilled), True, [0, 0, 0])

        self.retryGameBtn = Button(False, self.westernFont, "Retry", None, None, [20, 20, 20], [0, 0,  0], 800, 650, None, 70)
        self.backToMainMenuBtn = Button(False, self.westernFont, "Main menu", None, None, [20, 20, 20], [0, 0,  0], 900, 650, None, 70)

        pygame.draw.rect(self.gameOverOverlay, [0, 0, 0], self.gameOverOverlay.get_rect(), 4)

        self.focusedSprite = None
        self.upgradeTurretRect = pygame.Rect(1314, 370, 276, 400)

        self.enemySpawnerObjects = []

        self.userAtLastPage = False
        self.showTutorial = True
        self.currentTutorialPage = 1
        self.tutorialImages = [pygame.image.load("TowerDefense\Images\Tutorials\Tutorial1.png"), pygame.image.load("TowerDefense\Images\Tutorials\Tutorial2.png"),pygame.image.load("TowerDefense\Images\Tutorials\Tutorial3.png"),pygame.image.load("TowerDefense\Images\Tutorials\Tutorial4.png"),pygame.image.load("TowerDefense\Images\Tutorials\Tutorial5.png"), pygame.image.load("TowerDefense\Images\Tutorials\Tutorial6.png"),]
        self.tutorialRect = pygame.Rect(400, 160, 580, 400)

        self.tutorialBodyFont = pygame.font.SysFont("monospace", 19)
        self.tutorialBodyFont.set_bold(True)

        self.akimboTurretImage = pygame.image.load("TowerDefense\Images\Turrets\AkimboRevolverTurret.png").convert_alpha()
        self.akimboTurretImage = pygame.transform.scale(self.akimboTurretImage, (48, 98))
        self.outlineTurretImage = self.getOutline(self.akimboTurretImage, [0, 0, 0])
        self.akimboTurretImage.blit(self.outlineTurretImage, (0, 0))

        self.tntTurretImage = pygame.image.load("TowerDefense\Images\Turrets\TntTurret.png").convert_alpha()
        self.tntTurretImage = pygame.transform.scale(self.tntTurretImage, (86, 74))
        self.outlineTurretImage = self.getOutline(self.tntTurretImage, [0, 0, 0])
        self.tntTurretImage.blit(self.outlineTurretImage, (0, 0))

        self.sniperTurretImage = pygame.image.load("TowerDefense\Images\Turrets\SniperTurret.png").convert_alpha()
        self.sniperTurretImage = pygame.transform.scale(self.sniperTurretImage, (50, 98))
        self.outlineTurretImage = self.getOutline(self.sniperTurretImage, [0, 0, 0])
        self.sniperTurretImage.blit(self.outlineTurretImage, (0, 0))

        self.tutCloseBtn = Button(True, None, "Close", None, None, [40, 40, 40], [0, 0, 0], 480, 495, None, 40)
        self.tutNextBtn = Button(True, None, "Next", None, None, [40, 40, 40], [0, 0, 0], 780, 495, None, 40)
        self.tutPreviousBtn = Button(True, None, "Previous", None, None, [40, 40, 40], [0, 0, 0], 480, 495, None, 40)


    def render(self, screen):
        self.allSprites.clear(screen, self.mainBG)

        screen.blit(self.mainBG, (0, 0))

        self.renderPath(screen)

        for spriteToDraw in self.allSprites:
            spriteToDraw.draw(screen)

        self.renderHud(screen)

        if self.showTutorial:
            self.renderTutorialScreen(screen)

        if self.focusedSprite is not None and isinstance(self.focusedSprite, Enemy) and not self.focusedSprite.hasDied:
            self.renderEnemyStatsScreen(screen, self.focusedSprite)

        if self.hoverTurretObject is not None and self.focusedSprite is None:
            self.renderTurretUpgradeScreen(screen, self.hoverTurretObject)
        else:
            if self.focusedSprite is not None and isinstance(self.focusedSprite, Turret):
                self.renderTurretUpgradeScreen(screen, self.focusedSprite)

        if self.spawnerIsActive:
            self.nextRoundBtn.draw(screen)
        else:
            self.startGameBtn.draw(screen)

        if self.gameOver:
            self.renderGameOverScreen(screen)

    def update(self, deltaTime):

        if self.gold < 0:
            self.gameOver = True
            self.gold = 0

        if self.showTutorial:
            if self.tutCloseBtn.click():
                self.showTutorial = False

            if self.tutPreviousBtn.click():
                self.currentTutorialPage -= 1

            if self.tutNextBtn.click():
                self.currentTutorialPage += 1

        if not self.gameOver and not self.showTutorial:

            if self.spawnerIsActive:

                for enemySpawner in self.enemySpawnerObjects:
                    enemySpawner.update(deltaTime)

                self.spawnPauseTimer += deltaTime

                if self.spawnPauseTimer > self.pauseDuration:

                    self.spawnPauseTimer = 0
                    self.currentRound += 1
                    self.enemySpawnerObjects.append(EnemyWaveSpawner(self, self.currentRound))

            if not self.showTutorial:
                if not self.spawnerIsActive:
                    if self.startGameBtn.click():
                        self.spawnPauseTimer = self.pauseDuration
                        self.spawnerIsActive = True
                else:
                    if self.nextRoundBtn.click():  # Probably remove the function to go to the next round
                        self.spawnPauseTimer = 0
                        self.currentRound += 1
                        self.enemySpawnerObjects.append(EnemyWaveSpawner(self, self.currentRound))

        if not self.gameOver:
            self.allSprites.update(deltaTime)

        if not self.showTutorial:
            if self.currentShopSquare is not None and self.currentShopSquare.isDragginTurret and self.gold < self.currentShopSquare.price:
                self.currentShopSquare.isDragginTurret = False

            if self.currentShopSquare is not None:
                self.CheckHoverTurretCollision()

            if self.focusedSprite is not None and isinstance(self.focusedSprite, Enemy) and self.focusedSprite.hasDied:
                self.focusedSprite = None

            if self.focusedSprite is not None and isinstance(self.focusedSprite, Turret):
                if self.upgradeTurretSellButton.click():
                    self.focusedSprite.sellTurret()
                    self.focusedSprite = None

                if self.upgradeTurretUpgradeButton.click():
                    self.focusedSprite.upgradeTurret()

    def renderGameOverScreen(self, screen):

        self.gameOverLbl = self.gameOverFont.render("Game Over", True, [0, 0, 0])
        self.roundsSurvivedLbl = self.gameOverStatsFont.render("Final Round " + str(self.currentRound), True, [0, 0, 0])
        self.finalScoreLbl = self.gameOverStatsFont.render("Score " + str(self.score), True, [0, 0, 0])
        self.totalEnemiesKilledLbl = self.gameOverStatsFont.render("Enemies Killed " + str(self.totalEnemiesKilled), True, [0, 0, 0])

        self.gameOverOverlay.blit(self.gameOverLbl, (190, 20))
        self.gameOverOverlay.blit(self.roundsSurvivedLbl, (40, 170))
        self.gameOverOverlay.blit(self.finalScoreLbl, (40, 250))
        self.gameOverOverlay.blit(self.totalEnemiesKilledLbl, (40, 320))

        screen.blit(self.gameOverOverlay, (500, 150))

        self.backToMainMenuBtn.draw(screen)
        self.retryGameBtn.draw(screen)

        if self.backToMainMenuBtn.click():
            SceneManager.SceneManager.goToScene("TowerDefense.TowerDefenseMainMenuScene.TowerDefenseMainMenuScene")

        if self.retryGameBtn.click():
            SceneManager.SceneManager.goToScene("TowerDefense.Level1Scene.Level1Scene")

    def drawText(self, surface, text, color, rect, font, aa=False, bkg=None):
        rect = pygame.Rect(rect)
        y = rect.top
        lineSpacing = -2

        # get the height of the font
        fontHeight = font.size("Tg")[1]

        while text:
            i = 1

            # determine if the row of text will be outside our area
            if y + fontHeight > rect.bottom:
                break

            # determine maximum width of line
            while font.size(text[:i])[0] < rect.width and i < len(text):
                i += 1

            # if we've wrapped the text, then adjust the wrap to the last word
            if i < len(text):
                i = text.rfind(" ", 0, i) + 1

            # render the line and blit it to the surface
            if bkg:
                image = font.render(text[:i], 1, color, bkg)
                image.set_colorkey(bkg)
            else:
                image = font.render(text[:i], aa, color)

            surface.blit(image, (rect.left, y))
            y += fontHeight + lineSpacing

            # remove the text we just blitted
            text = text[i:]

        return text

    def renderEnemyStatsScreen(self, screen, enemyToShow):

        canvasRect = pygame.draw.rect(screen, [70, 50, 34], self.upgradeTurretRect)
        pygame.draw.rect(screen, [50, 30, 14], self.upgradeTurretRect, 3)  # Border

        self.scoreOnKill = 20
        self.goldOnKill = 100
        self.goldToSteal = 10

        if isinstance(enemyToShow, HorseRobber):
            horseHealthText = "Horse Health: " + str(enemyToShow.horseHealth)
            robberHealthText = "Robber Health: " + str(enemyToShow.robberHealth)
        else:
            healthText = "Health: " + str(enemyToShow.health)

        movementSpeed = "Speed: " + str(enemyToShow.movementSpeed)
        goldOnKillText = "Kill Gold: " + str(enemyToShow.goldOnKill)
        totalStolenGold = "Stolen Gold: " + str(enemyToShow.totalGoldOnEnemy)
        goldToStealText = "Gold To Steal: " + str(enemyToShow.goldToSteal)

        descriptionRect = pygame.Rect(0, 416, 260, 70)
        descriptionRect.centerx = canvasRect.centerx

        self.drawText(screen, enemyToShow.description, [0, 0, 0], descriptionRect, self.upgradeTurretDescriptionFont, True, None)

        self.focusedEnemyName = self.upgradeTurretStatsHeaderFont.render(enemyToShow.name, True, [0, 0, 0])

        if isinstance(enemyToShow, HorseRobber):
            self.focusedHorseHealth = self.upgradeTurretStatsFont.render(horseHealthText, True, [0, 0, 0])
            self.focusedRobberHealth = self.upgradeTurretStatsFont.render(robberHealthText, True, [0, 0, 0])
        else:
            self.focusedEnemyHealth = self.upgradeTurretStatsFont.render(healthText, True, [0, 0, 0])

        self.focusedEnemySpeed = self.upgradeTurretStatsFont.render(movementSpeed, True, [0, 0, 0])
        self.focusedEnemyGoldOnKill = self.upgradeTurretStatsFont.render(goldOnKillText, True, [0, 0, 0])
        self.focusedEnemyTotalStolenGold = self.upgradeTurretStatsFont.render(totalStolenGold, True, [0, 0, 0])
        self.focusedEnemyGoldToSteal = self.upgradeTurretStatsFont.render(goldToStealText, True, [0, 0, 0])

        screen.blit(self.focusedEnemyName, (canvasRect.centerx - int(self.focusedEnemyName.get_rect().width / 2), 380))

        if isinstance(enemyToShow, HorseRobber):

            screen.blit(self.focusedHorseHealth, (1326, 508))
            screen.blit(self.focusedRobberHealth, (1326, 538))
            screen.blit(self.focusedEnemySpeed, (1326, 568))
            screen.blit(self.focusedEnemyGoldOnKill, (1326, 598))
            screen.blit(self.focusedEnemyGoldToSteal, (1326, 628))
            screen.blit(self.focusedEnemyTotalStolenGold, (1326, 658))
        else:

            screen.blit(self.focusedEnemyHealth, (1326, 508))
            screen.blit(self.focusedEnemySpeed, (1326, 538))
            screen.blit(self.focusedEnemyGoldOnKill, (1326, 568))
            screen.blit(self.focusedEnemyGoldToSteal, (1326, 598))
            screen.blit(self.focusedEnemyTotalStolenGold, (1326, 628))

    def renderTurretUpgradeScreen(self, screen, turretToShow):

        spriteToShow = turretToShow

        canvasRect = pygame.draw.rect(screen, [70, 50, 34], self.upgradeTurretRect)
        pygame.draw.rect(screen, [50, 30, 14], self.upgradeTurretRect, 3)  # Border

        costText = "Cost: " + str(spriteToShow.totalGoldSpendOnTurret)
        damageText = "Damage: " + str(spriteToShow.damage)
        fireRateText = "Speed: " + str(spriteToShow.fireRate)
        rangeText = "Range: " + str(spriteToShow.range)

        if spriteToShow.isFocusedByUser:

            if spriteToShow.turretLevel < spriteToShow.turretMaxLevel:
                costText = "Cost: " + str(spriteToShow.totalGoldSpendOnTurret) + "       +" + str(spriteToShow.upgradeCost)  # 5 times spacebar
                damageText = "Damage: " + str(spriteToShow.damage) + "      +" + str(spriteToShow.nextLevelDamage - spriteToShow.damage)
                fireRateText = "Speed: " + str(spriteToShow.fireRate) + "      +" + str(spriteToShow.nextLevelFireRate - spriteToShow.fireRate)
                rangeText = "Range: " + str(spriteToShow.range) + "      +" + str(spriteToShow.nextLevelRange - spriteToShow.range)

            self.focusedTurretName = self.upgradeTurretStatsHeaderFont.render(spriteToShow.name + " Lvl " + str(spriteToShow.turretLevel), True, [0, 0, 0])
        else:
            self.focusedTurretName = self.upgradeTurretStatsHeaderFont.render(spriteToShow.name, True, [0, 0, 0])

        descriptionRect = pygame.Rect(0, 416, 260, 70)
        descriptionRect.centerx = canvasRect.centerx

        self.drawText(screen, spriteToShow.description, [0, 0, 0], descriptionRect, self.upgradeTurretDescriptionFont, True, None)

        self.focusedTurretCost = self.upgradeTurretStatsFont.render(costText, True, [0, 0, 0])
        self.focusedTurretDamage = self.upgradeTurretStatsFont.render(damageText, True, [0, 0, 0])
        self.focusedTurretFireRate = self.upgradeTurretStatsFont.render(fireRateText, True, [0, 0, 0])
        self.focusedTurretRange = self.upgradeTurretStatsFont.render(rangeText, True, [0, 0, 0])

        #Always display turret name
        screen.blit(self.focusedTurretName,
                    (canvasRect.centerx - int(self.focusedTurretName.get_rect().width / 2), 380))

        if not spriteToShow.isUpgrading:

            screen.blit(self.focusedTurretCost, (1326, 508))
            screen.blit(self.focusedTurretDamage, (1326, 538))
            screen.blit(self.focusedTurretFireRate, (1326, 568))
            screen.blit(self.focusedTurretRange, (1326, 598))

            if isinstance(spriteToShow, TntTurret):

                # TNT
                RadiusText = "Radius: " + str(spriteToShow.areaOfEffect)
                fuseTimeText = "FuseTime: " + str(spriteToShow.fuseTime)

                if spriteToShow.isFocusedByUser:

                    if spriteToShow.turretLevel < spriteToShow.turretMaxLevel:
                        RadiusText = "Radius: " + str(spriteToShow.areaOfEffect) + "     +" + str(spriteToShow.nextLevelAOE - spriteToShow.areaOfEffect)
                        fuseTimeText = "FuseTime: " + str(spriteToShow.fuseTime) + "   -" + str(spriteToShow.fuseTime - spriteToShow.nextLevelFuseTime)

                self.dynamiteStats = self.upgradeTurretStatsHeaderFont.render("Dynamite Stats", True, [0, 0, 0])
                self.focusedTurretAOE = self.upgradeTurretStatsFont.render(RadiusText, True, [0, 0, 0])
                self.focusedTurretFuseTime = self.upgradeTurretStatsFont.render(fuseTimeText, True, [0, 0, 0])

                screen.blit(self.dynamiteStats, (canvasRect.centerx - int(self.dynamiteStats.get_rect().width / 2), 640))

                screen.blit(self.focusedTurretAOE, (1326, 680))
                screen.blit(self.focusedTurretFuseTime, (1326, 710))

            if self.focusedSprite and isinstance(self.focusedSprite, Turret):
                self.upgradeTurretSellButton.draw(screen)

                if self.focusedSprite.turretLevel < self.focusedSprite.turretMaxLevel:
                    self.upgradeTurretUpgradeButton.draw(screen)
                    pygame.draw.rect(screen, [50, 30, 14], pygame.Rect(1462, 755, 115, 30), 3)

                pygame.draw.rect(screen, [50, 30, 14], pygame.Rect(1326, 755, 115, 30), 3)
        else:
            upgradeBarWidth = 250
            upgradeBarProgressWidth = (spriteToShow.upgradeTimer / spriteToShow.upgradeDuration * upgradeBarWidth)

            pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(canvasRect.centerx - (upgradeBarWidth / 2), canvasRect.centery, upgradeBarWidth, 24))
            pygame.draw.rect(screen, [70, 50, 34], pygame.Rect(canvasRect.centerx - (upgradeBarWidth / 2), canvasRect.centery, upgradeBarProgressWidth, 24))
            pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(canvasRect.centerx - (upgradeBarWidth / 2), canvasRect.centery, upgradeBarWidth, 24), 4)

            if self.focusedSprite and isinstance(self.focusedSprite, Turret):
                self.upgradeTurretSellButton.draw(screen)

            self.drawText(screen, "Making your turret more awesome!", [0, 0, 0], pygame.Rect(descriptionRect.centerx - 126, 620, 300, 70), self.upgradeTurretUpgradeTextFont, True, None)

    def renderTutorialScreen(self, screen):
        canvasRect = pygame.draw.rect(screen, [70, 50, 34], self.tutorialRect)
        pygame.draw.rect(screen, [50, 30, 14], self.tutorialRect, 3)  # Border

        screen.blit(self.tutorialImages[self.currentTutorialPage - 1], (400, 160))

        if self.currentTutorialPage == 1 or self.currentTutorialPage == 6:
            self.tutCloseBtn.draw(screen)

        if self.currentTutorialPage > 1:
            self.tutPreviousBtn.draw(screen)

        if self.currentTutorialPage >= 1 and self.currentTutorialPage < 6:
            self.tutNextBtn.draw(screen)

        if self.currentTutorialPage == 3:
            self.tutPreviousBtn.xPos = 634
            self.tutNextBtn.xPos = 872

            self.tutPreviousBtn.yPos = 505
            self.tutNextBtn.yPos = 505

        elif self.currentTutorialPage == 6:
            self.userAtLastPage = True
            self.tutPreviousBtn.xPos = 634
            self.tutCloseBtn.xPos = 872

            self.tutPreviousBtn.yPos = 495
            self.tutCloseBtn.yPos = 495
        else: # geen else maak een elif per page waar de buttons moeten
            self.tutPreviousBtn.xPos = 490
            self.tutNextBtn.xPos = 770

    def GetClosestEnemyToDestination(self, centerPos, radius, enemySprites):

        closestEnemyPosition = None
        closestEnemy = None

        for enemy in enemySprites:
            distanceToEnemy = centerPos.get_distance(enemy.position)

            if distanceToEnemy <= radius:
                if closestEnemyPosition is None:
                    closestEnemyPosition = enemy.distanceLeft
                    closestEnemy = enemy
                elif enemy.distanceLeft < closestEnemyPosition:
                    closestEnemyPosition = enemy.distanceLeft
                    closestEnemy = enemy

        return closestEnemy

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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.spawnerIsActive and not self.showTutorial:
                self.spawnPauseTimer = 0
                self.currentRound += 1
                self.enemySpawnerObjects.append(EnemyWaveSpawner(self, self.currentRound))

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not self.showTutorial and not self.gameOver:
                mousePos = pygame.mouse.get_pos()

                if self.sniperShopSquare.isDragginTurret == False and self.akimboShopSquare.isDragginTurret == False and self.tntShopSqaure.isDragginTurret == False:
                    spriteHasBeenFocused = False
                    for sprite in self.allSprites.sprites():

                        if sprite.rect.collidepoint(mousePos) and spriteHasBeenFocused == False:
                            spriteHasBeenFocused = True

                            if isinstance(sprite, Turret):
                                sprite.isFocusedByUser = True

                            self.focusedSprite = sprite
                        elif not self.rightHUDSideRect.collidepoint(mousePos) and not self.upperHUDSideRect.collidepoint(mousePos):
                            sprite.isFocusedByUser = False

                    if spriteHasBeenFocused == False and not self.rightHUDSideRect.collidepoint(mousePos) and not self.upperHUDSideRect.collidepoint(mousePos):
                        self.focusedSprite = None

                isMouseClickInsideUnplaceableBounds = False
                for turret in self.turretSprites.sprites():

                    if self.currentShopSquare is not None:
                        if turret.collisionRect.colliderect(self.currentShopSquare.collisionRect):
                            isMouseClickInsideUnplaceableBounds = True
                            break

                if isMouseClickInsideUnplaceableBounds == False:
                    for unplaceableBounds in self.unableToPlaceRects:

                        if self.currentShopSquare is not None:
                            if unplaceableBounds.colliderect(self.currentShopSquare.collisionRect):
                                isMouseClickInsideUnplaceableBounds = True
                                break

                if isMouseClickInsideUnplaceableBounds == False:

                    if self.currentShopSquare is not None:
                        self.turretPlacementSound.play()

                        if self.currentShopSquare.turretName == "Akimbo":# hier gebleven met self.currentShopSquare
                            AkimboRevolverTurret(Vector2(mousePos), self, self.allSprites, self.turretSprites)
                            self.gold -= self.currentShopSquare.price

                        elif self.currentShopSquare.turretName == "Tnt":
                            TntTurret(Vector2(mousePos), self, self.allSprites, self.turretSprites)
                            self.gold -= self.currentShopSquare.price

                        elif self.currentShopSquare.turretName == "Sniper":
                            SniperTurret(Vector2(mousePos), self, self.allSprites, self.turretSprites)
                            self.gold -= self.currentShopSquare.price

                        self.currentShopSquare.isDragginTurret = False
                        self.currentShopSquare = None
                else:
                    self.tntShopSqaure.isDragginTurret = False
                    self.akimboShopSquare.isDragginTurret = False
                    self.sniperShopSquare.isDragginTurret = False
                    self.currentShopSquare = None

                if self.gold >= self.akimboShopSquare.price and self.akimboShopSquare.isDragginTurret == False and self.akimboShopRect.collidepoint(mousePos):
                    self.akimboShopSquare.clicked()
                    self.currentShopSquare = self.akimboShopSquare

                    self.focusedSprite = None
                    for turret in self.turretSprites.sprites():
                        turret.isFocusedByUser = False

                if self.gold >= self.tntShopSqaure.price and self.tntShopSqaure.isDragginTurret == False and self.tntShopRect.collidepoint(mousePos):
                    self.tntShopSqaure.clicked()
                    self.currentShopSquare = self.tntShopSqaure

                    self.focusedSprite = None
                    for turret in self.turretSprites.sprites():
                        turret.isFocusedByUser = False

                if self.gold >= self.sniperShopSquare.price and self.sniperShopSquare.isDragginTurret == False and self.sniperShopRect.collidepoint(mousePos):
                    self.sniperShopSquare.clicked()
                    self.currentShopSquare = self.sniperShopSquare

                    self.focusedSprite = None
                    for turret in self.turretSprites.sprites():
                        turret.isFocusedByUser = False

            if event.type == pygame.MOUSEMOTION and not self.showTutorial and not self.gameOver:
                mousePos = pygame.mouse.get_pos()

                self.isHoveringOverAkimboShopRect = self.akimboShopRect.collidepoint(mousePos) # Mouse is hovering over this shop sqaure
                self.isHoveringOverTntShopRect = self.tntShopRect.collidepoint(mousePos) # Mouse is hovering over this shop sqaure
                self.isHoveringOverSniperShopRect = self.sniperShopRect.collidepoint(mousePos) # Mouse is hovering over this shop sqaure

                if self.isHoveringOverAkimboShopRect:
                    self.hoverTurretObject = self.akimboShopSquare.turretObject
                elif self.isHoveringOverTntShopRect:
                    self.hoverTurretObject = self.tntShopSqaure.turretObject
                elif self.isHoveringOverSniperShopRect:
                    self.hoverTurretObject = self.sniperShopSquare.turretObject

                if self.isHoveringOverAkimboShopRect == False and self.isHoveringOverTntShopRect == False and self.isHoveringOverSniperShopRect == False:
                    self.hoverTurretObject = None
            else:
                self.hoverTurretObject = None

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
                pass
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
            if self.currentShopSquare is not None and self.currentShopSquare.collisionRect is not None:

                if turret.collisionRect.colliderect(self.currentShopSquare.collisionRect):
                    turretIsInsideSomething = True
                    break

        if turretIsInsideSomething == False:
            for unplaceableBounds in self.unableToPlaceRects:

                if self.currentShopSquare is not None and self.currentShopSquare.collisionRect is not None:
                    if unplaceableBounds.colliderect(self.currentShopSquare.collisionRect):
                        turretIsInsideSomething = True
                        break

        if turretIsInsideSomething and self.currentShopSquare is not None:
            self.currentShopSquare.changeOutlineColor((255, 0, 0))

        else:
            self.currentShopSquare.changeOutlineColor((0, 0, 0))

    def getOutline(self, image, color=(0, 0, 0), threshold=127):
        mask = pygame.mask.from_surface(image, threshold)
        outline_image = pygame.Surface(image.get_size()).convert_alpha()
        outline_image.fill((0, 0, 0, 0))

        #outline_image = pygame.transform.rotozoom(outline_image, 0, 1)

        for point in mask.outline():
            outline_image.set_at(point, color)
        return outline_image