import sys, pygame, math, SceneManager
from BubbleShooter import BubbleShooterScene
from pygame.locals import *

class BubbleShooterMainMenuScene(SceneManager.Scene):

    def __init__(self):
        super(BubbleShooterMainMenuScene, self).__init__()
        pygame.init()
        # Sets the screen resolution and creates a variable to set other images' position

        self.screen = pygame.display.set_mode((1600, 900))
        # shows the mouse
        pygame.mouse.set_visible(True)

    def render(self, screen):
        pass


    def handle_events(self, events):
        pass


    def update(self, deltaTime):
        while True:
            # loads the background and changes it to fit the screen
            backgroundImage = pygame.image.load('BubbleShooter\Images\MainMenu.png').convert_alpha()
            backgroundImage = pygame.transform.scale(backgroundImage, (1600, 900))
            backgroundImageRect = backgroundImage.get_rect()
            self.screen.blit(backgroundImage, backgroundImageRect)
            pygame.display.update()


            # SceneManager.SceneMananger.currentScene = BubbleShooterScene.BubbleShooterScene()