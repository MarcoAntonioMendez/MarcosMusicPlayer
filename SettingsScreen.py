from rich.panel import Panel
from rich.console import Console
from TextManager import TextManager
from InputListener import InputListener
from TabsManager import TabsManager
from rich.text import Text
from rich.table import Table 
from rich.console import Group
from rich.layout import Layout
from rich.columns import Columns
from rich import box
import PresentationScreen

class SettingsScreen:
	"""Class small description.

	Class Large description


    Attributes:
	"""

	def __init__(self, presentation_screen: PresentationScreen, console: Console, textManager: TextManager, inputListener: InputListener, tabsManager: TabsManager):
		self.presentation_screen = presentation_screen
		self.console = console
		self.textManager = textManager
		self.inputListener = inputListener
		self.tabsManager = tabsManager


		# Setting constants to identify the "rows" of the interface
		self.ROW_ZERO_INDEX = 0
		self.ROW_ONE_INDEX = 1
		self.ROW_TWO_INDEX = 2

		# Setting constants to identify tabs
		self.SETTINGS_TAB_INDEX = 5
		self.EXIT_TAB_INDEX = 6

		# Setting constants for colors
		self.ITEM_SELECTED_COLOR = "green"
		self.ITEM_NOT_SELECTED_COLOR = "white"
		self.MAIN_EXTERIOR_PANEL_COLOR = "rgb(103,29,163)"

		# Variables for "X" and "Y" "positions", to identify which interface element is selected 
		self.current_x_pos = self.ROW_ZERO_INDEX
		self.current_y_pos = self.tabsManager.SETTINGS_TAB_INDEX



	def update(self):
		self.console.clear()

		# Assuming the user didn't choose to go another screen
		# If this is not the case, the value is changed in method process_enter_input(self)
		self.return_action = self.presentation_screen.SETTINGS_SCREEN_ID

		screens_tabs = self.tabsManager.build_tabs(x_pos = self.current_x_pos, y_pos = self.current_y_pos)

		panel_group = Group(
			screens_tabs,
			Text("\n\n"),
			Text("SettingsScreen?")
		)

		panel_title = "[white]" + self.textManager.panel_title_text + "[/white]"
		panel = Panel(panel_group, title=panel_title, style=self.MAIN_EXTERIOR_PANEL_COLOR, box=box.DOUBLE)
		self.console.print(panel)

		# Listening for key presses
		self.on_key_pressed(self.inputListener.listen_for_key_press())

		return self.return_action



	def on_key_pressed(self, key: int):
		"""
        Catches when the user presses the arrow keys or the enter key.
        When the user presses the arrow keys, the variables:
        	1. self.current_x_pos
        	2. self.current_y_pos
        get updated accordingly.
        ------This causes the in the interface to change which item is selected------

        Args:
            key (int): The key that was pressed.
        """
		if key == self.inputListener.KEY_RIGHT:
			if( (self.current_y_pos + 1) == (self.EXIT_TAB_INDEX + 1) ):
				self.current_y_pos = 0
			else:
				self.current_y_pos += 1

		elif key == self.inputListener.KEY_LEFT:
			if( (self.current_y_pos - 1) == -1 ):
				self.current_y_pos = self.EXIT_TAB_INDEX
			else:
				self.current_y_pos -= 1

		elif key == self.inputListener.KEY_UP:
			if( (self.current_x_pos - 1) == -1 ):
				self.current_x_pos = self.ROW_TWO_INDEX
			else:
				self.current_x_pos -= 1

		elif key == self.inputListener.KEY_DOWN:
			if( (self.current_x_pos + 1) == (self.ROW_TWO_INDEX + 1) ):
				self.current_x_pos = self.ROW_ZERO_INDEX
			else:
				self.current_x_pos += 1

		elif key == self.inputListener.KEY_ENTER:
			self.process_enter_input()


	def process_enter_input(self):
		if(self.tabsManager.is_now_playing_tab_selected(x_pos = self.current_x_pos, y_pos = self.current_y_pos)):
			self.return_action = self.presentation_screen.NOW_PLAYING_SCREEN_ID
			self.current_x_pos = self.ROW_ZERO_INDEX
			self.current_y_pos = self.tabsManager.SETTINGS_TAB_INDEX
		elif(self.tabsManager.is_exit_tab_selected(x_pos = self.current_x_pos, y_pos = self.current_y_pos)):
			self.return_action = self.presentation_screen.EXIT_SCREEN_ID