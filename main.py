from game.cat_view import CatView
from game.shop_view import ShopView, FoodView, ToysView
from game.water_view import WaterView
from game.profile import Profile

import os

from kivy.config import Config
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.audio import SoundLoader

class CatApp(App):
    def build(self):
        self._set_aspect_ratio()
        self.bg_music()

        self.root = ScreenManager()
        self.screen_manager()
        return self.root
    
    def bg_music(self):
        bgm_track = os.path.join(os.path.dirname(__file__), 'game\\resources\\bgm.mp3')
        self.sound = SoundLoader.load(bgm_track)
        self.sound.loop = True
        self.sound.volume = 0.05
        self.sound.play()

    def screen_manager(self):
        cat_view_screen = CatView(name='catview')
        shop_view_screen = ShopView(name='shop')
        water_view_screen = WaterView(name='water')
        profile_view_screen = Profile(name='profile')
        food_view_screen = FoodView(name='food')
        toys_view_screen = ToysView(name='toys')

        self.root.add_widget(cat_view_screen)
        self.root.add_widget(shop_view_screen)
        self.root.add_widget(water_view_screen)
        self.root.add_widget(profile_view_screen)
        self.root.add_widget(food_view_screen)
        self.root.add_widget(toys_view_screen)

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
    kv_waterview = os.path.join(os.path.dirname(__file__), 'kv/water_view.kv')
    Builder.load_file(kv_waterview)

if __name__ == '__main__':
    load_kv_files()
    CatApp().run()