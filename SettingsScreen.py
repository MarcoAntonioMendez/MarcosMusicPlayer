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

		# Setting constants to identify buttons
		self.SPANISH_LANGUAGE_BUTTON = 0
		self.ENGLISH_LANGUAGE_BUTTON = 1
		self.FRENCH_LANGUAGE_BUTTON = 2

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
		languages_buttons = self.build_buttons()


		panel_group = Group(
			screens_tabs,
			Text("\n\n"),
			Text(self.textManager.current_language_selected_text, style = "white"),
			Text("\n"),
			languages_buttons
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
		# Managing user's input if the user is located in the first row (tab's row)
		if(self.current_x_pos == self.ROW_ZERO_INDEX):
			if(key == self.inputListener.KEY_RIGHT):
				if( (self.current_y_pos + 1) == (self.tabsManager.EXIT_TAB_INDEX + 1) ):
					self.current_y_pos = 0
				else:
					self.current_y_pos += 1

			elif(key == self.inputListener.KEY_LEFT):
				if( (self.current_y_pos - 1) == -1 ):
					self.current_y_pos = self.tabsManager.EXIT_TAB_INDEX
				else:
					self.current_y_pos -= 1

		# Managing user's input if the user is located in the second row (language selection buttons)
		if(self.current_x_pos == self.ROW_ONE_INDEX):
			if(key == self.inputListener.KEY_RIGHT):
				if( (self.current_y_pos + 1) == (self.FRENCH_LANGUAGE_BUTTON + 1) ):
					self.current_y_pos = 0
				else:
					self.current_y_pos += 1

			elif(key == self.inputListener.KEY_LEFT):
				if( (self.current_y_pos - 1) == -1 ):
					self.current_y_pos = self.FRENCH_LANGUAGE_BUTTON
				else:
					self.current_y_pos -= 1


		# Managing user's input when going up and down the interface
		if key == self.inputListener.KEY_UP:
			if( (self.current_x_pos - 1) == -1 ):
				self.current_x_pos = self.ROW_TWO_INDEX
			else:
				self.current_x_pos -= 1
			self.current_y_pos = 0

		elif key == self.inputListener.KEY_DOWN:
			if( (self.current_x_pos + 1) == (self.ROW_TWO_INDEX + 1) ):
				self.current_x_pos = self.ROW_ZERO_INDEX
			else:
				self.current_x_pos += 1
			self.current_y_pos = 0

		# Managing user's input when enter is pressed.
		if(key == self.inputListener.KEY_ENTER):
			self.process_enter_input()


	def process_enter_input(self):
		# Checking if the user selected a tab to move to another screen
		if(self.tabsManager.is_now_playing_tab_selected(x_pos = self.current_x_pos, y_pos = self.current_y_pos)):
			self.return_action = self.presentation_screen.NOW_PLAYING_SCREEN_ID
			self.current_x_pos = self.ROW_ZERO_INDEX
			self.current_y_pos = self.tabsManager.SETTINGS_TAB_INDEX
		elif(self.tabsManager.is_exit_tab_selected(x_pos = self.current_x_pos, y_pos = self.current_y_pos)):
			self.return_action = self.presentation_screen.EXIT_SCREEN_ID


		# Checking if user change language
		self.check_if_user_changed_language()


	def build_buttons(self):
		"""
		This method creates all of the languages buttons, it checks which button is selected and which is not
		and it paints each button accordingly.

		Returns:
			An object Columns(), containing all of the buttons so they can be added to the outer panel
		"""
		# Defining a dictionary, pairing a button text with a method to check if that button is selected
		buttons_dictionary = {
			self.textManager.spanish_language_text_for_selection: self.is_spanish_button_selected(),
			self.textManager.english_language_text_for_selection: self.is_english_button_selected(),
			self.textManager.french_language_text_for_selection: self.is_french_button_selected()
		}

		language_buttons = []

		for button_text, is_button_selected in buttons_dictionary.items():
			# Checking if the current button being built contains the preferred language
			if(self.textManager.preferred_language == self.textManager.SPANISH and button_text == self.textManager.spanish_language_text_for_selection):
				button_text = "✅ " + button_text + " ✅"
			elif(self.textManager.preferred_language == self.textManager.ENGLISH and button_text == self.textManager.english_language_text_for_selection):
				button_text = "✅ " + button_text + " ✅"
			elif(self.textManager.preferred_language == self.textManager.FRENCH and button_text == self.textManager.french_language_text_for_selection):
				button_text = "✅ " + button_text + " ✅"
			else:
				button_text = "❌ " + button_text + " ❌"


			# Checking if the button is selected
			if is_button_selected:
				language_buttons.append(Panel(Text(button_text, justify="center"), style=self.ITEM_SELECTED_COLOR, box=box.HEAVY))
			else:
				language_buttons.append(Panel(Text(button_text, justify="center"), style=self.ITEM_NOT_SELECTED_COLOR, box=box.HEAVY))


		return Columns(language_buttons, expand=False)


	def is_spanish_button_selected(self):
		"""
		Checks if the values of x_pos and y_pos correspond to the spanish button being selected

		Returns:
			True or False depending if the spanish button is selected at the time
		"""
		if(self.current_x_pos == self.ROW_ONE_INDEX and self.current_y_pos == self.SPANISH_LANGUAGE_BUTTON):
			return True
		else:
			return False


	def is_english_button_selected(self):
		"""
		Checks if the values of x_pos and y_pos correspond to the english button being selected

		Returns:
			True or False depending if the english button is selected at the time
		"""
		if(self.current_x_pos == self.ROW_ONE_INDEX and self.current_y_pos == self.ENGLISH_LANGUAGE_BUTTON):
			return True
		else:
			return False


	def is_french_button_selected(self):
		"""
		Checks if the values of x_pos and y_pos correspond to the french button being selected

		Returns:
			True or False depending if the french button is selected at the time
		"""
		if(self.current_x_pos == self.ROW_ONE_INDEX and self.current_y_pos == self.FRENCH_LANGUAGE_BUTTON):
			return True
		else:
			return False


	def check_if_user_changed_language(self):
		"""
		This method checks if the user decided to change the language.
		"""
		# Checking if the user selected another language button.
		if(self.is_spanish_button_selected()):
			self.textManager.preferred_language = self.textManager.SPANISH
			self.textManager.set_texts()
			self.textManager.update_preferred_language_file()
		elif(self.is_english_button_selected()):
			self.textManager.preferred_language = self.textManager.ENGLISH
			self.textManager.set_texts()
			self.textManager.update_preferred_language_file()
		elif(self.is_french_button_selected()):
			self.textManager.preferred_language = self.textManager.FRENCH
			self.textManager.set_texts()
			self.textManager.update_preferred_language_file()