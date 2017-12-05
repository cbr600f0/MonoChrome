import pygame
from Scene import Scene as Scene
import SceneManager
from ButtonClass import Button

class SpaceInvaderMainMenuScene (Scene):

    def __init__(self):
        # Background
        self.mainBG_1 = pygame.image.load("SpaceInvaders/images/Background.png").convert()
        self.mainBG_1 = pygame.transform.scale(self.mainBG_1, (1600, 900))
        self.mainBG_2 = self.mainBG_1

        # get the methods and variables from the base class wich is Scene
        super(SpaceInvaderMainMenuScene, self).__init__()

        # Player
        self.x = 30     # Player
        self.y = 330    # Player

        self.bgY = 900


    def render(self, screen):
        screen.fill((0, 0, 0))  # Create screen
        screen.blit(self.mainBG_1, (0, self.bgY))
        screen.blit(self.mainBG_2, (0, self.bgY - 900))

    def update(self, deltaTime):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            print("Up")
        if pressed[pygame.K_DOWN]:
            print("Down")
        if pressed[pygame.K_LEFT]:
            print("Left")
        if pressed[pygame.K_RIGHT]:
            print("Right")

        if self.bgY <= 900:
            self.bgY = self.bgY + (300 * deltaTime)
        else:
            self.bgY = 0

    def handle_events(self, events):
        pass