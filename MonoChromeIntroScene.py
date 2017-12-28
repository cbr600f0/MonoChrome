import pygame
import SceneManager

class MonoChromeIntroScene(SceneManager.Scene): # MainMenuScene inherits from the class Scene (wich is the base class of all scenes)

    def __init__(self):
        super(MonoChromeIntroScene, self).__init__()  # get the methods and variables from the base class wich is Scene
        self.headerFont = pygame.font.SysFont("monospace", 28)
        self.headerFont.set_bold(True)

    # The function of this method is explained in the class Scene
    def render(self, screen):
        pygame.display.set_caption("MonoChrome intro (Press ESCAPE to close the game)")  # Changes the text of the window
        screen.fill((30, 30, 30))

        # render text
        label = self.headerFont.render("PRESS SPACE TO START THE GAME", 1, (255, 255, 255))
        screen.blit(label, (70, 20))

    # The function of this method is explained in the class Scene
    def update(self, deltaTime):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            SceneManager.SceneManager.goToScene("MainMenu.MainMenuScene.MainMenuScene")  # Changes the scene to MainMenu

    # The function of this method is explained in the class Scene
    def handle_events(self, events):
        pass