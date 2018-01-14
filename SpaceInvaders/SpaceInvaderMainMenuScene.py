import pygame
import SceneManager
from ButtonClass import Button

class SpaceInvaderMainMenuScene (SceneManager.Scene):

    def __init__(self, *optionalSceneParam):
        super(SpaceInvaderMainMenuScene, self).__init__()

        self.mainBG = pygame.image.load("SpaceInvaders/images/Start menu.png").convert()
        self.mainBG = pygame.transform.scale(self.mainBG, (1600, 900))

        # Font
        self.spaceFontSmall = pygame.font.Font("SpaceInvaders/font/OCRAEXT.TTF", 32)
        self.spaceFont = pygame.font.Font("SpaceInvaders/font/OCRAEXT.TTF", 80)

        self.startBtn   = Button(False, self.spaceFont, "Start",                    None, None, [47, 253, 39], [255, 255, 255], 125, 300, None, 120)
        self.optionsBtn = Button(False, self.spaceFont, "Options / instructions",   None, None, [47, 253, 39], [255, 255, 255], 125, 450, None, 120)
        self.quitBtn    = Button(False, self.spaceFont, "Quit to main menu",        None, None, [47, 253, 39], [255, 255, 255], 125, 600, None, 120)

        if optionalSceneParam[0][0] != None:
            self.audio = optionalSceneParam[0][0]
        else:
            self.audio = True

        if optionalSceneParam[0][1] != None:
            self.highestWave = optionalSceneParam[0][1]
        else:
            self.highestWave = 0

        # Extra
        self.messageLbl = ""

    def handle_events(self, events):
        for event in events:
            pass

    def update(self, deltaTime):
        if self.startBtn.click():
            SceneManager.SceneManager.goToScene("SpaceInvaders.SpaceInvaderLevelScene.SpaceInvaderLevelScene", self.audio, self.highestWave)

        if self.optionsBtn.click():
            SceneManager.SceneManager.goToScene("SpaceInvaders.SpaceInvaderOptionsScene.SpaceInvaderOptionsScene", self.audio, self.highestWave)

        if self.quitBtn.click():
            SceneManager.SceneManager.goToScene("MainMenu.MainMenuScene.MainMenuScene") # , self.audio, self.highestWave

    def render(self, screen):
        screen.blit(self.mainBG, (0, 0))

        self.messageLbl = self.spaceFontSmall.render("Your current highscore is: " + str(self.highestWave), True, [255, 255, 255])
        screen.blit(self.messageLbl, (140, 200))

        self.startBtn.draw(screen)
        self.optionsBtn.draw(screen)
        self.quitBtn.draw(screen)
