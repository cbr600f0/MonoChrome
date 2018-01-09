import pygame
import SceneManager
from ButtonClass import Button

class SpaceInvaderGameOverScene (SceneManager.Scene):

    def __init__(self, *optionalSceneParam):
        super(SpaceInvaderGameOverScene, self).__init__()

        # Background
        self.mainBG = pygame.image.load("SpaceInvaders/images/Background.png").convert()
        self.mainBG = pygame.transform.scale(self.mainBG, (1600, 900))

        # Font
        self.spaceFont = pygame.font.Font("SpaceInvaders/font/OCRAEXT.TTF", 32)

        if optionalSceneParam[0][0] != None:
            self.audio = optionalSceneParam[0][0]
        else:
            self.audio = True

        # Receive last score
        self.lastWave = str(optionalSceneParam[0][1])

        # Receive previous high score
        if optionalSceneParam[0][1] != None:
            self.highScoreWave = optionalSceneParam[0][2]
        else:
            self.highScoreWave = 0

        # Check highest score
        if self.lastWave > self.highScoreWave:
            self.newHighScoreWave = self.lastWave
        else:
            self.newHighScoreWave = self.highScoreWave

        # Extra
        self.messageLbl = ""

    def update(self, deltaTime):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            SceneManager.SceneManager.goToScene("SpaceInvaders.SpaceInvaderMainMenuScene.SpaceInvaderMainMenuScene", self.audio, self.newHighScoreWave)

    def handle_events(self, events):
        pass

    def render(self, screen):
        screen.blit(self.mainBG, (0, 0))

        self.messageLbl = self.spaceFont.render("Your last wave was: " + str(self.lastWave), True, [255, 255, 255])
        screen.blit(self.messageLbl, (650, 350))

        self.messageLbl = self.spaceFont.render("Your highest wave was: " + str(self.highScoreWave), True, [255, 255, 255])
        screen.blit(self.messageLbl, (650, 450))

        self.messageLbl = self.spaceFont.render("Press [space] to return to main menu", True, [255, 255, 255])
        screen.blit(self.messageLbl, (850, 750))
