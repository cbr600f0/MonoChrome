import pygame
from pygame import gfxdraw
import SceneManager
from ButtonClass import Button


class TowerDefenseMainMenuScene(SceneManager.Scene):

    def __init__(self):
        super(TowerDefenseMainMenuScene, self).__init__()

        self.mainBG = pygame.image.load("TowerDefense\Images\MainMenu.png").convert()
        self.mainBG = pygame.transform.scale(self.mainBG, (1600, 900))
        self.startBtn = Button("Start", None, None, [120, 120, 120], [132, 115, 100], 715, 195, None, 70)

    def render(self, screen):
        screen.blit(self.mainBG, (0, 0))

        self.startBtn.draw(screen)

    def update(self, deltaTime):

        if self.startBtn.click():
            SceneManager.SceneMananger.goToScene("TowerDefense.Level1Scene.Level1Scene")

    def handle_events(self, events):
        for event in events:
            pass