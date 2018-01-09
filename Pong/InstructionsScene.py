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
        screen.blit(header, (30, 100))
        Line1 = self.myfont.render("Your goal is always to get", 1, (255, 255, 255))
        screen.blit(Line1, (30, 200))
        Line2 = self.myfont.render("the ball past the white bar", 1, (255, 255, 255))
        screen.blit(Line2, (30, 250))
        Line3 = self.myfont.render("on the opposite side of the screen.", 1, (255, 255, 255))
        screen.blit(Line3, (30, 300))
        Line4 = self.myfont.render("The player on the left uses W & S to", 1, (255, 255, 255))
        screen.blit(Line4, (30, 400))
        Line5 = self.myfont.render("move up and down, the player on the", 1, (255, 255, 255))
        screen.blit(Line5, (30, 450))
        Line6 = self.myfont.render("right uses the arrow keys.", 1, (255, 255, 255))
        screen.blit(Line6, (30, 500))
        command = self.myfont.render("Press SPACE to return.", 1, (255, 255, 255))
        screen.blit(command, (350, 750))

        up = self.headerFont.render("W/↑", 1, (255, 255, 255))
        screen.blit(up, (1375, 90))
        down = self.headerFont.render("S/↓", 1, (255, 255, 255))
        screen.blit(down, (1375, 620))
        pygame.draw.rect(screen, [255, 255, 255], pygame.Rect(1400, 220, 60, 360))


    def update(self, deltaTime):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            SceneManager.SceneManager.goToScene("Pong.PongMainMenuScene.PongMainMenuScene")

    def handle_events(self, events):
        pass