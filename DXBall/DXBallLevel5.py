import pygame
import SceneManager
import pygame.gfxdraw
from DXBall.Ball import Ball
from DXBall.Paddle import Paddle
from DXBall.Block import Block
from ButtonClass import Button
from pygame.math import Vector2

class DXBallLevel5 (SceneManager.Scene):

    def __init__(self):
        super(DXBallLevel5, self).__init__()

        pygame.mixer.music.load('DXBall\Sounds\Lazerhawk-Overdrive.ogg')
        #pygame.mixer.music.play(loops=-1)

        # shows the mouse
        #pygame.mouse.set_visible(False)
        # loads the background and changes it to fit the screen
        self.MainBG = pygame.image.load('DXBall\Images\Level5.png').convert_alpha()
        self.MainBG = pygame.transform.scale(self.MainBG, (1600, 900))

        self.DXBallFont = pygame.font.Font("DXBall/SFAlienEncounters-Italic.ttf", 45)
        self.DXBallFont2 = pygame.font.Font("DXBall/Fonts/Megatron Condensed.otf", 52)
        self.DXBallFont3 = pygame.font.Font("DXBall/Fonts/SFAlienEncounters.ttf", 100)
        self.DXBallFont4 = pygame.font.Font("DXBall/Fonts/Megatron Condensed.otf", 80)

        self.health = 3

        self.buttonList = []

        self.nextBtn = Button(False, self.DXBallFont2, "[>]", None, None, [2, 255, 149], [2, 200, 149], 1520, 5, None,60)

        self.buttonList.append(self.nextBtn)

        self.allSprites = pygame.sprite.Group()
        self.ballSprites = pygame.sprite.Group()
        self.blockSprites = pygame.sprite.Group()
        self.ballcollideSprites = pygame.sprite.Group()

        self.ball = Ball(Vector2(800, 450), self.allSprites, self.ballSprites)
        Paddle(self.allSprites, self.ballcollideSprites)

        self.gameOver = False
        self.gameOverSurface = pygame.Surface((1600, 900))
        #self.gameOverSurface.set_alpha(90)
        self.gameOverSurface.fill((150, 46, 91))

        self.gameOverLbl = self.DXBallFont3.render("Game Over", True, [0, 0, 0])

        self.retryBtn = Button(False, self.DXBallFont4, "[Retry]", None, None, [255, 255, 255], [0, 0, 0], 620, 380,None, 60)
        self.exitBtn = Button(False, self.DXBallFont4, "[Exit]", None, None, [255, 255, 255], [0, 0, 0], 650, 470, None,60)

        self.gameOverSurface.blit(self.gameOverLbl, (480, 200))

        blockStartX = 100
        for i in range (12):
            spawnPos = Vector2(blockStartX + 100 * (i + 1) + (10 * i), 400)

            Block(spawnPos, self.blockSprites, self.ballcollideSprites, self.allSprites)

    def render(self, screen):
        screen.blit(self.MainBG, (0, 0))

        CurrentLives = self.DXBallFont.render("Lives: " + str(self.health), False, (2, 255, 149))
        screen.blit(CurrentLives, (100, 20))

        PowerUps = self.DXBallFont.render("Power Ups: Big upgrade", False, (2, 255, 149))
        screen.blit(PowerUps, (550, 20))

        CurrentLevel = self.DXBallFont.render("Level: 5", False, (2, 255, 149))
        screen.blit(CurrentLevel, (1300, 20))

        self.nextBtn.draw(screen)

        pygame.draw.rect(screen, [2, 255, 149], pygame.Rect(0, 65, 1600, 5))  # scoreboard border

        for spriteToDraw in self.allSprites:  #Make a forloop wich calls a draw method from each sprite instead of using draw on a sprite group
            spriteToDraw.draw(screen)

        if self.gameOver:
            self.renderGameOverScreen(screen)

    def renderGameOverScreen(self, screen):

        screen.blit(self.gameOverSurface, (0, 0))

        self.retryBtn.draw(screen)
        self.exitBtn.draw(screen)

        if self.retryBtn.click():
            SceneManager.SceneManager.goToScene("DXBall.DXBallLevel5.DXBallLevel5")

        if self.exitBtn.click():
            SceneManager.SceneManager.goToScene("DXBall.DXBallMainMenuScene.DXBallMainMenuScene")



    def update(self, deltaTime):
        self.allSprites.update(deltaTime, self.allSprites, self.ballSprites, self.ballcollideSprites)
        pressed = pygame.key.get_pressed()

        if self.health == 0:
            self.gameOver = True

        if self.nextBtn.click():
            pass #SceneManager.SceneManager.goToScene("DXBall.DXBallLevel5.DXBallLevel5")

        if self.ball.position.y > 900:
            self.health = self.health - 1

    def handle_events(self, events):
        pass