import pygame
from pygame import gfxdraw
from Scene import Scene as Scene
import SceneManager
from ButtonClass import Button
from Vector2D import Vector2D


class TowerDefenseScene(Scene):  # TowerDefenseScene inherits from the class Scene (wich is the base class of all scenes)

    def __init__(self):
        self.mainBG = pygame.image.load("MainMenu.png").convert()
        self.mainBG = pygame.transform.scale(self.mainBG, (1600, 900))

        super(TowerDefenseScene, self).__init__() # get the methods and variables from the base class wich is Scene
        self.boxPos = Vector2D(30, 30)
        self.backToMainMenuBtn = Button("Click to go back to the Main Menu", [220, 220, 220], [0, 0, 0], [120, 120, 120], 30, 100, None, 40)

        self.boxPosFont = pygame.font.SysFont("monospace", 12)
        self.boxPosFont.set_bold(True)

    # The function of this method is explained in the class Scene
    def render(self, screen):
        pygame.display.set_caption("Tower Defense (Press ESCAPE to close the game)")
        screen.blit(self.mainBG, (0, 0))
        self.backToMainMenuBtn.draw(screen)
        pygame.draw.rect(screen, [255, 0, 0], pygame.Rect(self.boxPos.x, self.boxPos.y, 20, 20))

        # self.renderTurretTest(screen)

        # render box text
        boxPosLbl = self.boxPosFont.render("X: " + str(self.boxPos.x) + "| Y: " + str(self.boxPos.y), 1, (255, 255, 0))
        screen.blit(boxPosLbl, (self.boxPos.x, self.boxPos.y))

    # The function of this method is explained in the class Scene
    def update(self, deltaTime):

        if self.backToMainMenuBtn.click():
            SceneManager.SceneMananger.goToScene("MainMenu")

        #  Move towards mouse pos and stop the cube when its at the mouse position
        mousePos = Vector2D(pygame.mouse.get_pos())
        moveToMousePosVector = mousePos - self.boxPos

        if self.boxPos.get_distance(mousePos) > 0:
            moveToMousePosVector.length = 1000 * deltaTime

        if moveToMousePosVector.length > mousePos.get_distance(self.boxPos):
            moveToMousePosVector.length = mousePos.get_distance(self.boxPos)

        self.boxPos += moveToMousePosVector


    # The function of this method is explained in the class Scene
    def handle_events(self, events):
        for event in events:
            pass