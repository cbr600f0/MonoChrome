import MainMenu
from TowerDefense.TowerDefenseMainMenuScene import TowerDefenseMainMenuScene
from MonoChromeIntroScene import MonoChromeIntroScene
from SpaceInvaders.SpaceInvaderScene import SpaceInvaderScene
from Pong.PongScene import PongScene

# LEES DEZE COMMENT
# Boys ik weet niet zeker als je een nieuwe Scene kiest deze Scene dan verder moet gaan hoe hij was zoals ik het nu gedaaan heb of dat als je voor de tweede keer terug gaat naar bijvoorbeeld towerdefense deze weer vanaf het begin moet beginnen

class SceneMananger(object):  # This is the class SceneManager wich manages scenes like changing the currentScene that is playing

    currentScene = None  # This scene that is currently playing

    # If you dont know what a class is or how it works look at this: https://docs.python.org/3/tutorial/classes.html

    # This marks the method as static, static is a part of class so you must first understand how classes work to understand what static is here is a link https://stackoverflow.com/questions/35089576/static-methods-in-oop
    @staticmethod
    def goToScene(sceneName):  # Changes the currentScene to the givin scene
        """
        Go to the givin scene

        @param sceneName: the sceneName to go to
        """
        if sceneName == "MainMenu":
            SceneMananger.currentScene = MainMenu.MainMenuScene()

        elif sceneName == "TowerDefenseMainMenuScene":
            SceneMananger.currentScene = TowerDefenseMainMenuScene()

        elif sceneName == "MonoChromeIntroScene":
            SceneMananger.currentScene = MonoChromeIntroScene()

        elif sceneName == "PongScene":
            SceneMananger.currentScene = PongScene()

        elif sceneName == "SpaceInvaderScene":
            SceneMananger.currentScene = SpaceInvaderScene()