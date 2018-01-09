import pygame
import SceneManager

class InstructionsScene(SceneManager.Scene):

    def __init__(self):
        super(InstructionsScene, self).__init__()
        self.headerFont = pygame.font.SysFont("monospace", 72)
        self.myfont = pygame.font.SysFont("monospace", 56)

    def render(self, screen):
        screen.fill((0, 0, 0))
        header = self.headerFont.render("Instructions", 1, (255, 255, 255))
        screen.blit(header, (300, 100))
        Line1 = self.myfont.render("Your goal is always to get", 1, (255, 255, 255))
        screen.blit(Line1, (300, 200))
        Line2 = self.myfont.render("the ball past the white bar", 1, (255, 255, 255))
        screen.blit(Line2, (300, 250))
        Line3 = self.myfont.render("on the opposite side of the screen.", 1, (255, 255, 255))
        screen.blit(Line3, (300, 300))
        Line4 = self.myfont.render("The player on the left uses W & S to", 1, (255, 255, 255))
        screen.blit(Line4, (300, 400))
        Line5 = self.myfont.render("move up and down, the player on the", 1, (255, 255, 255))
        screen.blit(Line5, (300, 450))
        Line6 = self.myfont.render("right uses the arrow keys.", 1, (255, 255, 255))
        screen.blit(Line6, (300, 500))
        command = self.myfont.render("Press SPACE to return.", 1, (255, 255, 255))
        screen.blit(command, (350, 750))

        #pygame.draw.rect(screen, [255, 255, 255], pygame.Rect, (60, 420, 30, 180))

    def update(self, deltaTime):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            SceneManager.SceneManager.goToScene("Pong.PongMainMenuScene.PongMainMenuScene")

    def handle_events(self, events):
        pass