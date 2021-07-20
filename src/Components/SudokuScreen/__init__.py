import kivy
from kivy.uix.widget import Widget
from kivy.uix.button import Button

from kivy.properties import ObjectProperty

from kivy.uix.gridlayout import GridLayout

from kivy.uix.screenmanager import ScreenManager, Screen

class SudokuSubgrid(GridLayout):
	def __init__(self, **kwargs):
		super(SudokuSubgrid, self).__init__(**kwargs)
		self.load_buttons()

	def load_buttons(self):
		for i in range(3*3):
			self.add_widget(Button())

class SudokuGrid(GridLayout):
	def __init__(self, **kwargs):
		super(SudokuGrid, self).__init__(**kwargs)
		self.load_grid()

	def load_grid(self):
		for i in range(3*3):
			self.add_widget(SudokuSubgrid())

class SudokuScreen(Screen):
	pass