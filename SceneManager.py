import MainMenu
from TowerDefense.TowerDefenseScene import TowerDefenseScene
from MonoChromeIntroScene import MonoChromeIntroScene
from Pong.PongScene import PongScene

# LEES DEZE COMMENT
# Boys ik weet niet zeker als je een nieuwe Scene kiest deze Scene dan verder moet gaan hoe hij was zoals ik het nu gedaaan heb of dat als je voor de tweede keer terug gaat naar bijvoorbeeld towerdefense deze weer vanaf het begin moet beginnen

class SceneMananger(object):  # This is the class SceneManager wich manages scenes like changing the currentScene that is playing

    currentScene = None  # This scene that is currently playing

    __mainMenuScene__ = None  # An empty reference to mainMenuScene this can change if we deside to change the way of changing scenes is handled
    __monoChromeIntroScene__ = None  # An empty reference to mainMenuScene this can change if we deside to change the way of changing scenes is handled
    __towerDefenseScene__ = None  # An empty reference to mainMenuScene this can change if we deside to change the way of changing scenes is handled
    __pongScene__ = None

    # If you dont know what a class is or how it works look at this: https://docs.python.org/3/tutorial/classes.html


    # This marks the method as static, static is a part of class so you must first understand how classes work to understand what static is here is a link https://stackoverflow.com/questions/35089576/static-methods-in-oop
    @staticmethod
    def goToScene(sceneName):  # Changes the currentScene to the givin scene
        """
        Go to the givin scene

        @param sceneName: the sceneName to go to
        """
        if sceneName == "MainMenu":

            if SceneMananger.__mainMenuScene__ == None:  # was the mainMenuScene already loaded once use that scene
                SceneMananger.__mainMenuScene__ = MainMenu.MainMenuScene()

            SceneMananger.currentScene = SceneMananger.__mainMenuScene__

        elif sceneName == "TowerDefense":
            if SceneMananger.__towerDefenseScene__ == None:  # was the towerDefenseScene already loaded once use that scene
                SceneMananger.__towerDefenseScene__ = TowerDefenseScene()

            SceneMananger.currentScene = SceneMananger.__towerDefenseScene__

        elif sceneName == "MonoChromeIntroScene":
            if SceneMananger.__monoChromeIntroScene__ == None:  # was the monochromeIntroScene already loaded once use that scene
                SceneMananger.__monoChromeIntroScene__ = MonoChromeIntroScene()

            SceneMananger.currentScene = SceneMananger.__monoChromeIntroScene__

        elif sceneName == "PongScene":
            if SceneMananger.__pongScene__ == None:  # was the monochromeIntroScene already loaded once use that scene
                SceneMananger.__pongScene__ = PongScene()

            SceneMananger.currentScene = SceneMananger.__pongScene__