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
        self.lightBallCount = 0
        int(self.lightBallCount)


        self.routePositions = ([400 ,700], [400, 50], [1200, 50], [1200, 700])
        self.spawnTimer = 0
        self.ballsToSpawn = 20
        self.player = Player(self, self.allSprites, self.lightBallSprites, self.lightBallCount, self.lightBallImages, self.routePositions, self.allSprites, self.playerSprites)


        mark = 0
        #     def __init__(self, spawnPos, playerInstance, lightBallImage, lightBallColor, *sprite_groups):
        for i in range(0, self.ballsToSpawn):
            mark += 1
            if mark == 2:
                mark = 0
                lightBallColor, lightBallImage = random.choice(list(self.lightBallImages.items()))
                LightBall(self, (self.routePositions[0][0], self.routePositions[0][1] - 45 * i), self.player, self.lightBallCount, lightBallImage, lightBallColor, True, self.routePositions, self.allSprites, self.lightBallSprites)

    def render(self, screen):
        self.allSprites.clear(screen, self.backgroundImage)
        screen.blit(self.backgroundImage, self.backgroundImageRect)
        pygame.draw.lines(screen, [55, 55, 55], False, self.routePositions, 50)
        self.allSprites.draw(screen)

    def handle_events(self, events):
        self.player.eventHandler = events
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousePos = pygame.mouse.get_pos()
                for sprite in self.lightBallSprites.sprites():

                    if sprite.rect.collidepoint(mousePos):
                        sprite.kill()

    def update(self, deltaTime):

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