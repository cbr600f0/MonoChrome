import pygame
import inspect
from ButtonClass import Button
from pygame.locals import *
from SceneManager import SceneManager  # This class takes care of switching between scenes (Examples of scene could be: the main menu, Tower Defense, Pong, ETC) Every game is its own scene (For badbois who already have experience with Unity the concept of a scene is the same here as in Unity)
import importlib

try:
    pygame.mixer.pre_init(44100, -16, 2, 1024)
except:
    pass

# Starts the game by initializing pygame
pygame.init()

try:
    pygame.mixer.set_num_channels(110)
except:
    pass
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
SceneManager.goToScene("MonoChromeIntroScene.MonoChromeIntroScene")


# Time that has passed since the last frame
deltaTime = 0

FPSLblFont = pygame.font.SysFont("monospace", 18)
FPSLblFont.set_bold(True)

pygame.mouse.set_visible(True) #makes mouse visible

switchScreenButton = Button(True, None, "Fullscreen", [220, 220, 220], [0, 0, 0], [120, 120, 120], [0, 0, 0], 120, 2, None, 24)

if gameIsInFullscreen == True:
    switchScreenButton.set_text("Windowed")

#Pause overlay stuff
continueBtn = Button(True, None, "Continue", [50, 50, 50], [120, 120, 120], [30, 30, 30], [120, 120, 120], 350, 300, 900, 100)
backToTitleScreenBtn = Button(True, None, "Back to title screen", [50, 50, 50], [120, 120, 120], [30, 30, 30], [120, 120, 120], 350, 450, 900, 100)
muteSoundsBtn = Button(True, None, "Mute/Unmute Music", [50, 50, 50], [120, 120, 120], [30, 30, 30], [120, 120, 120], 350, 600, 900, 100)

pauseOverlayCanvas = pygame.Surface([1600, 900], pygame.SRCALPHA, 32)
pauseOverlayCanvas = pauseOverlayCanvas.convert_alpha()
pauseOverlayCanvas.fill((0, 0, 0, 160))

allSoundIsMuted = False
lastDrawnFrame = None
gameIsPaused = False

while gameIsRunning:

    allEvents = pygame.event.get()
    for event in allEvents:
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:  # Did the user press the bigass red button in the top right close the game by ending the while loop wich is the gameloop
            gameIsRunning = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            gameIsPaused = not gameIsPaused
            lastDrawnFrame = screen.copy()

    if gameIsPaused == False:
        SceneManager.currentScene.handle_events(allEvents)  #Handles the events of the currentScene (the currentScene is the scene wich is playing now)
        SceneManager.currentScene.update(deltaTime)  #Handles the updates of the currentScene (the currentScene is the scene wich is playing now)
        SceneManager.currentScene.render(screen)  #Handles the rendering of the currentScene (the currentScene is the scene wich is playing now)
    else:
        handlePauseOverlay()

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


    if gameIsPaused == False:
        # draw FPS text
        FPSLbl = FPSLblFont.render("FPS: " + str(int(clock.get_fps())), 1, (255, 255, 255))
        screen.blit(FPSLbl, (4, 4))

    pygame.display.update()  # This makes pygame update its canvas thus rendering everything on the screen

    deltaTime = clock.tick(400) / 1000.0  # Calculates time since last frame wich is the deltaTime

    def handlePauseOverlay():

        screen.blit(lastDrawnFrame, (0, 0))
        screen.blit(pauseOverlayCanvas, (0, 0))
        continueBtn.draw(screen)
        backToTitleScreenBtn.draw(screen)
        muteSoundsBtn.draw(screen)

        if continueBtn.click():
            global gameIsPaused
            gameIsPaused = False

        if backToTitleScreenBtn.click():
            global gameIsPaused
            gameIsPaused = False
            pygame.mixer.music.stop()
            SceneManager.goToScene("MainMenu.MainMenuScene.MainMenuScene")

        if muteSoundsBtn.click(): # only works for music NOT sound
            global allSoundIsMuted
            allSoundIsMuted = not allSoundIsMuted
            if allSoundIsMuted:
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()



