import pygame
from pygame import gfxdraw
from Scene import Scene as Scene
import SceneManager
from ButtonClass import Button
from Vector2D import Vector2D
from TowerDefense.Towers.AkimboRevolverTurret import AkimboRevolverTurret
from TowerDefense.Enemies.Robber import Robber

class Level1(Scene):

    def __init__(self):
        super(Level1, self).__init__()
        self.testTurret = AkimboRevolverTurret()
        self.testEnemy = Robber()

        self.enemySprites = pygame.sprite.Group(self.testEnemy)
        self.turretSprites = pygame.sprite.Group(self.testTurret)

        self.mainBG = pygame.Surface((1600, 900))
        self.mainBG.fill((220, 220, 220))

        self.backToMainMenuBtn = Button("Click to go back to the Main Menu", [220, 220, 220], [0, 0, 0], [120, 120, 120], [0, 0, 0], 30, 100, None, 40)

    def render(self, screen):
        self.enemySprites.clear(screen, self.mainBG)
        self.turretSprites.clear(screen, self.mainBG)

        screen.blit(self.mainBG, (0, 0))
        pygame.display.set_caption("Tower Defense (Press ESCAPE to close the game)")

        self.backToMainMenuBtn.draw(screen)

        self.enemySprites.draw(screen)
        self.turretSprites.draw(screen)

    def update(self, deltaTime):
        self.enemySprites.update(deltaTime)
        self.turretSprites.update(deltaTime)
        self.testTurret.PosToFollow = self.testEnemy.position

        if self.backToMainMenuBtn.click():
            SceneManager.SceneMananger.goToScene("TowerDefenseMainMenuScene")

    def handle_events(self, events):
        for event in events:
            pass