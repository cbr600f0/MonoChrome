import pygame
from Scene import Scene as Scene
import SceneManager
from ButtonClass import Button


class MainMenuScene(Scene): # MainMenuScene inherits from the class Scene (wich is the base class of all scenes)

    def __init__(self):
        super(MainMenuScene, self).__init__()  # get the methods and variables from the base class wich is Scene

        self.towerDefenseBtn = Button("Click to go to Tower Defense", [220, 220, 220], [0, 0, 0], [120, 120, 120], 30, 100, None, 40)

    # The function of this method is explained in the class Scene
    def render(self, screen):
        pygame.display.set_caption("Main Menu")  # Changes the text of the window
        screen.fill((0, 200, 0))
        self.towerDefenseBtn.draw(screen)
        pass

    # The function of this method is explained in the class Scene
    def update(self):
        if self.towerDefenseBtn.click():
            SceneManager.SceneMananger.goToScene("TowerDefense") # Changes the scene to TowerDefense

    # The function of this method is explained in the class Scene
    def handle_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                pass  # In python you must implement stuff like this if statement, i dont want to implement it yet so i simple write pass wich does nothing you could say that this if statements implementation is empty