import sys, pygame, math, SceneManager
import ButtonClass as Button

class BubbleShooterMainMenuScene(SceneManager.Scene):

    def __init__(self):
        super(BubbleShooterMainMenuScene, self).__init__()

        pygame.mixer.music.load("BubbleShooter2/Sound/BackgroundSong.mp3")
        pygame.mixer.music.set_volume(0.0158)
        pygame.mixer.music.play(-1)

        # Adds buttons
        self.NewGameButton = Button.Button(True, None, "", None, None, (220, 220, 220), (220, 220, 220), 180, 305, 1280, 120)
        self.QuitGameButton = Button.Button(True, None, "", None, None,  (220, 220, 220), (220, 220, 220), 180, 583, 1280, 120)

        self.backgroundImage = pygame.image.load('BubbleShooter2\Images\MainMenu.png').convert_alpha()
        self.backgroundImage = pygame.transform.scale(self.backgroundImage, (1600, 900))
        self.backgroundImageRect = self.backgroundImage.get_rect()

    def render(self, screen):
        screen.blit(self.backgroundImage, self.backgroundImageRect)
        # Draws buttons
        self.NewGameButton.draw(screen)
        self.QuitGameButton.draw(screen)

    def handle_events(self, events):
        pass


    def update(self, deltaTime):
        if(self.NewGameButton.click()):
            SceneManager.SceneManager.goToScene('BubbleShooter2.BubbleShooterScene.BubbleShooterScene', 1)
        if (self.QuitGameButton.click()):
            pygame.mixer.music.stop()
            SceneManager.SceneManager.goToScene('MainMenu.MainMenuScene.MainMenuScene')