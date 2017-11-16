import pygame

intro = True

while intro:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()