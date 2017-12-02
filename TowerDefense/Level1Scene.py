import pygame, random, SceneManager
from ButtonClass import Button
from Vector2D import Vector2D
from TowerDefense.Towers.AkimboRevolverTurret import AkimboRevolverTurret
from TowerDefense.Enemies.Robber import Robber


class Level1Scene(SceneManager.Scene):

    def __init__(self):
        super(Level1Scene, self).__init__()
        self.spawnTimer = 0

        #Gameobject stuff
        self.allSprites = pygame.sprite.Group()
        self.enemySprites = pygame.sprite.Group()
        self.turretSprites = pygame.sprite.Group()
        self.bulletSprites = pygame.sprite.Group()

        # Immediately spawn a number of enemies
        for i in range(0):
            spawnPos = Vector2D(random.randrange(10, 1500), random.randrange(10, 800))
            Robber(spawnPos, self.allSprites, self.enemySprites)

        AkimboRevolverTurret(Vector2D(800, 450), self.allSprites, self.turretSprites)

        # Interface Stuff
        self.mainBG = pygame.Surface((1600, 900))
        self.mainBG.fill((0, 40, 0))
        self.backToMainMenuBtn = Button("Main menu", None, None, [120, 120, 120], [117, 100, 85], 100, 100, None, 70)

        self.enemiesAliveFont = pygame.font.SysFont("monospace", 22)
        self.totalAliveEnemiesLbl = self.enemiesAliveFont.render("Enemies alive: " + str(len(self.enemySprites.sprites())), 1, (255, 255, 255))

    def render(self, screen):
        self.allSprites.clear(screen, self.mainBG)

        screen.blit(self.mainBG, (0, 0))

        self.backToMainMenuBtn.draw(screen)

        self.allSprites.draw(screen)

        screen.blit(self.totalAliveEnemiesLbl, (240, 2))

    def update(self, deltaTime):
        self.spawnTimer += deltaTime

        if self.spawnTimer > 0.8:
            spawnPos = Vector2D(random.randrange(0, 1600), random.randrange(0, 900))
            Robber(spawnPos, self.allSprites, self.enemySprites)
            self.spawnTimer = 0

        self.allSprites.update(deltaTime, self.allSprites, self.turretSprites, self.enemySprites, self.bulletSprites)

        if self.backToMainMenuBtn.click():
            SceneManager.SceneMananger.goToScene("TowerDefense.TowerDefenseMainMenuScene.TowerDefenseMainMenuScene")

        self.totalAliveEnemiesLbl = self.enemiesAliveFont.render("Enemies alive: " + str(len(self.enemySprites.sprites())), 1, (255, 255, 255))

    def handle_events(self, events):
        for event in events:
            pass