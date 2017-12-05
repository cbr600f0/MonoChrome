import pygame
from Scene import Scene as Scene
import SceneManager
from ButtonClass import Button
from Vector2D import Vector2D

class DXBallMainMenuScene (Scene):

    def __init__(self):
        super(DXBallMainMenuScene, self).__init__()
        self.x = 800    #player
        self.y = 750   #player
        self.isPaused = False
        self.pausedSurface = pygame.Surface((1600, 900))
        self.pausedSurface.set_alpha(90)
        self.pausedSurface.fill((150, 46, 91))

    def render(self, screen):
        width = screen.width
        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(self.x, self.y, 240, 30)) #paddle

        pygame.draw.rect(screen, [153, 255, 153], pygame.Rect(720, 390, 60, 60)) #ball
        if self.isPaused:
            screen.blit(self.pausedSurface, (0, 0))

    def paused(self):
        pass

    def update(self, deltaTime):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]: self.x += 500 * deltaTime
        if pressed[pygame.K_LEFT]: self.x -= 500 * deltaTime
        if self.x < 0:
            self.x = 0
        if self.x > 1360:
            self.x = 1360
        if pressed[pygame.K_p]: self.isPaused = True
        if pressed[pygame.K_o]: self.isPaused = False


    def handle_events(self, events):
        pass
