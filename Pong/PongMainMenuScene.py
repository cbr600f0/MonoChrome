import pygame
import SceneManager
from ButtonClass import Button

class PongMainMenuScene (SceneManager.Scene):

    def __init__(self):
        super(PongMainMenuScene, self).__init__()
        self.headerFont = pygame.font.SysFont("monospace", 72)
        self.myfont = pygame.font.SysFont("monospace", 48)
        self.SinglePlayerButton = Button(False, self.myfont, "Single player", (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0), 600, 225, 400, 75)
        self.MultiplayerButton = Button(False, self.myfont, "Multiplayer", (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0), 600, 325, 400, 75)
        self.ExitButton = Button(False, self.myfont, "Exit", (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0), 600, 525, 400, 75)
        self.InstructionsButton = Button(False, self.myfont, "Instructions", (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0), 600, 425, 400, 75)
        pygame.mixer.music.load("Pong/PongMusic.ogg")
        pygame.mixer.music.set_volume(0.0158)
        pygame.mixer.music.play(-1)

    def render(self, screen):
        screen.fill((0, 0, 0))

        #Main Menu Decoration

        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(0, 0, 60, 60))
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(1540, 0, 60, 60))
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(0, 840, 60, 60))
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(1540, 840, 60, 60))
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(60, 300, 60, 360))
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(1480, 300, 60, 360))

        #Main Menu Buttons

        self.SinglePlayerButton.draw(screen)
        self.MultiplayerButton.draw(screen)
        self.ExitButton.draw(screen)
        self.InstructionsButton.draw(screen)
        label = self.headerFont.render("PONG", 1, (255, 255, 255))
        screen.blit(label, (700, 100))

    def update(self, deltaTime):
        pressed = pygame.key.get_pressed()
        if self.SinglePlayerButton.click():
            SceneManager.SceneManager.goToScene("Pong.PongSinglePlayerScene.PongSinglePlayerScene")
        if self.MultiplayerButton.click():
            SceneManager.SceneManager.goToScene("Pong.PongMultiplayerScene.PongMultiplayerScene")
        if self.ExitButton.click():
            pygame.mixer.music.stop()
            SceneManager.SceneManager.goToScene("MainMenu.MainMenuScene.MainMenuScene")
        if self.InstructionsButton.click():
            SceneManager.SceneManager.goToScene("Pong.InstructionsScene.InstructionsScene")

    def handle_events(self, events):
        pass

