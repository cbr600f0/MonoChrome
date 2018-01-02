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
        self.InfiniteButton = Button(False, self.myfont, "Infinite", (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0), 600, 425, 400, 75)
        self.AudioButton = Button(False, self.myfont, "Audio", (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0), 600, 525, 400, 75)
        self.ExitButton = Button( False, self.myfont, "Exit", (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0), 600, 625, 400, 75)

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
        self.InfiniteButton.draw(screen)
        self.AudioButton.draw(screen)
        self.ExitButton.draw(screen)
        label = self.headerFont.render("PONG", 1, (255, 255, 255))
        screen.blit(label, (700, 100))

    def update(self, deltaTime):
        pressed = pygame.key.get_pressed()
        if self.SinglePlayerButton.click():
            SceneManager.SceneManager.goToScene("Pong.PongSinglePlayerScene.PongSinglePlayerScene")
        if self.MultiplayerButton.click():
            SceneManager.SceneManager.goToScene("Pong.PongMultiplayerScene.PongMultiplayerScene")
        if self.InfiniteButton.click():
            SceneManager.SceneManager.goToScene("Pong.PongInfiniteScene.PongInfiniteScene")
        if self.ExitButton.click():
            SceneManager.SceneManager.goToScene("MainMenu.MainMenuScene.MainMenuScene")
        if pressed[pygame.K_1]:
            SceneManager.SceneManager.goToScene("Pong.Player1VictoryScene.Player1VictoryScene")
        if pressed[pygame.K_2]:
            SceneManager.SceneManager.goToScene("Pong.Player2VictoryScene.Player2VictoryScene")

    def handle_events(self, events):
        pass

