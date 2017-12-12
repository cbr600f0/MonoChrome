import pygame
import SceneManager
import pygame.gfxdraw
from DXBall.Ball import Ball
from DXBall.Paddle import Paddle
from ButtonClass import Button
from Vector2 import Vector2

class DXBallMainMenuScene (SceneManager.Scene):

    def __init__(self):
        super(DXBallMainMenuScene, self).__init__()

        #pygame.mixer.music.load('DXBall\Sounds\Lazerhawk-Overddrive.mp3')
        #pygame.mixer.music.play(loops=-1)

        # shows the mouse
        pygame.mouse.set_visible(False)
        # loads the background and changes it to fit the screen
        self.MainBG = pygame.image.load('DXBall\Images\Leveldesignv1.png').convert_alpha()
        self.MainBG = pygame.transform.scale(self.MainBG, (1600, 900))

        self.allSprites = pygame.sprite.Group()
        self.ballSprites = pygame.sprite.Group()
        self.ballcollideSprites = pygame.sprite.Group()

        Ball(Vector2(800, 450), self.allSprites, self.ballSprites)
        Paddle(self.allSprites, self.ballcollideSprites)

        self.isPaused = False
        self.pausedSurface = pygame.Surface((1600, 900))
        self.pausedSurface.set_alpha(90)
        self.pausedSurface.fill((150, 46, 91))



    def render(self, screen):
        screen.blit(self.MainBG, (0, 0))

        self.allSprites.draw(screen)
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(100, 200, 99, 49))  # block
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(200, 200, 99, 49))  # block
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(300, 200, 99, 49))  # block
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(400, 200, 99, 49))  # block
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(500, 200, 99, 49))  # block
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(600, 200, 99, 49))  # block
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(700, 200, 99, 49))  # block
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(800, 200, 99, 49))  # block
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(900, 200, 99, 49))  # block
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(1000, 200, 99, 49))  # block
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(1100, 200, 99, 49))  # block
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(1200, 200, 99, 49))  # block
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(1300, 200, 99, 49))  # block
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(1400, 200, 99, 49))  # block


        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(400, 300, 99, 49))  # block
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(500, 300, 99, 49))  # block
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(600, 300, 99, 49))  # block
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(700, 300, 99, 49))  # block
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(800, 300, 99, 49))  # block
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(900, 300, 99, 49))  # block
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(1000, 300, 99, 49))  # block
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(1100, 300, 99, 49))  # block


        if self.isPaused:
            screen.blit(self.pausedSurface, (0, 0))


    def paused(self):
        pass


    def update(self, deltaTime):
        self.allSprites.update(deltaTime, self.allSprites, self.ballSprites, self.ballcollideSprites)
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_p]:
            self.isPaused = True
        if pressed[pygame.K_o]:
            self.isPaused = False


    def handle_events(self, events):
        pass