import kivy
from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
# from mapview import FarmersMapView
from kivy_garden.mapview import MapView

Window.size = [700, 700]

#300, 450

class FirstScreen(Screen):
    pass

sm = ScreenManager()

class PresentApp(MDApp):
    def build(self):

        sm.add_widget(Builder.load_file('C:/Users/Batton_Zoey/Desktop/Present/Present App/present.kv'))

        sm.add_widget(FirstScreen(name='first'))

        return sm

if __name__ == '__main__':
    PresentApp().run()

# PresentApp().run()