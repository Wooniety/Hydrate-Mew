from kivy.uix.screenmanager import Screen

class CatView(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        shop_button = Button(text='Enter Shop')
        shop_button.bind(on_press=self.open_shop)
        self.add_widget(shop_button)
        
    def open_shop(self, instance):
        self.manager.current = 'shop'