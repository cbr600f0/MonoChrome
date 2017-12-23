import sys, pygame, math, SceneManager
import ButtonClass as Button

class BubbleShooterMainMenuScene(SceneManager.Scene):

    def __init__(self):
        super(BubbleShooterMainMenuScene, self).__init__()

        # Adds buttons
        self.NewGameButton = Button.Button(True, None, "", None, None, (220, 220, 220), (220, 220, 220), 180, 75, 1280, 120)
        self.PasswordButton = Button.Button(True, None, "", None, None, (220, 220, 220), (220, 220, 220), 180, 280, 1280, 120)
        self.OptionsButton = Button.Button(True, None, "", None, None, (220, 220, 220), (220, 220, 220), 180, 487, 1280, 120)
        self.QuitGameButton = Button.Button(True, None, "", None, None,  (220, 220, 220), (220, 220, 220), 180, 690, 1280, 120)

        self.backgroundImage = pygame.image.load('BubbleShooter2\Images\MainMenu.png').convert_alpha()
        self.backgroundImage = pygame.transform.scale(self.backgroundImage, (1600, 900))
        self.backgroundImageRect = self.backgroundImage.get_rect()

    def render(self, screen):
        screen.blit(self.backgroundImage, self.backgroundImageRect)
        # Draws buttons
        self.NewGameButton.draw(screen)
        self.PasswordButton.draw(screen)
        self.OptionsButton.draw(screen)
        self.QuitGameButton.draw(screen)

    def handle_events(self, events):
        pass


    def update(self, deltaTime):
        if(self.NewGameButton.click()):
            SceneManager.SceneManager.goToScene('BubbleShooter2.BubbleShooterScene.BubbleShooterScene')
        if (self.PasswordButton.click()):
            pass
        if (self.OptionsButton.click()):
            pass
        if (self.QuitGameButton.click()):
            SceneManager.SceneManager.goToScene('MainMenu.MainMenuScene.MainMenuScene')