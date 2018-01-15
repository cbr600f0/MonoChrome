import sys, pygame, math, random, SceneManager, Vector2
from BubbleShooter2.Player import Player
from BubbleShooter2.LightBall import LightBall
from ButtonClass import Button

class GameOverScene(SceneManager.Scene):
    def __init__(self, *optionalSceneParam):
        super(GameOverScene, self).__init__()
        self.backgroundImage = pygame.image.load("BubbleShooter2\Images\GameOverImage.png")
        self.RetryButton = Button(True, None, "Retry", None, None, [0, 5, 255], [0, 5, 110], 715, 630, None, 82)
        self.MainMenuButton = Button(True, None, "Main Menu", None, None, [0, 5, 255], [0, 5, 110], 715, 730, None, 82)

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