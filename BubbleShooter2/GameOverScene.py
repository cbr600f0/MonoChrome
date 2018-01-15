import sys, pygame, math, random, SceneManager, Vector2
from BubbleShooter2.Player import Player
from BubbleShooter2.LightBall import LightBall
import ButtonClass as Button

class GameOverScene(SceneManager.Scene):
    def __init__(self, *optionalSceneParam):
        super(GameOverScene, self).__init__()
        self.backgroundImage = pygame.image.load("BubbleShooter2\Images\GameOverImage.png")
        self.RetryButton = Button.Button(True, None, "", (255, 0, 0), (255, 0, 0), (220, 220, 220), (220, 220, 220), 350, 700, 1280, 120)
        self.ManMenuButton = Button.Button(True, None, "", (255, 0, 0), (255, 0, 0), (220, 220, 220), (220, 220, 220), 600, 700, 1280, 120)

    def render(self, screen):
        screen.blit(self.backgroundImage, (0, 0))
        self.RetryButton.draw(screen)
        self.MainMenuButton.draw(screen)

    def handle_events(self, events):
        pass

    def update(self, deltaTime):
        if self.RetryButton.click():
            SceneManager.SceneManager.goToScene('BubbleShooter2.BubbleShooterScene.BubbleShooterScene', 1)
        if self.MainMenuButton.click():
            SceneManager.SceneManager.goToScene('BubbleShooter2.BubbleShooterMainMenuScene.BubbleShooterMainMenuScene')