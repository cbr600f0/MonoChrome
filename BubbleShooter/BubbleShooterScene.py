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

        self.routePositions = ([400, 700], [400, 50], [1200, 50], [1200, 800])
        self.spawnTimer = 0
        self.ballsToSpawn = 10

        # def __init__(self, spawnPos, playerInstance, lightBallImage, lightBallColor, *sprite_groups):
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
        if(len(self.lightBallSprites.sprites()) > 0):
            self.lightBallSprites.sprites()[0].isLastInLine = True
        self.allSprites.update(deltaTime, self.allSprites, self.lightBallSprites)

    def spawnBalls(self):
        pass

    # 1: Think visually (haunted house)
    # 2: Think of the objects needed to create the visual (simple like rectangle for walls)
    # 3: Think how to program those full objects, how to name them and
    #    if there is a better base-object for it (3 rectangles + 2 triangles -> 1 prism)
    # 4: Try to convert it to an other language/project if it doesn't work on first thought
    # 5: write a large comment about how you're gonna program it (write real usable examples)
    # 6: Think if there is a better way to do it or better place to make it.
    # 7: Start making the code piece by piece.

    # Note: Don't think of a game is a whole object. A game is made of functionalities and visuals,
    #       those visuals are made with objects, Functionalities are made of smaller methods WITHIN the object
    #       Only make Methods for the functionalities that your current goal needs (no reason to create what might be changed)

    #-------------------------------------------------------------------------------------------------------------------
    #