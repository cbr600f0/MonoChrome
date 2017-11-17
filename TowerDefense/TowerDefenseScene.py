import pygame
from Scene import Scene as Scene
import SceneManager
from ButtonClass import Button


class TowerDefenseScene(Scene):  # TowerDefenseScene inherits from the class Scene (wich is the base class of all scenes)

    def __init__(self):
        super(TowerDefenseScene, self).__init__() # get the methods and variables from the base class wich is Scene

        self.boxX = 30
        self.boxY = 30

        self.bg = pygame.Surface((32,32))
        self.bg.convert()
        self.bg.fill(pygame.Color(0, 0, 120))
        self.backToMainMenuBtn = Button("Click to go back to the Main Menu", [220, 220, 220], [0, 0, 0], [120, 120, 120], 30, 100, None, 40)
        pygame.display.set_caption("Tower Defense")

    # The function of this method is explained in the class Scene
    def render(self, screen):
        pygame.display.set_caption("Tower Defense")
        screen.fill((0,0, 120))
        self.backToMainMenuBtn.draw(screen)
        pygame.draw.rect(screen, [255, 0, 0], pygame.Rect(self.boxX, self.boxY, 60, 60))

        myfont = pygame.font.SysFont("monospace", 28)

        # render text
        label = myfont.render("Controls: W, A, S, D", 1, (255, 255, 0))
        screen.blit(label, (160, 20))

    # The function of this method is explained in the class Scene
    def update(self):
        if self.backToMainMenuBtn.click():
            SceneManager.SceneMananger.goToScene("MainMenu")

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]: self.boxY -= 3
        if pressed[pygame.K_s]: self.boxY += 3
        if pressed[pygame.K_a]: self.boxX -= 3
        if pressed[pygame.K_d]: self.boxX += 3

    # The function of this method is explained in the class Scene
    def handle_events(self, events):
        for e in events:
            pass  # In python you must implement stuff like this if statement, i dont want to implement it yet so i simple write pass wich does nothing you could say that this if statements implementation is empty