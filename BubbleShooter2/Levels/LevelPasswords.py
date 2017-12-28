import sys, pygame, math
from pygame.locals import *

class LevelPasswords():
    def __init__(self, password):
        PasswordList = ["", "Mark", "Vivian"]
        i = 0
        for Password in PasswordList:
            if password == Password:
                return i
            i += 1
        return "You have entered an incorrect password!"

    def render(self, screen):
        pass

    def handle_events(self, events):
        pass

    def update(self, deltaTime):
        pass
