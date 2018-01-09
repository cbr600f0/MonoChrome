import pygame
import SceneManager

class Player2VictoryScene(SceneManager.Scene):

    def __init__(self):
        super(Player2VictoryScene, self).__init__()
        self.headerFont = pygame.font.SysFont("monospace", 128)
        self.myfont = pygame.font.SysFont("monospace", 72)

    def render(self, screen):
        screen.fill((0, 0, 0))
        header = self.headerFont.render("GAME OVER", 1, (255, 255, 255))
        screen.blit(header, (450, 100))
        winner = self.myfont.render("Player 2 wins!", 1, (255, 255, 255))
        screen.blit(winner, (500, 300))
        command = self.myfont.render("Press SPACE to continue", 1, (255, 255, 255))
        screen.blit(command, (350, 750))

    def update(self, deltaTime):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            SceneManager.SceneManager.goToScene("Pong.PongMainMenuScene.PongMainMenuScene")

    def handle_events(self, events):
        pass