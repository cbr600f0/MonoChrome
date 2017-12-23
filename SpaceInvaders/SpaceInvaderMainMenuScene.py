import pygame
import SceneManager
from ButtonClass import Button

class SpaceInvaderMainMenuScene (SceneManager.Scene):

    def __init__(self):
        super(SpaceInvaderMainMenuScene, self).__init__()

        self.mainBG = pygame.image.load("SpaceInvaders/images/Start menu.png").convert()
        self.mainBG = pygame.transform.scale(self.mainBG, (1600, 900))

        self.startBtn   = Button("Start",               None, None, [47, 253, 39], [255, 255, 255], 50, 250, None, 120)
        self.optionsBtn = Button("Options",             None, None, [47, 253, 39], [255, 255, 255], 50, 400, None, 120)
        self.quitBtn    = Button("Quit to main menu",   None, None, [47, 253, 39], [255, 255, 255], 50, 550, None, 120)

    def handle_events(self, events):
        for event in events:
            pass

    def update(self, deltaTime):
        if self.startBtn.click():
            SceneManager.SceneManager.goToScene("SpaceInvaders.SpaceInvaderLevelScene.SpaceInvaderLevelScene")

        if self.optionsBtn.click():
            pass

        if self.quitBtn.click():
            SceneManager.SceneManager.goToScene("MainMenuScene.MainMenuScene")

    def render(self, screen):
        screen.blit(self.mainBG, (0, 0))
        self.startBtn.draw(screen)
        self.optionsBtn.draw(screen)
        self.quitBtn.draw(screen)

        # Draw highscore wave