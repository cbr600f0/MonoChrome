import pygame
import SceneManager
import pygame.gfxdraw
from DXBall.Ball import Ball
from DXBall.Paddle import Paddle
from DXBall.Block import Block
from ButtonClass import Button
from pygame.math import Vector2

class DXBallLevel1 (SceneManager.Scene):

    def __init__(self):
        super(DXBallLevel1, self).__init__()

        pygame.mixer.music.load('DXBall\Sounds\Lazerhawk-Overdrive.ogg')
        #pygame.mixer.music.play(loops=-1)

        # shows the mouse
        #pygame.mouse.set_visible(False)
        # loads the background and changes it to fit the screen
        self.MainBG = pygame.image.load('DXBall\Images\Leveldesignv1.png').convert_alpha()
        self.MainBG = pygame.transform.scale(self.MainBG, (1600, 900))

        self.allSprites = pygame.sprite.Group()
        self.ballSprites = pygame.sprite.Group()
        self.blockSprites = pygame.sprite.Group()
        self.ballcollideSprites = pygame.sprite.Group()

        Ball(Vector2(800, 450), self.allSprites, self.ballSprites)
        Paddle(self.allSprites, self.ballcollideSprites)

        self.isPaused = False
        self.pausedSurface = pygame.Surface((1600, 900))
        self.pausedSurface.set_alpha(90)
        self.pausedSurface.fill((150, 46, 91))

        blockStartX = 100
        for i in range (12):
            spawnPos = Vector2(blockStartX + 100 * (i + 1) + (10 * i), 400)

            Block(spawnPos, self.blockSprites, self.ballcollideSprites, self.allSprites)

    def render(self, screen):
        screen.blit(self.MainBG, (0, 0))

        for spriteToDraw in self.allSprites:  #Make a forloop wich calls a draw method from each sprite instead of using draw on a sprite group
            spriteToDraw.draw(screen)

        if self.isPaused:
            screen.blit(self.pausedSurface, (0, 0))


    def update(self, deltaTime):
        self.allSprites.update(deltaTime, self.allSprites, self.ballSprites, self.ballcollideSprites)
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_p]:
            self.isPaused = True
        if pressed[pygame.K_o]:
            self.isPaused = False


    def handle_events(self, events):
        pass