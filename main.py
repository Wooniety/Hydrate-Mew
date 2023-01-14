from game.cat_view import CatView
from game.shop_view import ShopView
from game.water_view import WaterView
from game.profile import Profile

import os

from kivy.config import Config
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

class CatApp(App):
    def build(self):
        self._set_aspect_ratio()
        self.root = ScreenManager()

        self.screen_manager()
        return self.root
    
    def screen_manager(self):
        cat_view_screen = CatView(name='catview')
        shop_view_screen = ShopView(name='shop')
        water_view_screen = WaterView(name='water')
        profile_view_screen = Profile(name='profile')

        self.root.add_widget(cat_view_screen)
        self.root.add_widget(shop_view_screen)
        self.root.add_widget(water_view_screen)
        self.root.add_widget(profile_view_screen)

    def _set_aspect_ratio(self):
        Config.set('graphics', 'width', '480')
        Config.set('graphics', 'height', '854')
        Config.set('graphics', 'resizable', 0)
        Config.write()
    
def load_kv_files():
    kv_catview = os.path.join(os.path.dirname(__file__), 'kv/cat_view.kv')
    Builder.load_file(kv_catview)
    kv_shopview = os.path.join(os.path.dirname(__file__), 'kv/shop_view.kv')
    Builder.load_file(kv_shopview)
    kv_profile = os.path.join(os.path.dirname(__file__), 'kv/profile.kv')
    Builder.load_file(kv_profile)

if __name__ == '__main__':
    load_kv_files()
    CatApp().run()