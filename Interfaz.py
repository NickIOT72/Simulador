import kivy
import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.clock import Clock

Window.size = (800,600)
Config.set('graphics', 'fullscreen', '0')

class MainScreen(Screen):
    pass
    #def __init__(self, **kwargs):
    #    super(MainScreen, self).__init__(**kwargs)
    #    self.text= str(time.asctime())
    #    Clock.schedule_interval(self.update,1)
#
    #def update(self, *args):
    #    self.ids["LlMsg"].text = str(time.asctime())
    #    print(self.ids["LlMsg"].text)

class ScreenManagement(ScreenManager):
    pass

class My1App(App):
    def build(self):
        Builder.load_file("interfaz.kv")
        return ScreenManagement()


if __name__ == '__main__':
    My1App().run()