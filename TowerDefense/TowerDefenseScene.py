import pygame
from Scene import Scene as Scene
import SceneManager
from ButtonClass import Button
from Vector2D import Vector2D

class TowerDefenseScene(Scene):  # TowerDefenseScene inherits from the class Scene (wich is the base class of all scenes)

    def __init__(self):
        super(TowerDefenseScene, self).__init__() # get the methods and variables from the base class wich is Scene
        self.boxPos = Vector2D(30, 30)
        self.backToMainMenuBtn = Button("Click to go back to the Main Menu", [220, 220, 220], [0, 0, 0], [120, 120, 120], 30, 100, None, 40)

    # The function of this method is explained in the class Scene
    def render(self, screen):
        pygame.display.set_caption("Tower Defense (Press ESCAPE to close the game)")
        screen.fill((0,0, 120))
        self.backToMainMenuBtn.draw(screen)
        pygame.draw.rect(screen, [255, 0, 0], pygame.Rect(self.boxPos.x, self.boxPos.y, 10, 10))

        myfont = pygame.font.SysFont("monospace", 12)
        myfont.set_bold(True)

        # render text
        label = myfont.render("Controls: W, A, S, D", 1, (255, 255, 0))
        # render box text
        label2 = myfont.render("X: " + str(self.boxPos.x) + "| Y: " + str(self.boxPos.y), 1, (255, 255, 0))
        screen.blit(label2, (self.boxPos.x, self.boxPos.y))
        screen.blit(label, (160, 20))

    # The function of this method is explained in the class Scene
    def update(self, deltaTime):
        if self.backToMainMenuBtn.click():
            SceneManager.SceneMananger.goToScene("MainMenu")

        #  Move towards mouse pos and stop the cube when its at the mouse position
        mousePos = Vector2D(pygame.mouse.get_pos())
        moveToMousePosVector = mousePos - self.boxPos

        if self.boxPos.get_distance(mousePos) > 0:
            moveToMousePosVector.length = 300 * deltaTime

        if moveToMousePosVector.length > mousePos.get_distance(self.boxPos):
            moveToMousePosVector.length = mousePos.get_distance(self.boxPos)

        self.boxPos += moveToMousePosVector


    # The function of this method is explained in the class Scene
    def handle_events(self, events):
        for event in events:
            pass