from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Ellipse

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1, 1, 0)
            Ellipse(pos=(200,200), size=(100,100))