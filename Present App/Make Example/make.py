import kivy
from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class FirstScreen(Screen):
    pass
class SecondScreen(Screen):
    pass

sm = ScreenManager()
class Example(App):
    def build(self):
        sm.add_widget(Builder.load_file('make.kv'))

        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        return sm


if __name__ == '__main__':
    Example().run()
