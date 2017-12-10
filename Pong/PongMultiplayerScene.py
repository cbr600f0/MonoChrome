import pygame
import SceneManager
from ButtonClass import Button
from Pong.Ball import Ball
from Vector2 import Vector2
from Pong.Player1 import Player1
from Pong.Player2 import Player2

class PongMultiplayerScene (SceneManager.Scene):

    def __init__(self):
        super(PongMultiplayerScene, self).__init__()
        self.allSprites = pygame.sprite.Group()
        self.ballSprites = pygame.sprite.Group()
        self.playerSprites = pygame.sprite.Group()
        Ball(Vector2(720, 390), self.allSprites, self.ballSprites)
        Player1(self.allSprites, self.playerSprites)
        Player2(self.allSprites, self.playerSprites)

        self.myfont = pygame.font.SysFont("monospace", 26)

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.allSprites.draw(screen)
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(0, 45, 1600, 5)) #barrier, scoreboard border
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(395, 0, 5, 45))  #scoreboard border
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(795, 0, 5, 45))  # scoreboard border
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(1195, 0, 5, 45))  # scoreboard border
        Multiplayer = self.myfont.render("Mode: Multiplayer", 1, (255, 255, 255))
        screen.blit(Multiplayer, (410, 8))
        P1Lives = self.myfont.render("P1 Lives:", 1, (255, 255, 255))
        screen.blit(P1Lives, (15, 8))
        P2Lives = self.myfont.render("P2 Lives:", 1, (255, 255, 255))
        screen.blit(P2Lives, (1210, 8))


    def update(self, deltaTime):
        self.allSprites.update(deltaTime)
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_BACKSPACE]:
            SceneManager.SceneManager.goToScene("Pong.PongMainMenuScene.PongMainMenuScene")

    def handle_events(self, events):
        pass
