import pygame
import SceneManager
from ButtonClass import Button


class MainMenuScene(SceneManager.Scene): # MainMenuScene inherits from the class Scene (wich is the base class of all scenes)

    def __init__(self):
        super(MainMenuScene, self).__init__()  # get the methods and variables from the base class wich is Scene
        self.pongFont = pygame.font.SysFont("monospace", 40)
        self.spaceInvadersFont = pygame.font.Font("SpaceInvaders/font/OCRAEXT.TTF", 30)
        self.towerDefenseFont = pygame.font.Font("TowerDefense/WesternFont.otf", 40)

        self.backgroundImage = pygame.image.load("MainMenu/Images/MainMenuBackgroundPlusMachine.png").convert()

        self.towerDefenseBtn = Button(False, self.towerDefenseFont, "Tower Defense", [220, 220, 220], [0, 0, 0], [120, 120, 120], [0, 0, 0], 900, 100, 600, 60)
        self.pongBtn = Button(False, self.pongFont, "Pong", [220, 220, 220], [0, 0, 0], [120, 120, 120], [0, 0, 0], 900, 160, 600, 60)
        self.DXBallBtn = Button(True, None, "DX-ball", [220, 220, 220], [0, 0, 0], [120, 120, 120], [0, 0, 0], 900, 220, 600, 60)
        self.spaceInvadersBtn = Button(False, self.spaceInvadersFont, "Space Invaders", [220, 220, 220], [0, 0, 0], [120, 120, 120], [0, 0, 0], 900, 280, 600, 60)
        self.BubbleShooterBtn = Button(True, None, "Bubble Shooter", [220, 220, 220], [0, 0, 0], [120, 120, 120], [0, 0, 0], 900, 340, 600, 60)

    # The function of this method is explained in the class Scene
    def render(self, screen):

        screen.blit(self.backgroundImage, (0, 0))

        self.pongBtn.draw(screen)
        self.towerDefenseBtn.draw(screen)
        self.spaceInvadersBtn.draw(screen)
        self.BubbleShooterBtn.draw(screen)
        self.DXBallBtn.draw(screen)

    # The function of this method is explained in the class Scene
    def update(self, deltaTime):

        if self.towerDefenseBtn.click():
            SceneManager.SceneManager.goToScene("TowerDefense.TowerDefenseMainMenuScene.TowerDefenseMainMenuScene") # Changes the scene to TowerDefense

        if self.pongBtn.click():
            SceneManager.SceneManager.goToScene("Pong.PongMainMenuScene.PongMainMenuScene") # Changes the scene to Pong

        if self.spaceInvadersBtn.click():
            SceneManager.SceneManager.goToScene("SpaceInvaders.SpaceInvaderMainMenuScene.SpaceInvaderMainMenuScene", None) # Changes the scene to SpaceInvaders

        if self.BubbleShooterBtn.click():
            SceneManager.SceneManager.goToScene("BubbleShooter2.BubbleShooterMainMenuScene.BubbleShooterMainMenuScene") # Changes the scene to BubbleShooter

        if self.DXBallBtn.click():
            SceneManager.SceneManager.goToScene("DXBall.DXBallMainMenuScene.DXBallMainMenuScene") # Changes the scene to DX-ball

    # The function of this method is explained in the class Scene
    def handle_events(self, events):
        pass