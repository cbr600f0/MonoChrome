import pygame
import SceneManager
from ButtonClass import Button
from Pong import PongMultiplayerScene

class PongMainMenuScene (SceneManager.Scene):

    def __init__(self):
        super(PongMainMenuScene, self).__init__()
        self.SinglePlayerButton = Button("Single player", (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0), 400, 25, 800, 150)
        self.MultiplayerButton = Button("Multiplayer", (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0), 400, 200, 800, 150)
        self.InfiniteButton = Button("Infinite", (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0), 400, 375, 800, 150)
        self.AudioButton = Button("Audio", (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0), 400, 550, 800, 150)
        self.ExitButton = Button("Exit", (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0), 400, 725, 800, 150)


    def render(self, screen):
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(0, 0, 60, 60))        #decoration
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(1540, 0, 60, 60))     #|
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(0, 840, 60, 60))      #|
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(1540, 840, 60, 60))   #decoration
        self.SinglePlayerButton.draw(screen)                                        #button
        self.MultiplayerButton.draw(screen)                                         #|
        self.InfiniteButton.draw(screen)                                            #|
        self.AudioButton.draw(screen)                                               #|
        self.ExitButton.draw(screen)                                                #button

    def update(self, deltaTime):
        pressed = pygame.key.get_pressed()
        if self.MultiplayerButton.click():
            SceneManager.SceneManager.goToScene("Pong.PongMultiplayerScene.PongMultiplayerScene")
        if self.ExitButton.click():
            SceneManager.SceneManager.goToScene("MainMenuScene.MainMenuScene")

    def handle_events(self, events):
        pass

