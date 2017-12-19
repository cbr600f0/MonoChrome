import pygame
import SceneManager
from ButtonClass import Button
from Vector2 import Vector2
from SpaceInvaders.enemy.Enemy import Enemy
from SpaceInvaders.player.Player import Player

class SpaceInvaderLevelScene (SceneManager.Scene):

    def __init__(self):
        # get the methods and variables from the base class which is Scene
        super(SpaceInvaderLevelScene, self).__init__()

    # Background
        self.mainBG_1 = pygame.image.load("SpaceInvaders/images/Background.png").convert()
        self.mainBG_1 = pygame.transform.scale(self.mainBG_1, (1600, 900))
        self.mainBG_2 = self.mainBG_1
        self.mainBG_Y_Speed = 900

    # Font
        self.spaceFont = pygame.font.Font("SpaceInvaders/font/OCRAEXT.TTF", 32)

    # BG settings
        self.BGSound = pygame.mixer.Sound("SpaceInvaders/audio/Shooting_Stars_8_bit.ogg")
        self.BGSound.play(-1)

    # Sprite groups
        self.allSprites = pygame.sprite.Group()
        self.enemySprites = pygame.sprite.Group()
        self.playerSprites = pygame.sprite.Group()
        self.bulletSprites = pygame.sprite.Group()

    # Setting
        self.wave = 0
        self.wavesLbl = ""
        self.showNextWave = False
        self.countDownTimer = 3

    # Create player
        Player(Vector2(750, 750), self.allSprites, self.playerSprites)

    def handle_events(self, events):
        pass

    def enemyCreate(self):
        for i in range(4):
            for j in range(10):
                spawnPos = Vector2(50 + (j * 50), 100 + (i * 50))
                Enemy(spawnPos, i, self.allSprites, self.enemySprites)

    def update(self, deltaTime):
        # Countdown
        if self.showNextWave:
            if self.countDownTimer >= 0:
                self.countDownTimer -= deltaTime
            else:
                self.countDownTimer = 3
                self.showNextWave = False

        # Background animation
        if self.mainBG_Y_Speed <= 900:
            self.mainBG_Y_Speed += (300 * deltaTime * ((self.wave / 10) + 1))
        else:
            self.mainBG_Y_Speed = 0

        # Create wave
        if len(self.enemySprites) == 0:
            self.wave += 1
            self.showNextWave = True
            self.enemyCreate()

        if self.showNextWave != True:
            self.allSprites.update(deltaTime, self.allSprites, self.enemySprites, self.playerSprites, self.bulletSprites)

    def render(self, screen):
        screen.fill((0, 0, 0))  # Create screen
        screen.blit(self.mainBG_1, (0, self.mainBG_Y_Speed))
        screen.blit(self.mainBG_2, (0, self.mainBG_Y_Speed - 900))

        self.wavesLbl = self.spaceFont.render("Wave: " + str(self.wave), True, [255, 255, 255])
        screen.blit(self.wavesLbl, (1300, 10))

        if self.showNextWave:
            self.timerLbl = self.spaceFont.render(str(self.countDownTimer), True, [255, 255, 255])
            screen.blit(self.timerLbl, (900, 400))

        self.allSprites.draw(screen)

        # Draw lives