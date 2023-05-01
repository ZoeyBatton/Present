import kivy
from kivy.app import App
# from kivymd.app import MDApp
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
# from mapview import FarmersMapView
from kivy_garden.mapview import MapView
from kivy.factory import Factory
import os


Window.size = [700, 700]

#300, 450

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class ThirdScreen(Screen):
    pass  

class FourthScreen(Screen):
    pass

class FifthScreen(Screen):
    pass

class SixthScreen(Screen):
    pass

class SeventhScreen(Screen):
    pass

class EigthScreen(Screen):
    pass

class FLayout(Screen):
    pass

class Blayout(Screen):
    pass

class End(Screen):
    pass

sm = ScreenManager()

class PresentApp(MDApp):
    def build(self):

        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(ThirdScreen(name='third'))
        sm.add_widget(FLayout(name='flayout'))
        sm.add_widget(Blayout(name='blayout'))
        sm.add_widget(FourthScreen(name='fourth'))
        sm.add_widget(FifthScreen(name='fifth'))
        sm.add_widget(SixthScreen(name='sixth'))
        sm.add_widget(SeventhScreen(name='seventh'))
        sm.add_widget(EigthScreen(name='eigth'))
        sm.add_widget(End(name='end'))
        return sm

if __name__ == '__main__':
    PresentApp().run()
