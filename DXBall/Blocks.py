import pygame
import SceneManager
from ButtonClass import Button

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

# Size of break-out blocks
block_width = 50
block_height = 25


class Blocks(pygame.sprite.Sprite):
    """This class represents each block that will get knocked out by the ball
    It derives from the "Sprite" class in Pygame """

    def __init__(self, color, x, y, *sprite_groups):
        """ Constructor. Pass in the color of the block,
            and its x and y position. """

        # Call the parent class (Sprite) constructor
        super().__init__(self, *sprite_groups)

        # Create the image of the block of appropriate size
        # The width and height are sent as a list for the first parameter.
        self.Blocks = pygame.Surface([block_width, block_height])

        # Fill the image with the appropriate color
        self.Blocks.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        self.image = self.Blocks
        self.rect = self.Blocks.get_rect()

        # Move the top left of the rectangle to x,y.
        # This is where our block will appear..
        self.rect.x = x
        self.rect.y = y


blocks = pygame.sprite.Group()
allsprites = pygame.sprite.Group()

# The top of the block (y position)
top = 80

# Number of blocks to create
blockcount = 32

# --- Create blocks

# Five rows of blocks
for row in range(5):
    # 32 columns of blocks
    for column in range(0, blockcount):
        # Create a block (color,x,y)
        block = Blocks(blue, column * (block_width + 2) + 1, top)
        blocks.add(block)
        allsprites.add(block)
    # Move the top of the next row down
    top += block_height + 2