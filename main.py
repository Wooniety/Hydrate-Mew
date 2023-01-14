from kivy.app import App
from kivy.uix.widget import Widget


class CatGame(Widget):
    pass


class CatApp(App):
    def build(self):
        return CatGame()


if __name__ == '__main__':
    CatApp().run()