import pygame, random
import SceneManager
from Vector2 import Vector2
from Pong.Player1 import Player1
from Pong.Ball import Ball
from Pong.Block import Block

class PongSinglePlayerScene (SceneManager.Scene):

    def __init__(self):
        super(PongSinglePlayerScene, self).__init__()
        self.allSprites = pygame.sprite.Group()
        self.ballSprites = pygame.sprite.Group()
        self.playerSprites = pygame.sprite.Group()
        self.blockSprites = pygame.sprite.Group()
        self.ball = Ball(self.allSprites, self.ballSprites)
        self.ballCollideSprites = pygame.sprite.Group()
        self.player1 = Player1(self.allSprites, self.playerSprites, self.ballCollideSprites)
        self.hasStarted = False
        self.is_white = True
        if self.is_white:
            self.color = (255, 255, 255)
        else:
            self.color = (0, 0, 0)
        self.level = 1
        self.block1 = Block(1550, random.randint(45, 650), self.allSprites, self.blockSprites, self.ballCollideSprites)
        self.block2 = Block(1550, random.randint(45, 650), self.allSprites, self.blockSprites, self.ballCollideSprites)
        self.ball.xVel = -self.ball.xVel
        self.myfont = pygame.font.SysFont("monospace", 26)
        self.ball.position = Vector2(850, 450)

    def render(self, screen):
        screen.fill((0, 0, 0))
        if self.hasStarted == False:

            Start = self.myfont.render("Press SPACE to start.", 1, (self.color))
            screen.blit(Start, (600, 250))
        self.allSprites.draw(screen)
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(0, 45, 1600, 5)) #barrier, scoreboard border
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(395, 0, 5, 45))  #scoreboard border
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(795, 0, 5, 45))  # scoreboard border
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(1195, 0, 5, 45))  # scoreboard border
        Points = self.myfont.render("Points:", 1, (0, 0, 0))
        screen.blit(Points, (15, 8))
        SinglePlayer = self.myfont.render("Mode: Single Player", 1, (255, 255, 255))
        screen.blit(SinglePlayer, (410, 8))
        Lives = self.myfont.render("Lives: 1", 1, (255, 255, 255))
        screen.blit(Lives, (805, 8))
        Level = self.myfont.render("Level: " + str(self.level), 1, (255, 255, 255))
        screen.blit(Level, (1210, 8))

    def update(self, deltaTime):
        if self.ball.position.x > 1539:
            self.block1.y = random.randint(45, 650)
            self.block2.y = random.randint(45, 650)
            self.ball.position = Vector2(720, 390)
            self.hasStarted = False
            self.is_white = True
            if self.ball.xVel > 0:
                self.ball.xVel = -self.ball.xVel
            self.ball.position = Vector2(850, 450)
            self.player1.x = 60
            self.player1.y = 420
            self.level += 1
        if self.ball.position.x < 1:
            SceneManager.SceneManager.goToScene("Pong.LoserScene.LoserScene")


        if self.hasStarted:

            self.allSprites.update(deltaTime, self.ballCollideSprites)
        pressed = pygame.key.get_pressed()


        if self.is_white:
            self.color = (255, 255, 255)
        else:
            self.color = (0, 0, 0)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.is_white = not self.is_white
                self.hasStarted = True
