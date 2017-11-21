import pygame
from Scene import Scene as Scene
import SceneManager
from ButtonClass import Button

class PongScene (Scene):

    def __init__(self):
        super(PongScene, self).__init__()
        self.x = 30
        self.y = 330

    def render(self, screen):
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(self.x, self.y, 60, 240))

    def update(self, deltaTime):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: self.y -= 8
        if pressed[pygame.K_DOWN]: self.y += 8

    def handle_events(self, events):
        pass