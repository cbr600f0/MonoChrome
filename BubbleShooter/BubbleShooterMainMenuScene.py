import sys, pygame, math, SceneManager
from BubbleShooter import BubbleShooterScene
from pygame.locals import *
import ButtonClass as Button

class BubbleShooterMainMenuScene(SceneManager.Scene):

    def __init__(self):
        super(BubbleShooterMainMenuScene, self).__init__()
        pygame.init()
        # Sets the screen resolution and creates a variable to set other images' position

        self.screen = pygame.display.set_mode((1600, 900))
        # shows the mouse
        pygame.mouse.set_visible(True)

        # Adds buttons
        self.NewGameButton = Button.Button("", None, None, (220, 220, 220), (220, 220, 220), 180, 75, 1280, 120)
        self.PasswordButton = Button.Button("", None, None, (220, 220, 220), (220, 220, 220), 180, 280, 1280, 120)
        self.OptionsButton = Button.Button("", None, None, (220, 220, 220), (220, 220, 220), 180, 487, 1280, 120)
        self.QuitGameButton = Button.Button("", None, None,  (220, 220, 220), (220, 220, 220), 180, 690, 1280, 120)

    def render(self, screen):
        # Draws buttons
        self.NewGameButton.draw(screen)
        self.PasswordButton.draw(screen)
        self.OptionsButton.draw(screen)
        self.QuitGameButton.draw(screen)
        pass


    def handle_events(self, events):
        pass


    def update(self, deltaTime):
        # loads the background and changes it to fit the screen
        backgroundImage = pygame.image.load('BubbleShooter\Images\MainMenu.png').convert_alpha()
        backgroundImage = pygame.transform.scale(backgroundImage, (1600, 900))
        backgroundImageRect = backgroundImage.get_rect()
        self.screen.blit(backgroundImage, backgroundImageRect)
        pygame.display.update()

        if(self.NewGameButton.click()):
            SceneManager.SceneMananger.currentScene = BubbleShooterScene.BubbleShooterScene()
        if (self.PasswordButton.click()):
            pass
        if (self.OptionsButton.click()):
            pass
        if (self.QuitGameButton.click()):
            pass