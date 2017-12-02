import pygame
import SceneManager
from ButtonClass import Button


class MainMenuScene(SceneManager.Scene): # MainMenuScene inherits from the class Scene (wich is the base class of all scenes)

    def __init__(self):
        super(MainMenuScene, self).__init__()  # get the methods and variables from the base class wich is Scene

        self.towerDefenseBtn = Button("Click to go to Tower Defense", [220, 220, 220], [0, 0, 0], [120, 120, 120], [0, 0, 0], 30, 100, None, 40)
        self.pongBtn = Button("Click to go to Pong", [220, 220, 220], [0, 0, 0], [120, 120, 120], [0, 0, 0], 30, 140, None, 40)
        self.spaceInvadersBtn = Button("Click to go to Space Invaders", [220, 220, 220], [0, 0, 0], [120, 120, 120], [0, 0, 0], 30, 180, None, 40)
        self.BubbleShooterBtn = Button("Click to go to Bubble Shooter", [220, 220, 220], [0, 0, 0], [120, 120, 120], [0, 0, 0], 30, 220, None, 40)

    # The function of this method is explained in the class Scene
    def render(self, screen):
        pygame.display.set_caption("Main Menu (Press ESCAPE to close the game)")  # Changes the text of the window
        screen.fill((90, 90, 90))
        self.towerDefenseBtn.draw(screen)
        self.pongBtn.draw(screen)
        self.spaceInvadersBtn.draw(screen)
        self.BubbleShooterBtn.draw(screen)

    # The function of this method is explained in the class Scene
    def update(self, deltaTime):
        if self.towerDefenseBtn.click():
            SceneManager.SceneMananger.goToScene("TowerDefense.TowerDefenseMainMenuScene.TowerDefenseMainMenuScene") # Changes the scene to TowerDefense

        if self.pongBtn.click():
            SceneManager.SceneMananger.goToScene("Pong.PongScene") # Changes the scene to Pong

        if self.spaceInvadersBtn.click():
            SceneManager.SceneMananger.goToScene("SpaceInvaders.SpaceInvaderScene") # Changes the scene to SpaceInvaders

        if self.BubbleShooterBtn.click():
            SceneManager.SceneMananger.goToScene("BubbleShooter.BubbleShooterScene") # Changes the scene to BubbleShooter

    # The function of this method is explained in the class Scene
    def handle_events(self, events):
        pass  # In python you must implement stuff like this if statement, i dont want to implement it yet so i simple write pass wich does nothing you could say that this if statements implementation is empty