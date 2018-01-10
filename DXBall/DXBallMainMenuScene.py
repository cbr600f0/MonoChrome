import pygame
import SceneManager

from ButtonClass import Button


class DXBallMainMenuScene(SceneManager.Scene):

    def __init__(self):
        super(DXBallMainMenuScene, self).__init__()

        pygame.mixer.music.load('DXBall\Sounds\MiamiNights1984-Accelerated.ogg')
        pygame.mixer.music.play(loops=-1)

        self.DXBallFont = pygame.font.Font("DXBall/SFAlienEncounters-Italic.ttf", 52)
        self.DXBallFont2 = pygame.font.Font("DXBall/Fonts/Megatron Condensed.otf", 52)

        self.mainBG = pygame.image.load("DXBall\Images\BckGrnd.png").convert()
        self.mainBG = pygame.transform.scale(self.mainBG, (1600, 900))

        self.arrowFont = pygame.font.SysFont("monospace", 50)
        self.arrowLbl = self.arrowFont.render(">", True, [2, 255, 149])

        self.buttonList = []

        self.startBtn = Button(False, self.DXBallFont, "[Start]", None, None, [2, 255, 149], [2, 255, 149], 44, 540, None, 60)
        self.optionsBtn = Button(False, self.DXBallFont, "[Options]", None, None, [2, 255, 149], [2, 255, 149], 44, 590, None, 60)
        self.quitBtn = Button(False, self.DXBallFont, "[Quit]", None, None, [2, 255, 149], [2, 255, 149], 44, 640, None, 60)

        self.buttonList.append(self.startBtn)
        self.buttonList.append(self.optionsBtn)
        self.buttonList.append(self.quitBtn)

        self.currentArrowPos = (0, 0)

    def render(self, screen):
        screen.blit(self.mainBG, (0, 0))
        screen.blit(self.arrowLbl, self.currentArrowPos)

        self.startBtn.draw(screen)
        self.optionsBtn.draw(screen)
        self.quitBtn.draw(screen)

    def update(self, deltaTime):

        self.currentArrowPos = (-1600, -900)
        for index in range(len(self.buttonList)):
            button = self.buttonList[index]

            if button.mouseState == "hover":
                self.currentArrowPos = (button.xPos - 15, button.yPos)

        if self.startBtn.click():
            SceneManager.SceneManager.goToScene("DXBall.DXBallLevel1.DXBallLevel1")

        if self.optionsBtn.click():
            pass

        if self.quitBtn.click():
            SceneManager.SceneManager.goToScene("MainMenu.MainMenuScene.MainMenuScene")

    def handle_events(self, events):
        for event in events:
            pass