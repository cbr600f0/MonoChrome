import sys, pygame, math, random, SceneManager, Vector2
from BubbleShooter2.Player import Player
from BubbleShooter2.LightBall import LightBall

class BubbleShooterScene(SceneManager.Scene):
    def __init__(self, *optionalSceneParam):
        super(BubbleShooterScene, self).__init__()

        self.gameOver = False
        self.level = optionalSceneParam[0][0]
        self.score = 0
        self.myfont = pygame.font.SysFont("monospace", 25)
        self.myfont.set_bold(True)

        # Loads in the images and changes it where needed
        self.backgroundImage = pygame.image.load('BubbleShooter2\Images\BackgroundDiscoGrid.png').convert_alpha()
        self.backgroundImage = pygame.transform.scale(self.backgroundImage, (1600, 900))
        self.backgroundImageRect = self.backgroundImage.get_rect()

        self.playerSprites = pygame.sprite.Group()
        self.allSpritesGroup = pygame.sprite.Group()
        self.allSprites = pygame.sprite.OrderedUpdates(self.allSpritesGroup)
        self.lightBallSpritesGroup = pygame.sprite.Group()
        self.lightBallSprites = pygame.sprite.OrderedUpdates(self.lightBallSpritesGroup)

        self.lightBallImages = {
                            'Pink': pygame.image.load("BubbleShooter2\Images\Enemy2.png").convert_alpha(),
                            'Orange': pygame.image.load("BubbleShooter2\Images\Enemy3.png").convert_alpha(),
                            'Blue': pygame.image.load("BubbleShooter2\Images\Enemy4.png").convert_alpha(),
                            'Green': pygame.image.load("BubbleShooter2\Images\Enemy5.png").convert_alpha(),
                            'Yellow': pygame.image.load("BubbleShooter2\Images\Enemy6.png").convert_alpha(),
                            'Black': pygame.image.load("BubbleShooter2\Images\Enemy7.png").convert_alpha()
                          }
        self.lightBallCount = 0

        self.level1 = ([400 ,900], [400, 50], [1200, 50], [1200, 700])
        self.level2 = ([0, 50], [1550, 50], [1550, 850], [50, 850], [50, 150], [200, 150], [200, 500])
        if self.level == 1:
            self.routePositions = self.level1
        elif self.level == 2:
            self.routePositions = self.level2
        self.spawnTimer = 0
        self.ballsToSpawn = 30
        self.player = Player(self, self.allSprites, self.lightBallSprites, self.lightBallCount, self.lightBallImages, self.routePositions, self.allSprites, self.playerSprites)

        startBalls = 6

        #     def __init__(self, spawnPos, playerInstance, lightBallImage, lightBallColor, *sprite_groups):
        for i in range(0, self.ballsToSpawn):
            lightBallColor, lightBallImage = random.choice(list(self.lightBallImages.items()))
            self.lightBallCount += 1
            if self.level == 1:
                LightBall(self, (self.routePositions[0][0], self.routePositions[0][1] + ((self.ballsToSpawn * 40) - (40 * startBalls)) - (i * 40)), self.player, self.lightBallCount, lightBallImage, lightBallColor, True, self.routePositions, self.allSprites, self.lightBallSprites)
            elif self.level == 2:
                LightBall(self, (self.routePositions[0][0] - ((self.ballsToSpawn * 40) + (40 * startBalls)) + (i * 40), self.routePositions[0][1]), self.player, self.lightBallCount, lightBallImage, lightBallColor, True, self.routePositions, self.allSprites, self.lightBallSprites)

        self.player.loadNewLightBall()
    def render(self, screen):
        self.allSprites.clear(screen, self.backgroundImage)
        screen.blit(self.backgroundImage, self.backgroundImageRect)
        pygame.draw.lines(screen, [55, 55, 55], False, self.routePositions, 50)
        self.allSprites.draw(screen)
        self.scoreLbl = self.myfont.render("Score: " + str(self.score), True, [0, 180, 0])
        screen.blit(self.scoreLbl, (800, 600))

    def handle_events(self, events):
        self.player.eventHandler = events

    def update(self, deltaTime):

        if len(self.lightBallSprites.sprites()) == 0:
            if self.level == 1:
                self.level = 2
            elif self.level == 2:
                self.level = 1
            SceneManager.SceneManager.goToScene('BubbleShooter2.BubbleShooterScene.BubbleShooterScene', self.level)

        if self.gameOver:
            SceneManager.SceneManager.goToScene('BubbleShooter2.GameOverScene.GameOverScene')

        firstIsGettingPushed = False
        for i in range(len(self.lightBallSprites.sprites())):
            currentLightball = self.lightBallSprites.sprites()[i]
            if currentLightball.isOnRoute:
                if firstIsGettingPushed == False:
                    currentLightball.canMove = True
                    firstIsGettingPushed = True
                if i < len(self.lightBallSprites.sprites()) - 1:
                    nextLightballInList = self.lightBallSprites.sprites()[i + 1]
                    if nextLightballInList.isOnRoute:
                        if currentLightball.position.get_distance(nextLightballInList.position) < 40:
                            nextLightballInList.canMove = True
                        else:
                            nextLightballInList.canMove = False

        self.allSprites.update(deltaTime, self.allSprites, self.lightBallSprites)

    def spawnBalls(self):
        pass