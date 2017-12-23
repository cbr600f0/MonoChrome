import sys, pygame, math, random, SceneManager, Vector2
from BubbleShooter2.Player import Player
from BubbleShooter2.LightBall import LightBall

class BubbleShooterScene(SceneManager.Scene):
    def __init__(self):
        super(BubbleShooterScene, self).__init__()

        # Loads in the images and changes it where needed
        self.backgroundImage = pygame.image.load('BubbleShooter\Images\BackgroundDiscoGrid.png').convert_alpha()
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

        self.player = Player(self.allSprites, self.lightBallSprites, self.lightBallImages, self.allSprites, self.playerSprites)

        self.routePositions = ([400 ,700], [400, 50], [1200, 50], [1200, 800])
        self.spawnTimer = 0
        self.ballsToSpawn = 10


        #     def __init__(self, spawnPos, playerInstance, lightBallImage, lightBallColor, *sprite_groups):
        for i in range(0, self.ballsToSpawn):
            lightBallColor, lightBallImage = random.choice(list(self.lightBallImages.items()))
            LightBall((self.routePositions[0][0], self.routePositions[0][1] - 45 * i), self.player, lightBallImage, lightBallColor, True, self.routePositions,self.allSprites, self.lightBallSprites)


    def render(self, screen):
        self.allSprites.clear(screen, self.backgroundImage)
        screen.blit(self.backgroundImage, self.backgroundImageRect)
        pygame.draw.lines(screen, [55, 55, 55], False, self.routePositions, 50)
        self.allSprites.draw(screen)

    def handle_events(self, events):
        self.player.eventHandler = events
        for event in events:
            pass

    def update(self, deltaTime):
        for lightBall in self.lightBallSprites:
            if lightBall.isOnRoute:
                lightBall.isLastInLine = True
                break
        self.allSprites.update(deltaTime, self.allSprites, self.lightBallSprites)


    def spawnBalls(self):
        pass