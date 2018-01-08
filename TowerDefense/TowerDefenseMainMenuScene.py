import pygame
import SceneManager

from ButtonClass import Button


class TowerDefenseMainMenuScene(SceneManager.Scene):

    def __init__(self):
        super(TowerDefenseMainMenuScene, self).__init__()

        pygame.mixer.music.load("TowerDefense/Sounds/WesternBackgroundMusic.ogg")
        pygame.mixer.music.set_volume(0.0158)
        pygame.mixer.music.play(-1)

        self.mainBG = pygame.image.load("TowerDefense\Images\MainMenu.png").convert()
        self.mainBG = pygame.transform.scale(self.mainBG, (1600, 900))

        self.westernFont = pygame.font.Font("TowerDefense\WesternFont.otf", 42)
        self.startBtn = Button(False, self.westernFont, "Start", None, None, [127, 110, 95], [110, 90, 73], 715, 195, None, 70)
        self.optionsBtn = Button(False, self.westernFont, "Options", None, None, [127, 110, 95], [110, 90, 73], 700, 360, None, 70)
        self.quitBtn = Button(False, self.westernFont, "Quit to main menu", None, None, [127, 110, 95], [110, 90, 73], 610, 525, None, 70)

    def render(self, screen):
        screen.blit(self.mainBG, (0, 0))

        self.startBtn.draw(screen)
        self.optionsBtn.draw(screen)
        self.quitBtn.draw(screen)

    def update(self, deltaTime):

        if self.startBtn.click():
            SceneManager.SceneManager.goToScene("TowerDefense.Level1Scene.Level1Scene")

        if self.optionsBtn.click():
            pass

        if self.quitBtn.click():
            SceneManager.SceneManager.goToScene("MainMenu.MainMenuScene.MainMenuScene")
            pygame.mixer.music.stop()

    def handle_events(self, events):
        for event in events:
            pass