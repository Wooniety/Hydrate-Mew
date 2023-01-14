from game.cat_view import CatView
from game.shop_view import ShopView

import os

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

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
    
def load_kv_files():
    kv_main = os.path.join(os.path.dirname(__file__), 'kv\cat_view.kv')
    Builder.load_file(kv_main)
    kv_game = os.path.join(os.path.dirname(__file__), 'shop_view.kv')
    Builder.load_file(kv_game)

if __name__ == '__main__':
    CatApp().run()