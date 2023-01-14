from game.cat_view import CatView
from game.shop_view import ShopView

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.screenmanager import ScreenManager
from kivy.vector import Vector
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class CatApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        
        # Create an instance of the MainMenuScreen
        cat_view_screen = CatView(name='catview')
        shop_view_screen = ShopView(name='shop')

        # Add the screens to the screen manager
        sm.add_widget(cat_view_screen)
        sm.add_widget(shop_view_screen)
        return sm

if __name__ == '__main__':
    CatApp().run()