import pygame
from Scene import Scene as Scene
import SceneManager
from ButtonClass import Button

class SpaceInvaderScene (Scene):

    def __init__(self):
        super(SpaceInvaderScene, self).__init__()
        self.x = 30     # Player
        self.y = 330    # Player

    def render(self, screen):
        screen.fill((0, 0, 0))  # Create screen

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

    def handle_events(self, events):
        pass