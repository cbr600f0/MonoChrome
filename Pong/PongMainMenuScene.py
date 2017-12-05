import pygame
import SceneManager
from ButtonClass import Button
from Pong import PongMultiplayerScene

class PongMainMenuScene (SceneManager.Scene):

    def __init__(self):
        super(PongMainMenuScene, self).__init__()
        self.MultiplayerButton = Button("Multiplayer", (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0), 200, 200, 1300, 250)


    def render(self, screen):
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(0, 0, 60, 60))        #decoration
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(1540, 0, 60, 60))     #decoration
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(0, 840, 60, 60))      #decoration
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(1540, 840, 60, 60))   #decoration
        self.MultiplayerButton.draw(screen)

    def update(self, deltaTime):
        pressed = pygame.key.get_pressed()
        if(self.MultiplayerButton.click()):
            SceneManager.SceneMananger.currentScene = PongMultiplayerScene.PongMultiplayerScene()

    def handle_events(self, events):
        pass

