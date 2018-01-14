import pygame, math
import SceneManager
from ButtonClass import Button
from Vector2 import Vector2
from SpaceInvaders.enemy.Enemy import Enemy
from SpaceInvaders.enemy.EnemyBoss import EnemyBoss
from SpaceInvaders.player.Player import Player


class SpaceInvaderLevelScene(SceneManager.Scene):

    def __init__(self, *optionalSceneParam):
        # get the methods and variables from the base class which is Scene
        super(SpaceInvaderLevelScene, self).__init__()

        # Background
        self.mainBG_1 = pygame.image.load("SpaceInvaders/images/Background.png").convert()
        self.mainBG_1 = pygame.transform.scale(self.mainBG_1, (1600, 900))
        self.mainBG_2 = self.mainBG_1
        self.mainBG_Y_Speed = 900

        # Lives
        self.livesImage1 = pygame.image.load("SpaceInvaders/images/Lives.png").convert_alpha()
        self.livesImage1 = pygame.transform.scale(self.livesImage1, (50, 50))
        self.livesImage2 = self.livesImage1
        self.livesImage3 = self.livesImage1

        # Font
        self.spaceFont = pygame.font.Font("SpaceInvaders/font/OCRAEXT.TTF", 32)

        # Sprite groups
        self.allSprites = pygame.sprite.Group()
        self.enemySprites = pygame.sprite.Group()
        self.playerSprites = pygame.sprite.Group()
        self.bulletSprites = pygame.sprite.Group()
        self.bossSprites = pygame.sprite.Group()

        # Setting
        self.wave = 0
        self.wavesLbl = ""
        self.timerLbl = ""
        self.showNextWave = False
        self.countDownTimer = 3
        self.enemyReachedLastRow = ""
        self.bossLives = 0
        self.bossOriginalLives = 0

        # Create player
        Player(Vector2(750, 750), self.allSprites, self.playerSprites)
        self.lives = ""

        # Get audio settings
        if optionalSceneParam[0][0] != None:
            self.audio = optionalSceneParam[0][0]
        else:
            self.audio = True

        # BG settings
        #self.BGSound = pygame.mixer.Sound("SpaceInvaders/audio/Shooting_Stars_8_bit.ogg")
        self.BGSound = pygame.mixer.music.load("SpaceInvaders/audio/Shooting_Stars_8_bit.ogg")

        if self.audio:
            #self.BGSound.play(-1)
            pygame.mixer.music.play(-1, 0.0)

        # Get previous high score
        if optionalSceneParam[0][1] != None:
            self.highestWave = optionalSceneParam[0][1]
        else:
            self.highestWave = 0

    def handle_events(self, events):
        pass

    def bossCreate(self):
        spawnPos = Vector2(800, 250)
        EnemyBoss(spawnPos, self.allSprites, self.bossSprites)

    def enemyCreate(self):
        for i in range(4):
            for j in range(10):
                spawnPos = Vector2(50 + (j * 50), 100 + (i * 50))
                Enemy(spawnPos, i, self.allSprites, self.enemySprites)

    def getAudio(self):
        return self.audio

    def update(self, deltaTime):

        # Countdown logic
        if self.showNextWave:
            if self.countDownTimer >= 0:
                self.countDownTimer -= deltaTime
            else:
                self.countDownTimer = 3
                self.showNextWave = False

        # Background animation
        if self.mainBG_Y_Speed <= 900:
            self.mainBG_Y_Speed += (300 * deltaTime * ((self.wave / 40) + 1))
        else:
            self.mainBG_Y_Speed = 0

        # Create wave
        if len(self.enemySprites) == 0 and len(self.bossSprites) == 0:
            for bulletSettings in pygame.sprite.RenderUpdates(self.bulletSprites):
                bulletSettings.kill()

            self.wave += 1
            self.showNextWave = True

            # Type of battle
            if self.wave % 10 == 0:
                self.bossCreate()
            else:
                self.enemyCreate()

        # Get player lives
        for playerSettings in pygame.sprite.GroupSingle(self.playerSprites):
            self.lives = str(playerSettings.getLives())
            playerSettings.setAudio(self.audio)

        # Get and Set enemy setting
        for enemySettings in pygame.sprite.RenderUpdates(self.enemySprites):
            self.enemyReachedLastRow = enemySettings.getLastRowInfo()
            enemySettings.setWave(self.wave)
            enemySettings.setAudio(self.audio)

        # Get and Set boss setting
        for bossSettings in pygame.sprite.RenderUpdates(self.bossSprites):
            self.bossLives = bossSettings.getLives()
            self.bossOriginalLives = bossSettings.getOriginalLives()
            bossSettings.setAudio(self.audio)

        # Lives == 0 or enemies reached bottom
        if self.lives <= str(0) or self.enemyReachedLastRow:
            SceneManager.SceneManager.goToScene("SpaceInvaders.SpaceInvaderGameOverScene.SpaceInvaderGameOverScene", self.audio, str(self.wave), str(self.highestWave))

        # Only move when timer is turned off
        if self.showNextWave != True:
            self.allSprites.update(deltaTime, self.allSprites, self.enemySprites, self.playerSprites, self.bulletSprites, self.bossSprites)

    def render(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.mainBG_1, (0, self.mainBG_Y_Speed))
        screen.blit(self.mainBG_2, (0, self.mainBG_Y_Speed - 900))

        # boss lives
        if len(self.bossSprites) != 0:
            pygame.draw.rect(screen, [255, 0, 0], pygame.Rect(225, 10, 725, 49))  # block
            pygame.draw.rect(screen, [0, 255, 0], pygame.Rect(225, 10, ((725 / self.bossOriginalLives) * self.bossLives), 49)) # block

        # Show waves
        self.wavesLbl = self.spaceFont.render("Wave: " + str(self.wave), True, [255, 255, 255])
        screen.blit(self.wavesLbl, (1300, 10))

        # Draw lives
        if self.lives > str(0):
            if self.lives >= str(1):
                screen.blit(self.livesImage1, (1000, 10))
            if self.lives >= str(2):
                screen.blit(self.livesImage2, (1050, 10))
            if self.lives >= str(3):
                screen.blit(self.livesImage3, (1100, 10))

        # Draw rest
        self.allSprites.draw(screen)

        # Countdown
        if self.showNextWave:
            self.timerLbl = self.spaceFont.render("New wave inbound", True, [255, 255, 255])
            screen.blit(self.timerLbl, (650, 350))
            self.timerLbl = self.spaceFont.render(str(math.floor(self.countDownTimer) + 1), True, [255, 255, 255])
            screen.blit(self.timerLbl, (800, 400))
