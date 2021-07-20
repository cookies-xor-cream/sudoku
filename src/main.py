import kivy

from kivy.config import Config
Config.set('graphics','resizable',0)
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '1000')

from kivy.app import App
from kivy.uix.label import Label

from Components.SudokuScreen import SudokuScreen

from kivy.core.window import Window

class SudokuApp(App):
    def build(self):
        return SudokuScreen()


if __name__ == '__main__':
    SudokuApp().run()
