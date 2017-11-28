import pygame
from Scene import Scene as Scene
import SceneManager
from ButtonClass import Button

class PongScene (Scene):

    def __init__(self):
        super(PongScene, self).__init__()
        self.x = 30     #player
        self.y = 330    #player 

    def render(self, screen):
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(self.x, self.y, 60, 240)) #paddle
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(1540, 0, 60, 400)) #backwall
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(1540, 500, 60, 900)) #backwall
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(720, 390, 60, 60)) #ball

    def update(self, deltaTime):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: self.y -= 200 * deltaTime
        if pressed[pygame.K_DOWN]: self.y += 200 * deltaTime


    def handle_events(self, events):
        pass
