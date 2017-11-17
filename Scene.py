
class Scene(object): # The base class of all scenes

    # The constructor of the class, look on the internet how classes work to understand what this is
    def __init__(self):
        pass

    def render(self, screen):  # The base method wich the other use classes like: MainMenuScene, implement to render stuff of that scene
        raise NotImplementedError

    def update(self):  # The base method wich the other classes use like: MainMenuScene, implement to update stuff of that scene
        raise NotImplementedError

    def handle_events(self, events):  # The base method wich the other classes use like: MainMenuScene, implement to handle events of that scene
        raise NotImplementedError