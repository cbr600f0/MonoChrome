import pygame
import SceneManager

from ButtonClass import Button


class DXBallMainMenuScene(SceneManager.Scene):

    def __init__(self):
        super(DXBallMainMenuScene, self).__init__()

        pygame.mixer.music.load('DXBall\Sounds\MiamiNights1984-Accelerated.ogg')
        #pygame.mixer.music.play(loops=-1)

        self.mainBG = pygame.image.load("DXBall\Images\menuschermv3.titel.png").convert()
        self.mainBG = pygame.transform.scale(self.mainBG, (1600, 900))

        self.startBtn = Button(True, None, ">", None, None, [2, 255, 149], [110, 90, 73], 70, 480, None, 70)
        self.optionsBtn = Button(True, None, ">", None, None, [2, 255, 149], [110, 90, 73], 70, 530, None, 70)
        self.quitBtn = Button(True, None, ">", None, None, [2, 255, 149], [110, 90, 73], 70, 580, None, 70)

    def render(self, screen):
        screen.blit(self.mainBG, (0, 0))

        self.startBtn.draw(screen)
        self.optionsBtn.draw(screen)
        self.quitBtn.draw(screen)

    def update(self, deltaTime):

        if self.startBtn.click():
            SceneManager.SceneManager.goToScene("DXBall.DXBallLevel1.DXBallLevel1")

        if self.optionsBtn.click():
            pass

        if self.quitBtn.click():
            SceneManager.SceneManager.goToScene("MainMenu.MainMenuScene.MainMenuScene")

    def handle_events(self, events):
        for event in events:
            pass