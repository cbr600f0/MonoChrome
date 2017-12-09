import pygame, random
import SceneManager
from ButtonClass import Button
from Vector2 import Vector2
from SpaceInvaders.enemy.Enemy import Enemy

class SpaceInvaderLevelScene (SceneManager.Scene):

    def __init__(self):
        # get the methods and variables from the base class wich is Scene
        super(SpaceInvaderLevelScene, self).__init__()

    # Background
        self.mainBG_1 = pygame.image.load("SpaceInvaders/images/Background.png").convert()
        self.mainBG_1 = pygame.transform.scale(self.mainBG_1, (1600, 900))
        self.mainBG_2 = self.mainBG_1
        self.mainBG_Y_Speed = 900

    # Sprite groups
        self.allSprites = pygame.sprite.Group()
        self.enemySprites = pygame.sprite.Group()
        self.playerSprites = pygame.sprite.Group()
        self.bulletSprites = pygame.sprite.Group()

    # Player + settings
        self.player = pygame.image.load("SpaceInvaders/images/Player.png").convert_alpha()
        self.player = pygame.transform.scale(self.player, (100, 100))
        self.x = 750
        self.y = 750
        self.speed = 500

    # Create enemies
        for i in range(4):
            for j in range(10):
                spawnPos = Vector2(50 + (j * 100), 100 + (i * 100))
                Enemy(spawnPos, self.allSprites, self.enemySprites)

    def handle_events(self, events):
        pass

    def update(self, deltaTime):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            print("Shoot")
            # Create bullet
            # From player x
            # Go up with speed

        if pressed[pygame.K_LEFT]:
            # Left border
            if (self.x > 0):
                self.x -= (self.speed * deltaTime)

        if pressed[pygame.K_RIGHT]:
            # Right border
            if (self.x < 1500):
                self.x += (self.speed * deltaTime)

        # Background animation
        if self.mainBG_Y_Speed <= 900:
            self.mainBG_Y_Speed += (300 * deltaTime)
        else:
            self.mainBG_Y_Speed = 0

        self.allSprites.update(deltaTime)

    def render(self, screen):
        screen.fill((0, 0, 0))  # Create screen
        screen.blit(self.mainBG_1, (0, self.mainBG_Y_Speed))
        screen.blit(self.mainBG_2, (0, self.mainBG_Y_Speed - 900))

        screen.blit(self.player, (self.x, self.y))

        self.allSprites.draw(screen)

        # Draw lives
        # Draw Current wave
