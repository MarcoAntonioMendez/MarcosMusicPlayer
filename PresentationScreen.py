from rich.panel import Panel
from rich.console import Console
from rich import box
from TextManager import TextManager
from NowPlayingScreen import NowPlayingScreen
from SettingsScreen import SettingsScreen
from ExitScreen import ExitScreen
from InputListener import InputListener
from TabsManager import TabsManager

class PresentationScreen:
	"""Class for the presentation screen.

	This class is in charge of:
    	1. Presenting a little welcome message for the user.
    	2. Initialize a console object to pass it to other clases.
    	3. Initialize a TextManager object to pass it to other classes.
    	4. Initialize a InputListener object to pass it to other classes.
    	5. Initialize each possible screen to have it ready.


    Attributes:
    	NOW_PLAYING_SCREEN_ID (int): Constant to identify the NowPlayingScreen.
    	TRACKS_SCREEN_ID (int): Constant to identify the TracksScreen.
    	ARTISTS_SCREEN_ID (int): Constant to identify the ArtistsScreen.
    	ALBUMS_SCREEN_ID (int): Constant to identify the AlbumsScreen.
    	GENRES_SCREEN_ID (int): Constant to identify the GenresScreen.
    	SETTINGS_SCREEN_ID (int): Constant to identify the SettingsScreen.
    	EXIT_SCREEN_ID (int): Constant to identify the ExitScreen.

    	console (Console): A console object to print stuff to the terminal.
    	textManager (TextManager): A TextManager object to get all texts for this screen.
    	inputListener (InputListener): An InputListener object to manage all of the user's input.

    	nowPlayingScreen (NowPlayingScreen): An object that represents the screen where the current song is being played.
    	exitScreen (ExitScreen): An object that presents the screen when the user has decided to exit the program.

    	active_screen (int): This variable represents which screen is currently active, so the main loop can render it.
	"""

	def __init__(self):
		"""Initialize a PresentationScreen instance.
		"""
		self.NOW_PLAYING_SCREEN_ID = 1
		self.TRACKS_SCREEN_ID = 2
		self.ARTISTS_SCREEN_ID = 3
		self.ALBUMS_SCREEN_ID = 4
		self.GENRES_SCREEN_ID = 5
		self.SETTINGS_SCREEN_ID = 6
		self.EXIT_SCREEN_ID = 7


		self.panel_color = "rgb(103,29,163)"
		self.text_color = "white"


		self.console = Console()
		self.console.show_cursor(show=False)
		self.console.clear()


		self.textManager = TextManager()


		self.inputListener = InputListener()


		# Creating tha PresentationScreen, the panel, panel title and the welcome message
		self.build_presentation_screen()


		#
		self.tabsManager = TabsManager(self.textManager)


		self.nowPlayingScreen = NowPlayingScreen(self, self.console, self.textManager, self.inputListener, self.tabsManager)
		self.settingsScreen = SettingsScreen(self, self.console, self.textManager, self.inputListener, self.tabsManager)
		self.exitScreen = ExitScreen(self.console, self.textManager, self.inputListener)


		self.active_screen = self.NOW_PLAYING_SCREEN_ID


	def start(self):
		"""
			This method starts the main loop of the software.
			In this method, it will be managed which screen is active so it can be rendered.
			Also, it will check when the user decides to exit the software.
		"""
		input("")

		# Main Loop for the whole software
		while(self.active_screen != self.EXIT_SCREEN_ID):
			print(self.active_screen)

			if(self.active_screen == self.NOW_PLAYING_SCREEN_ID):
				self.active_screen = self.nowPlayingScreen.update()

			elif(self.active_screen == self.TRACKS_SCREEN_ID):
				print()
			elif(self.active_screen == self.ARTISTS_SCREEN_ID):
				print()
			elif(self.active_screen == self.ALBUMS_SCREEN_ID):
				print()
			elif(self.active_screen == self.GENRES_SCREEN_ID):
				print()

			elif(self.active_screen == self.SETTINGS_SCREEN_ID):
				self.active_screen = self.settingsScreen.update()

		# Showing the exit screen and pretty much finishing the execution of the software.
		self.exitScreen.start()



	def build_presentation_screen(self):
		"""
			This method builds the panel, panel title and the welcome message
		"""
		# Getting the welcome message text
		welcome_message_text = self.textManager.welcome_message_text


		# Building welcome message so it can fit inside the panel
		line_jumps = round(self.console.size.height/2)-2
		spaces_for_title = (round(self.console.size.width/2)-2) - round(len(welcome_message_text)/2)
		welcome_message = ""


		# Adding line jumps to put message in center
		for i in range(line_jumps):
			welcome_message += "\n"
		
		# Adding some spaces to put message in center
		for i in range(spaces_for_title):
			welcome_message += " "
		welcome_message += "[" + self.text_color + "]" + welcome_message_text + "[/" + self.text_color + "]"

		# Adding line jumps to put message in center
		for i in range(line_jumps):
			welcome_message += "\n"


		# Creating and displaying panel
		panel_title = "[" + self.text_color + "]" + self.textManager.panel_title_text + "[/" + self.text_color + "]"
		panel = Panel(welcome_message, title = panel_title, style = self.panel_color, box = box.DOUBLE)
		self.console.print(panel)