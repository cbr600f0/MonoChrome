import pygame
import SceneManager
from ButtonClass import Button

class PongMainScene (SceneManager.Scene):

    def __init__(self):
        super(PongMainScene, self).__init__()
        self.player1x = 30     #player 1x
        self.player1y = 330    #player 1y
        self.player2x = 1510   #player 2x
        self.player2y = 330    #player 2y

    def render(self, screen):
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(self.player1x, self.player1y, 60, 240)) #player 1
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(720, 390, 60, 60)) #ball
        pygame.draw.rect(screen,[255, 255, 255], pygame.Rect(self.player2x, self.player2y, 60, 240))   #player 2


    def update(self, deltaTime):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]: self.player1y -= 200 * deltaTime    #player 1 movement up
        if pressed[pygame.K_s]: self.player1y += 200 * deltaTime    #player 1 movement down
        if pressed[pygame.K_UP]: self.player2y -= 200 * deltaTime   #player 2 movement up
        if pressed[pygame.K_DOWN]: self.player2y += 200 * deltaTime #player 2 movement down


    def handle_events(self, events):
        pass

