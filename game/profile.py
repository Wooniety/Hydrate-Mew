from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class Profile(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.textinput = TextInput(text='Enter Cat Name:',size_hint=(1, .2), pos_hint={'center_x': .5, 'center_y': .5})
        self.button = Button(text="Submit",size_hint=(1, .2))
        layout.add_widget(self.textinput)
        layout.add_widget(self.button)
        self.add_widget(layout)
