import pygame
from pygame.locals import *
import SceneManager # This class takes care of switching between scenes (Examples of scene could be: the main menu, Tower Defense, Pong, ETC) Every game is its own scene (For badbois who already have experience with Unity the concept of a scene is the same here as in Unity)


# Starts the game by initializing pygame
pygame.init()

# Sets to screen size to a specified size and makes the screen fullscreen
screen = pygame.display.set_mode((600, 400))

# A bool wich says if the game is running or not (if this bool becomes False the whole game will close)
gameIsRunning = True

# Gets a sort of timer from pygame (you can use clock to change the FPS with clock.tick for instance)
clock = pygame.time.Clock()

# Tells the SceneManger to go to the MainMenu Scene (Yes seeing SceneManager.SceneMananger is weird im still trying to understand how i can fix this to be only SceneManager.goToScene(""))
SceneManager.SceneMananger.goToScene("MonoChromeIntroScene")

# Time that has passed since the last frame
deltaTime = 0

while gameIsRunning:

    allEvents = pygame.event.get()
    for event in allEvents:
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # Did the user press the bigass red button in the top right close the game by ending the while loop wich is the gameloop
            gameIsRunning = False

    SceneManager.SceneMananger.currentScene.handle_events(allEvents)  #Handles the events of the currentScene (the currentScene is the scene wich is playing now)
    SceneManager.SceneMananger.currentScene.update(deltaTime)  #Handles the updates of the currentScene (the currentScene is the scene wich is playing now)
    SceneManager.SceneMananger.currentScene.render(screen)  #Handles the rendering of the currentScene (the currentScene is the scene wich is playing now)
    pygame.display.update()  # This makes pygame update its canvas thus rendering everything on the screen

    deltaTime = clock.tick(60) / 1000.0  # Calculates time since last frame wich is the deltaTime

