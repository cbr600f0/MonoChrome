import pygame
from pygame import gfxdraw
from Scene import Scene as Scene
import SceneManager
from ButtonClass import Button


class TowerDefenseMainMenuScene(Scene):

    def __init__(self):
        super(TowerDefenseMainMenuScene, self).__init__()

        self.mainBG = pygame.image.load("TowerDefense\Images\MainMenu.png").convert()
        self.mainBG = pygame.transform.scale(self.mainBG, (1600, 900))
        self.backToMainMenuBtn = Button("Start", None, None, [120, 120, 120], [132, 115, 100], 715, 195, None, 70)

    def render(self, screen):
        screen.blit(self.mainBG, (0, 0))

        self.backToMainMenuBtn.draw(screen)

    def update(self, deltaTime):

        if self.backToMainMenuBtn.click():
            SceneManager.SceneMananger.goToScene("MainMenu")

    def handle_events(self, events):
        for event in events:
            pass