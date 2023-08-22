from rich.panel import Panel
from TextManager import TextManager
from rich import box
from rich.text import Text
from rich.columns import Columns

class TabsManager:
	"""Class to show the upper tabs.

	Large description of the class


	Attributes:
		attribute_name (int): Attribute description.
	"""

	def __init__(self, textManager: TextManager):
		"""Initialize a TabsManager instance.
		"""
		self.textManager = TextManager()

		# Setting constants to identify tabs
		self.NOW_PLAYING_TAB_INDEX = 0
		self.TRACKS_TAB_INDEX = 1
		self.ARTISTS_TAB_INDEX = 2
		self.ALBUMS_TAB_INDEX = 3
		self.GENRES_TAB_INDEX = 4
		self.SETTINGS_TAB_INDEX = 5
		self.EXIT_TAB_INDEX = 6

		self.ROW_ZERO_INDEX = 0

		# Setting constants for colors
		self.ITEM_SELECTED_COLOR = "green"
		self.ITEM_NOT_SELECTED_COLOR = "white"


	def build_tabs(self, x_pos: int, y_pos: int):
		"""
		This method creates all of the tabs positioned in the top of the software, it checks which tab is selected and which is not
		and it paints each tab accordingly.

		Returns:
			An object Columns(), containing all of the tabs so they can be added to the outer panel
		"""
		# Defining a dictionary, pairing a tab text with a tab method to check if that tab is selected
		tabs_dictionary = {
			self.textManager.now_playing_tab_text: self.is_now_playing_tab_selected(x_pos = x_pos, y_pos = y_pos),
			self.textManager.tracks_tab_text: self.is_tracks_tab_selected(x_pos = x_pos, y_pos = y_pos),
			self.textManager.artists_tab_text: self.is_artists_tab_selected(x_pos = x_pos, y_pos = y_pos),
			self.textManager.albums_tab_text: self.is_albums_tab_selected(x_pos = x_pos, y_pos = y_pos),
			self.textManager.genres_tab_text: self.is_genres_tab_selected(x_pos = x_pos, y_pos = y_pos),
			self.textManager.settings_tab_text: self.is_settings_tab_selected(x_pos = x_pos, y_pos = y_pos),
			self.textManager.exit_tab_text: self.is_exit_tab_selected(x_pos = x_pos, y_pos = y_pos)
		}


		tabs = []
		# Traversing the dictionary to checking which tab is currently selected and painting each tab accordingly
		for tab_text, is_tab_selected in tabs_dictionary.items():
			if(is_tab_selected):
				tabs.append( Panel(Text(tab_text, justify="center"), style=self.ITEM_SELECTED_COLOR, box=box.HEAVY) )
			else:
				tabs.append( Panel(Text(tab_text, justify="center"), style=self.ITEM_NOT_SELECTED_COLOR, box=box.HEAVY) )


		return Columns(tabs, expand=True)


	def is_exit_tab_selected(self, x_pos: int, y_pos: int):
		"""
		Checks if the values of x_pos and y_pos correspond to the "Exit" tab being selected

		Returns:
			True or False depending if the "Exit" tab is selected at the time
		"""
		if(x_pos == self.ROW_ZERO_INDEX and y_pos == self.EXIT_TAB_INDEX):
			return True
		else:
			return False


	def is_now_playing_tab_selected(self, x_pos: int, y_pos: int):
		"""
		Checks if the values of x_pos and y_pos correspond to the "Now Playing" tab being selected

		Returns:
			True or False depending if the "Now Playing" tab is selected at the time
		"""
		if(x_pos == self.ROW_ZERO_INDEX and y_pos == self.NOW_PLAYING_TAB_INDEX):
			return True
		else:
			return False


	def is_tracks_tab_selected(self, x_pos: int, y_pos: int):
		"""
		Checks if the values of x_pos and y_pos correspond to the "Tracks" tab being selected

		Returns:
			True or False depending if the "Tracks" tab is selected at the time
		"""
		if(x_pos == self.ROW_ZERO_INDEX and y_pos == self.TRACKS_TAB_INDEX):
			return True
		else:
			return False


	def is_artists_tab_selected(self, x_pos: int, y_pos: int):
		"""
		Checks if the values of x_pos and y_pos correspond to the "Artists" tab being selected

		Returns:
			True or False depending if the "Artists" tab is selected at the time
		"""
		if(x_pos == self.ROW_ZERO_INDEX and y_pos == self.ARTISTS_TAB_INDEX):
			return True
		else:
			return False


	def is_albums_tab_selected(self, x_pos: int, y_pos: int):
		"""
		Checks if the values of x_pos and y_pos correspond to the "Albums" tab being selected

		Returns:
			True or False depending if the "Albums" tab is selected at the time
		"""
		if(x_pos == self.ROW_ZERO_INDEX and y_pos == self.ALBUMS_TAB_INDEX):
			return True
		else:
			return False


	def is_genres_tab_selected(self, x_pos: int, y_pos: int):
		"""
		Checks if the values of x_pos and y_pos correspond to the "Genres" tab being selected

		Returns:
			True or False depending if the "Genres" tab is selected at the time
		"""
		if(x_pos == self.ROW_ZERO_INDEX and y_pos == self.GENRES_TAB_INDEX):
			return True
		else:
			return False


	def is_settings_tab_selected(self, x_pos: int, y_pos: int):
		"""
		Checks if the values of x_pos and y_pos correspond to the "Settings" tab being selected

		Returns:
			True or False depending if the "Settings" tab is selected at the time
		"""
		if(x_pos == self.ROW_ZERO_INDEX and y_pos == self.SETTINGS_TAB_INDEX):
			return True
		else:
			return False