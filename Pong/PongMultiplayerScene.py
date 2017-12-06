import pygame
import SceneManager
from ButtonClass import Button
from Pong.Ball import Ball
from Vector2D import Vector2D

class PongMultiplayerScene (SceneManager.Scene):

    def __init__(self):
        super(PongMultiplayerScene, self).__init__()
        self.player1x = 30     #player 1x
        self.player1y = 330    #player 1y
        self.player2x = 1540   #player 2x
        self.player2y = 330    #player 2y
        self.allSprites = pygame.sprite.Group()
        self.ballSprites = pygame.sprite.Group()
        Ball(Vector2D(720, 390), self.allSprites, self.ballSprites)

    def render(self, screen):
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(self.player1x, self.player1y, 30, 180)) #player 1
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(self.player2x, self.player2y, 30, 180))   #player 2
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(0, 45, 1600, 5)) #barrier, scoreboard border
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(395, 0, 5, 45))  #scoreboard border
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(795, 0, 5, 45))  # scoreboard border
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(1195, 0, 5, 45))  # scoreboard border
        self.allSprites.draw(screen)                                            #ball


    def update(self, deltaTime):
        self.allSprites.update(deltaTime)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.player1y -= 500 * deltaTime    #player 1 movement up
        if pressed[pygame.K_s]:
            self.player1y += 500 * deltaTime    #player 1 movement down
        if self.player1y < 50:
            self.player1y = 50
        if self.player1y > 720:
            self.player1y = 720
        if pressed[pygame.K_UP]:
            self.player2y -= 500 * deltaTime   #player 2 movement up
        if pressed[pygame.K_DOWN]:
            self.player2y += 500 * deltaTime #player 2 movement down
        if self.player2y < 50:
            self.player2y = 50
        if self.player2y > 720:
            self.player2y = 720
        if pressed[pygame.K_BACKSPACE]:
            SceneManager.SceneManager.goToScene("Pong.PongMainMenuScene.PongMainMenuScene")

    def handle_events(self, events):
        pass
