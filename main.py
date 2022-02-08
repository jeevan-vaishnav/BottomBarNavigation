from ast import Import
from turtle import Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

Window.size = (400, 600)


class ScreenOne(Screen):
    pass


sm = ScreenManager()
sm.add_widget(ScreenOne(name="s1"))


class MyApp(MDApp):
    def build(self):

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Lime"

        screen = Screen()
        kv = Builder.load_file('main.kv')
        screen.add_widget(kv)
        return screen


if __name__ == "__main__":
    MyApp().run()
