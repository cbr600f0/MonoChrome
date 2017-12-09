from Scene import Scene
import importlib

class SceneManager(object):  # This is the class SceneManager wich manages scenes like changing the currentScene

    currentScene = None  # This scene that is currently playing

    @staticmethod
    def goToScene(pathToScene, *optionalSceneParam):  # Changes the currentScene to the givin scene

        module_name, class_name = pathToScene.rsplit(".", 1)
        somemodule = importlib.import_module(module_name)

        sceneClass = getattr(somemodule, class_name)

        if issubclass(sceneClass, Scene):  # Is the sceneClass of type 'Scene'
            if len(optionalSceneParam) > 0:
                SceneManager.currentScene = sceneClass(optionalSceneParam)
            else:
                SceneManager.currentScene = sceneClass()
        else:
            raise TypeError