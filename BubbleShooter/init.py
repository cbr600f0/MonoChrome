def NameSpammer():
    Name = input('whats your name? \n')

    mark = 0
    vivian = True
    while vivian:
        print("no." + str(mark) + ": " + Name)
        if mark == 100:
            vivian = False
        mark += 1

def Racegame():
    import pygame

    pygame.init()
    gameDisplay = pygame.display.set_mode((800,600))
    pygame.display.set_caption('A bit Racey')
    clock = pygame.time.Clock()

    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            print(event)

        pygame.display.update()

        clock.tick(30)

    pygame.quit()
    quit()


class SpecialBubbleShooter():
    Racegame()
    keysPressed = pygame.key.get_pressed()
    if