import pygame
import SceneManager
from ButtonClass import Button

class PongMainMenuScene (SceneManager.Scene):

    def __init__(self):
        super(PongMainMenuScene, self).__init__()


    def render(self, screen):
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(0, 0, 60, 60))
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(1540, 0, 60, 60))
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(0, 840, 60, 60))
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(1540, 840, 60, 60))
        

    def update(self, deltaTime):
        pressed = pygame.key.get_pressed()


    def handle_events(self, events):
        pass

