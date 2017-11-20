import sys, pygame, math
from pygame.locals import *
def NameSpammer():
    Name = input('whats your name? \n')

    mark = 0
    vivian = True
    while vivian:
        print("no." + str(mark) + ": " + Name)
        if mark == 100:
            vivian = False
        mark += 1

def RaceGame():

    pygame.init()
    gameDisplay = pygame.display.set_mode((800,600))
    pygame.display.set_caption('A bit Racey')
    clock = pygame.time.Clock()

    #insert image
    shion = pygame.image.load('Images\ShionSonozaki.jpg')
    shionRect = shion.get_rect()

    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            print(event)
        #check if a key is pressed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            print("The ESC key has been pressed!")
        #display image
        gameDisplay.blit(shion, shionRect)
        pygame.display.update()

        clock.tick(1)

    pygame.quit()
    quit()

def TestStuff():
    #Rotating image towards the mouse
    spaceship = ('Images\BackToBack.jpg')
    mouse_c = ('Images\MSKHigurashi.jpg')
    backg = ('Images\ShionSonozaki.jpg')
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    bk = pygame.image.load(backg).convert_alpha()
    mousec = pygame.image.load(mouse_c).convert_alpha()
    space_ship = pygame.image.load(spaceship).convert_alpha()
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                print("test1")
            elif event.type == MOUSEBUTTONDOWN and event.button == 3:
                print("test3")
        screen.blit(bk, (0, 0))
        pos = pygame.mouse.get_pos()
        screen.blit(mousec, (pos))
        angle = 360 - math.atan2(pos[1] - 300, pos[0] - 400) * 180 / math.pi
        rotimage = pygame.transform.rotate(space_ship, angle)
        rect = rotimage.get_rect(center=(400, 300))
        screen.blit(rotimage, rect)  # I need space_ship to rotate towards my cursor
        pygame.display.update()


class SpecialBubbleShooter():
    TestStuff()