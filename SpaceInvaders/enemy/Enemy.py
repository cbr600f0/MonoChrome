import pygame
from Vector2 import Vector2

class Enemy(pygame.sprite.Sprite):

    def __init__(self, pos, *sprite_groups):
        super().__init__(*sprite_groups)

        self.enemyImage1 = pygame.image.load("SpaceInvaders/images/Enemy1.png").convert_alpha()
        self.enemyImage1 = pygame.transform.scale(self.enemyImage1, (100, 100))
        self.enemyMask = pygame.mask.from_surface(self.enemyImage1)

        self.position = pos
        self.direction = 0  # What is the angle of this enemy(used for rotating)
        self.health = 100

        self.movementSideways = 6
        self.movementSpeed = 100
        self.movementDirectionToRight = True
        self.movementMoveEnemy = False

        self.movementTimer = 100
        self.movementTimerOriginalTime = self.movementTimer

        self.hasDied = False

        self.image = self.enemyImage1
        self.rect = self.enemyImage1.get_rect()

        self.rect.center = self.position

    def takeDamage(self, damageTaken):
        pass
        # raise NotImplemented
        self.health -= damageTaken

        if self.health > 0:
            self.die()

    def die(self):
        pass
        #raise NotImplemented

        if self.hasDied is False:
            self.kill()
            self.hasDied = True

    def update(self, deltaTime):

        if self.hasDied is False:

            # Must move
            if self.movementTimer == 0:
                self.movementMoveEnemy = True

            # Timer
            if self.movementTimer > 0:
                self.movementTimer -= 1
            else:
                self.movementTimer = self.movementTimerOriginalTime

            # Move enemy
            if self.movementMoveEnemy:
                if self.movementSideways > 0:
                    if self.movementDirectionToRight:
                        # Left
                        print("Pos:" + str(self.position))
                        self.position = self.position + Vector2(self.movementSpeed, 0)
                        print("Pos:" + str(self.position))
                        # self.position += moveToMousePosVector * self.movementSpeed * deltaTime
                    else:
                        # Right
                        self.position = self.position - Vector2(self.movementSpeed, 0)
                    self.movementSideways -= 1
                else:
                    # Go downwards
                    self.position = self.position + Vector2(0, self.movementSpeed)

                    if self.movementDirectionToRight:
                        self.movementDirectionToRight = False
                    else:
                        self.movementDirectionToRight = True

                    self.movementSideways = 6

                self.movementMoveEnemy = False
            # Move 6x sideways
            # Move 1x down
            # Reverse direction
            # Ect

