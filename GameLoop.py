import pygame
import inspect
from ButtonClass import Button
from pygame.locals import *
from SceneManager import SceneMananger  # This class takes care of switching between scenes (Examples of scene could be: the main menu, Tower Defense, Pong, ETC) Every game is its own scene (For badbois who already have experience with Unity the concept of a scene is the same here as in Unity)
import importlib

# Starts the game by initializing pygame
pygame.init()
gameIsInFullscreen = False  # Change this to False if you want to make the screen windowed at the start

if gameIsInFullscreen == False:
    # Sets to screen size to a specified size
    screen = pygame.display.set_mode((1600, 900))
else:
    # Sets to screen size to a specified size and makes the screen fullscreen
    screen = pygame.display.set_mode((1600, 900), pygame.FULLSCREEN)

# A bool wich says if the game is running or not (if this bool becomes False the whole game will close)
gameIsRunning = True

# Gets a sort of timer from pygame (you can use clock to change the FPS with clock.tick for instance)
clock = pygame.time.Clock()

# Tells the SceneManger to go to the MainMenu Scene (Yes seeing SceneManager.SceneMananger is weird im still trying to understand how i can fix this to be only SceneManager.goToScene(""))
SceneMananger.goToScene("MonoChromeIntroScene.MonoChromeIntroScene")


# Time that has passed since the last frame
deltaTime = 0

FPSLblFont = pygame.font.SysFont("monospace", 18)
FPSLblFont.set_bold(True)

pygame.mouse.set_visible(False) #makes mouse invisible
currentCursorImage = pygame.image.load("SteamPunkCursor.png")
currentCursorImage = pygame.transform.scale(currentCursorImage, (50, 50))

switchScreenButton = Button("Fullscreen", [220, 220, 220], [0, 0, 0], [120, 120, 120], [0, 0, 0], 120, 2, None, 24)

if gameIsInFullscreen == True:
    switchScreenButton.set_text("Windowed")

gameIsPaused = False
while gameIsRunning:

    allEvents = pygame.event.get()
    for event in allEvents:
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # Did the user press the bigass red button in the top right close the game by ending the while loop wich is the gameloop
            gameIsRunning = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            gameIsPaused = not gameIsPaused

    SceneMananger.currentScene.handle_events(allEvents)  #Handles the events of the currentScene (the currentScene is the scene wich is playing now)
    SceneMananger.currentScene.update(deltaTime)  #Handles the updates of the currentScene (the currentScene is the scene wich is playing now)
    SceneMananger.currentScene.render(screen)  #Handles the rendering of the currentScene (the currentScene is the scene wich is playing now)

    switchScreenButton.draw(screen)
    if switchScreenButton.click():
        changedWindowMode = False
        if gameIsInFullscreen == True:
            screen = pygame.display.set_mode((1600, 900))
            gameIsInFullscreen = False
            changedWindowMode = True
            switchScreenButton.set_text("Fullscreen")

        if gameIsInFullscreen == False and changedWindowMode == False:
            screen = pygame.display.set_mode((1600, 900), pygame.FULLSCREEN)
            gameIsInFullscreen = True
            changedWindowMode = True
            switchScreenButton.set_text("Windowed")

    # draw FPS text
    FPSLbl = FPSLblFont.render("FPS: " + str(int(clock.get_fps())), 1, (255, 255, 255))
    screen.blit(FPSLbl, (4, 4))
    mousePos = pygame.mouse.get_pos()
    screen.blit(currentCursorImage, mousePos)
    pygame.display.update()  # This makes pygame update its canvas thus rendering everything on the screen

    deltaTime = clock.tick(400) / 1000.0  # Calculates time since last frame wich is the deltaTime

