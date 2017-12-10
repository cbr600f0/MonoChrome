import pygame, random, SceneManager
from ButtonClass import Button
from Vector2 import Vector2
from TowerDefense.Towers.AkimboRevolverTurret import AkimboRevolverTurret
from TowerDefense.Enemies.Robber import Robber


class Level1Scene(SceneManager.Scene): # create a ONScenePlay method and make it so that people can send parameters with it to the new scene via Scenemanager.goToScene()

    def __init__(self, *optionalInformation):
        super(Level1Scene, self).__init__()
        self.spawnTimer = 0
        self.linePositions = ([1000, 980], [1000, 500], [1200, 500], [1200, 180], [120, 180], [120, 800], [320, 800], [320, 500], [800, 500], [800, 980])

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
        self.numberOfEnemiesToSpawn = 10
        self.numberOfEnemiesSpawnedThisRound = 0
        self.currentRound = 1

        # Immediately spawn a number of enemies
        for i in range(0):
            Robber(self.linePositions, self, self.allSprites, self.enemySprites)

        # Interface Stuff
        self.mainBG = pygame.Surface((1600, 900))
        self.mainBG.fill([100, 80, 63])

        self.backToMainMenuBtn = Button("Main menu", None, None, [120, 120, 120], [117, 100, 85], 100, 80, None, 70)
        self.nextRoundBtn = Button("Next Round", None, None, [40, 40, 40], [0, 0, 0], 1324, 820, None, 60)

        self.westernFont = pygame.font.Font("TowerDefense\WesternFont.otf", 28)
        self.difficultyLbl = self.westernFont.render("Difficulty: " + str(self.difficulty), True, [0, 0, 0])
        self.scoreLbl = self.westernFont.render("Score: " + str(self.score), True, [0, 0, 0])
        self.goldLbl = self.westernFont.render("Gold: " + str(self.gold), True, [0, 0, 0])
        self.roundLbl = self.westernFont.render("Round: " + str(self.currentRound), True, [0, 0, 0])

    def render(self, screen):
        self.allSprites.clear(screen, self.mainBG)

        screen.blit(self.mainBG, (0, 0))

        self.renderPath(screen)
        self.allSprites.draw(screen)
        self.renderHud(screen)

        self.backToMainMenuBtn.draw(screen)
        self.nextRoundBtn.draw(screen)

    def update(self, deltaTime):

        if self.spawnerIsActive:
            self.spawnTimer += deltaTime

            if self.numberOfEnemiesSpawnedThisRound < self.numberOfEnemiesToSpawn:
                if self.spawnTimer > 1.2:
                    Robber(self.linePositions, self, self.allSprites, self.enemySprites)
                    self.numberOfEnemiesSpawnedThisRound += 1
                    self.spawnTimer = 0

            else:
                self.beginNextRound()

        self.allSprites.update(deltaTime, self.allSprites, self.turretSprites, self.enemySprites, self.bulletSprites)

        if self.backToMainMenuBtn.click():
            SceneManager.SceneManager.goToScene("TowerDefense.TowerDefenseMainMenuScene.TowerDefenseMainMenuScene")

        if self.nextRoundBtn.click():
            pass  # next round logic here

    def getEnemiesInArea(self, centerPos, radius, enemySprites):

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

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                mousePos = pygame.mouse.get_pos()
                AkimboRevolverTurret(Vector2(mousePos[0], mousePos[1]), self, self.allSprites, self.turretSprites)

    def renderPath(self, screen):
        COLOR = [80, 60, 44]

        pygame.draw.lines(screen, COLOR, False, self.linePositions, 66)

    def renderHud(self, screen):

        self.difficultyLbl = self.westernFont.render("Difficulty: " + str(self.difficulty), True, [0, 0, 0])
        self.scoreLbl = self.westernFont.render("Score: " + str(self.score), True, [0, 0, 0])
        self.roundLbl = self.westernFont.render("Round: " + str(self.currentRound), True, [0, 0, 0])
        self.goldLbl = self.westernFont.render("Gold: " + str(self.gold), True, [0, 0, 0])

        # Top
        pygame.draw.line(screen, [50, 30, 14], (0, 70), (1600, 70), 4) # Top Border
        pygame.draw.rect(screen, [80, 60, 44], pygame.Rect(0, 0, 1600, 70))

        screen.blit(self.difficultyLbl, (130, 6))
        pygame.draw.line(screen, [50, 30, 14], (500, 0), (500, 70), 4)
        screen.blit(self.scoreLbl, (850, 6))
        screen.blit(self.roundLbl, (850, 100))
        screen.blit(self.goldLbl, (1400, 6))

        # Right
        pygame.draw.rect(screen, [80, 60, 44], pygame.Rect(1300, 73, 300, 827))
        pygame.draw.line(screen, [50, 30, 14], (1300, 0), (1300, 900), 4)

        # Right Bottom
        pygame.draw.line(screen, [50, 30, 14], (1300, 800), (1600, 800), 4)

    def beginNextRound(self):
        self.numberOfEnemiesToSpawn += 1
        self.currentRound += 1
        self.numberOfEnemiesSpawnedThisRound = 0
        self.spawnTimer = 0