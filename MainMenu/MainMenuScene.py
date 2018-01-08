import pygame
import SceneManager
from ButtonClass import Button


class MainMenuScene(SceneManager.Scene): # MainMenuScene inherits from the class Scene (wich is the base class of all scenes)

    def __init__(self):
        super(MainMenuScene, self).__init__()  # get the methods and variables from the base class wich is Scene

        #Fonts
        self.pongFont = pygame.font.SysFont("monospace", 40)
        self.spaceInvadersFont = pygame.font.Font("SpaceInvaders/font/OCRAEXT.TTF", 30)
        self.towerDefenseFont = pygame.font.Font("TowerDefense/WesternFont.otf", 40)
        self.DXBallFont = pygame.font.Font("DXBall/SFAlienEncounters-Italic.ttf", 52)

        self.backgroundImage = pygame.image.load("MainMenu/Images/MainMenuBackgroundPlusMachine.png").convert()
        self.headerSurfaceSize = (638, 134)
        self.bodySurfaceSize = (560, 460)

        #Header Images
        self.pongHeaderImage = pygame.image.load("MainMenu/Images/Minigames/PongHeader.png").convert()
        self.pongHeaderImage = pygame.transform.scale(self.pongHeaderImage, self.headerSurfaceSize)

        self.towerDefenseHeaderImage = pygame.image.load("MainMenu/Images/Minigames/TowerDefenseHeader.png").convert()
        self.towerDefenseHeaderImage = pygame.transform.scale(self.towerDefenseHeaderImage, self.headerSurfaceSize)

        self.dxBallHeaderImage = pygame.image.load("MainMenu/Images/Minigames/DXBallHeader.png").convert()
        self.dxBallHeaderImage = pygame.transform.scale(self.dxBallHeaderImage, self.headerSurfaceSize)

        #self.spaceInvadersHeaderImage = pygame.image.load("MainMenu/Images/Minigames/PongHeader.png").convert() # i wont use this title its title quality is too bad

        self.bubbleShooterHeaderImage = pygame.image.load("MainMenu/Images/Minigames/LightballShooterHeader.png").convert()
        self.bubbleShooterHeaderImage = pygame.transform.scale(self.bubbleShooterHeaderImage, self.headerSurfaceSize)

        #Body Images
        self.pongBodyImage = pygame.image.load("MainMenu/Images/Minigames/PongArcadeBodyImage.png").convert()
        self.pongBodyImage = pygame.transform.scale(self.pongBodyImage, self.bodySurfaceSize)

        self.towerDefenseBodyImage = pygame.image.load("MainMenu/Images/Minigames/TowerDefenseArcadeBodyImage.png").convert()
        self.towerDefenseBodyImage = pygame.transform.scale(self.towerDefenseBodyImage, self.bodySurfaceSize)

        self.dxBallBodyImage = pygame.image.load("MainMenu/Images/Minigames/DXBallHeader.png").convert()
        self.dxBallBodyImage = pygame.transform.scale(self.dxBallBodyImage, self.bodySurfaceSize)

        #self.spaceInvadersBodyImage = pygame.image.load("MainMenu/Images/Minigames/PongHeader.png").convert() # i wont use this title its title quality is too bad

        self.bubbleShooterBodyImage = pygame.image.load("MainMenu/Images/Minigames/LightballShooterHeader.png").convert()
        self.bubbleShooterBodyImage = pygame.transform.scale(self.bubbleShooterBodyImage, self.bodySurfaceSize)

        #Surfaces
        self.headerSurface = pygame.Surface(self.headerSurfaceSize)
        self.bodySurface = pygame.Surface(self.bodySurfaceSize)
        self.backgroundBodySurface = pygame.Surface((570, 470))
        self.backgroundBodySurface.fill((40, 40, 40))

         #Buttons
        self.towerDefenseBtn = Button(False, self.towerDefenseFont, "Tower Defense", [220, 220, 220], [0, 0, 0], [120, 120, 120], [0, 0, 0], 900, 160, 600, 60)
        self.pongBtn = Button(False, self.pongFont, "Pong", [220, 220, 220], [0, 0, 0], [120, 120, 120], [0, 0, 0], 900, 100, 600, 60)
        self.DXBallBtn = Button(False, self.DXBallFont, "Retroball", [220, 220, 220], [0, 0, 0], [120, 120, 120], [0, 0, 0], 900, 340, 600, 60)
        self.spaceInvadersBtn = Button(False, self.spaceInvadersFont, "Space Invaders", [220, 220, 220], [0, 0, 0], [120, 120, 120], [0, 0, 0], 900, 220, 600, 60)
        self.bubbleShooterBtn = Button(True, None, "Bubble Shooter", [220, 220, 220], [0, 0, 0], [120, 120, 120], [0, 0, 0], 900, 280, 600, 60)

        self.currentHeaderImage = self.pongHeaderImage
        self.currentBodyImage = self.pongBodyImage

        self.currentMinigameBtn = self.pongBtn

        self.minigameBtnList = []
        self.minigameBtnList.append(self.pongBtn)
        self.minigameBtnList.append(self.towerDefenseBtn)
        self.minigameBtnList.append(self.DXBallBtn)
        self.minigameBtnList.append(self.spaceInvadersBtn)
        self.minigameBtnList.append(self.bubbleShooterBtn)

        self.headerImageList = []
        self.headerImageList.append(self.pongHeaderImage)
        self.headerImageList.append(self.towerDefenseHeaderImage)
        self.headerImageList.append(self.dxBallHeaderImage)
        self.headerImageList.append(self.dxBallHeaderImage) # this should be space invaders but i dont have an image for that yet
        self.headerImageList.append(self.bubbleShooterHeaderImage)

        self.bodyImageList = []
        self.bodyImageList.append(self.pongBodyImage)
        self.bodyImageList.append(self.towerDefenseBodyImage)
        self.bodyImageList.append(self.dxBallBodyImage)
        self.bodyImageList.append(self.dxBallBodyImage) # this should be space invaders but i dont have an image for that yet
        self.bodyImageList.append(self.bubbleShooterBodyImage)

    # The function of this method is explained in the class Scene
    def render(self, screen):

        screen.blit(self.backgroundImage, (0, 0))

        self.headerSurface.blit(self.currentHeaderImage, (0, 0))
        self.bodySurface.blit(self.currentBodyImage, (0, 0))

        screen.blit(self.headerSurface, (84, 40))
        screen.blit(self.backgroundBodySurface, (117, 238))
        screen.blit(self.bodySurface, (122, 243))

        self.drawButtons(screen)

    def update(self, deltaTime):

        for index in range(len(self.minigameBtnList)):
            minigameBtn = self.minigameBtnList[index]

            if minigameBtn.mouseState == "hover":
                self.currentHeaderImage = self.headerImageList[index]
                self.currentBodyImage = self.bodyImageList[index]
                self.currentMinigameBtn = minigameBtn

            if minigameBtn is not self.currentMinigameBtn:
                minigameBtn.lockHoverState = False

        self.currentMinigameBtn.lockHoverState = True

        if self.towerDefenseBtn.click():
            SceneManager.SceneManager.goToScene("TowerDefense.TowerDefenseMainMenuScene.TowerDefenseMainMenuScene") # Changes the scene to TowerDefense

        if self.pongBtn.click():
            SceneManager.SceneManager.goToScene("Pong.PongMainMenuScene.PongMainMenuScene") # Changes the scene to Pong

        if self.spaceInvadersBtn.click():
            SceneManager.SceneManager.goToScene("SpaceInvaders.SpaceInvaderMainMenuScene.SpaceInvaderMainMenuScene", None) # Changes the scene to SpaceInvaders

        if self.bubbleShooterBtn.click():
            SceneManager.SceneManager.goToScene("BubbleShooter2.BubbleShooterMainMenuScene.BubbleShooterMainMenuScene") # Changes the scene to BubbleShooter

        if self.DXBallBtn.click():
            SceneManager.SceneManager.goToScene("DXBall.DXBallMainMenuScene.DXBallMainMenuScene") # Changes the scene to DX-ball

    def drawButtons(self, screen):
        self.pongBtn.draw(screen)
        self.towerDefenseBtn.draw(screen)
        self.spaceInvadersBtn.draw(screen)
        self.bubbleShooterBtn.draw(screen)
        self.DXBallBtn.draw(screen)

    def handle_events(self, events):
        pass

    def getOutline(self, image, color=(0, 0, 0), threshold=127):
        mask = pygame.mask.from_surface(image, threshold)
        outline_image = pygame.Surface(image.get_size()).convert_alpha()
        outline_image.fill((0, 0, 0, 0))

        #outline_image = pygame.transform.rotozoom(outline_image, 0, 1)

        for point in mask.outline():
            outline_image.set_at(point, color)
        return outline_image