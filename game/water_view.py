from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button

class WaterView(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.water_drank = 0

    def update_label(self):
        if self.water_drank < 0:
            self.water_drank = 0
        amt_str = f"Water Consumed: {self.water_drank}"
        self.ids.water_drank.text = amt_str

    def drink_cup(self):
        self.water_drank += 250
        self.update_label()

    def remove_cup(self):
        self.water_drank -= 250
        self.update_label()

    def drink_bottle(self):
        self.water_drank += 750
        self.update_label()

    def remove_bottle(self):
        self.water_drank -= 750
        self.update_label()
    
    



