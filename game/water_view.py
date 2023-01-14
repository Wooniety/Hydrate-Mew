from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button

class WaterView(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.water_drank = 0

    def drink_cup(self):
        self.water_drank += 250

    def remove_cup(self):
        self.water_drank -= 250

    def drink_bottle(self):
        self.water_drank += 750

    def remove_bottle(self):
        self.water_drank -= 750
    



