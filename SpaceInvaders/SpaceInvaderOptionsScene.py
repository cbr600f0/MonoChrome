import pygame
import SceneManager
from ButtonClass import Button

class SpaceInvaderOptionsScene (SceneManager.Scene):

    def __init__(self, *optionalSceneParam):
        super(SpaceInvaderOptionsScene, self).__init__()

        self.mainBG = pygame.image.load("SpaceInvaders/images/Start menu.png").convert()
        self.mainBG = pygame.transform.scale(self.mainBG, (1600, 900))

        # Font
        self.spaceFont = pygame.font.Font("SpaceInvaders/font/OCRAEXT.TTF", 32)
        self.spaceFontMed = pygame.font.Font("SpaceInvaders/font/OCRAEXT.TTF", 60)
        self.spaceFontBig = pygame.font.Font("SpaceInvaders/font/OCRAEXT.TTF", 100)

        # Get audio settings
        if optionalSceneParam[0][0] != None:
            self.audio = optionalSceneParam[0][0]
        else:
            self.audio = True

        if self.audio == True:
            self.onBtn = Button(False, self.spaceFontBig, "On", None, None, [47, 253, 39], [42, 178, 35], 1000, 250, None, 120)
            self.offBtn = Button(False, self.spaceFontBig, "Off", None, None, [47, 253, 39], [255, 255, 255], 1150, 250, None, 120)
        else:
            self.onBtn = Button(False, self.spaceFontBig, "On", None, None, [47, 253, 39], [255, 255, 255], 1000, 250, None, 120)
            self.offBtn = Button(False, self.spaceFontBig, "Off", None, None, [47, 253, 39], [42, 178, 35], 1150, 250, None, 120)

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

        if self.onBtn.click():
            self.audio = True
            self.onBtn = Button(False, self.spaceFontBig, "On", None, None, [47, 253, 39], [42, 178, 35], 1000, 250, None, 120)
            self.offBtn = Button(False, self.spaceFontBig, "Off", None, None, [47, 253, 39], [255, 255, 255], 1150, 250, None, 120)

        if self.offBtn.click():
            self.audio = False
            self.onBtn = Button(False, self.spaceFontBig, "On", None, None, [47, 253, 39], [255, 255, 255], 1000, 250, None, 120)
            self.offBtn = Button(False, self.spaceFontBig, "Off", None, None, [47, 253, 39], [42, 178, 35], 1150, 250, None, 120)

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            SceneManager.SceneManager.goToScene("SpaceInvaders.SpaceInvaderMainMenuScene.SpaceInvaderMainMenuScene", self.audio, self.highestWave)

    def render(self, screen):
        screen.blit(self.mainBG, (0, 0))

        self.messageLbl = self.spaceFontBig.render("Audio is: ", True, [255, 255, 255])
        screen.blit(self.messageLbl, (250, 250))

        self.messageLbl = self.spaceFontMed.render("Controls: Up         = Shoot", True, [255, 255, 255])
        screen.blit(self.messageLbl, (250, 400))
        self.messageLbl = self.spaceFontMed.render("          Left/Right = Move", True, [255, 255, 255])
        screen.blit(self.messageLbl, (250, 450))
        self.messageLbl = self.spaceFontMed.render("          Backspace  = Quit game", True, [255, 255, 255])
        screen.blit(self.messageLbl, (250, 500))

        self.messageLbl = self.spaceFont.render("Press [space] to return to menu", True, [255, 255, 255])
        screen.blit(self.messageLbl, (850, 750))

        self.onBtn.draw(screen)
        self.offBtn.draw(screen)
