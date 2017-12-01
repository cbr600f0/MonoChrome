import pygame
from pygame import gfxdraw
from Scene import Scene as Scene
import SceneManager
from ButtonClass import Button
from Vector2D import Vector2D
from TowerDefense.Towers.AkimboRevolverTurret import AkimboRevolverTurret

class TowerDefenseScene(Scene):

    def __init__(self):
        super(TowerDefenseScene, self).__init__()
        self.testTurret = AkimboRevolverTurret()
        self.allSprites = pygame.sprite.Group(self.testTurret)

        self.mainBG = pygame.image.load("MainMenu.png").convert()
        self.mainBG = pygame.transform.scale(self.mainBG, (1600, 900))
        self.boxPos = Vector2D(30, 30)
        self.backToMainMenuBtn = Button("Click to go back to the Main Menu", [220, 220, 220], [0, 0, 0], [120, 120, 120], 30, 100, None, 40)

        self.boxPosFont = pygame.font.SysFont("monospace", 12)
        self.boxPosFont.set_bold(True)

    def render(self, screen):
        self.allSprites.clear(screen, self.mainBG)
        screen.blit(self.mainBG, (0, 0))
        pygame.display.set_caption("Tower Defense (Press ESCAPE to close the game)")

        self.backToMainMenuBtn.draw(screen)

        #Render Box
        pygame.draw.rect(screen, [255, 0, 0], pygame.Rect(self.boxPos.x, self.boxPos.y, 20, 20))

        # render box text
        boxPosLbl = self.boxPosFont.render("X: " + str(self.boxPos.x) + "| Y: " + str(self.boxPos.y), 1, (255, 255, 0))
        screen.blit(boxPosLbl, (self.boxPos.x, self.boxPos.y))
        self.allSprites.draw(screen)

    def update(self, deltaTime):
        self.allSprites.update()
        self.testTurret.PosToFollow = self.boxPos
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

    def handle_events(self, events):
        for event in events:
            pass