

class TextManager:
	"""Class for managing all texts for the app.

	This class is in charge of:
    	1. Read and write user's preferred language for the app.
    	2. Set and get the values in the selected language for all texts displayed in the app.


    Attributes:
    	ENGLISH (str): A constant for the english language.
    	SPANISH (str): A constant for the spanish language.
    	FRENCH (str): A constant for the french language.
    	preferred_language (str): Variable for the user's selected language.

    	--------------------------------------------------- These variables are for the PresentationScreen -----------------------------------------------
    	panel_title_text (str): Variable for the title of the panel that surrounds the app.
    	welcome_message_text (str): Variable for the welcome message displayed in the PresentationScreen.

    	---------------------------------------------------------- This variables are for the tabs --------------------------------------------------------
    	now_playing_tab_text (str): Variable for the text of the "Now Playing" tab (This tab appears in the top side at almost all moments).
    	tracks_tab_text (str): Variable for the text of the "Tracks" tab (This tab appears in the top side at almost all moments).
    	artists_tab_text (str): Variable for the text of the "Artists" tab (This tab appears in the top side at almost all moments).
    	albums_tab_text (str): Variable for the text of the "Album" tab (This tab appears in the top side at almost all moments).
    	genres_tab_text (str): Variable for the text of the "Genres" tab (This tab appears in the top side at almost all moments).
    	settings_tab_text (str): Variable for the text of the "Settings" tab (This tab appears in the top side at almost all moments).
    	exit_tab_text (str): Variable for the text of the "Exit" tab (This tab appears in the top side at almost all moments).

    	--------------------------------------------------------- These variables are for the ExitScreen --------------------------------------------------
    	thank_you_text (str): Variable for the text thanking the user to user the software.
    	press_enter_to_finish_text (str): Variable for the text asking the user to press enter to exit the software.
	"""

	def __init__(self):
		"""Initialize a TextManager instance.
		"""
		# Setting up constants
		self.ENGLISH = "ENGLISH"
		self.SPANISH = "SPANISH"
		self.FRENCH = "FRENCH"

		# Reading the preferred language saved
		with open("config/preferred_language.mmp") as preferred_language_file:
			self.preferred_language = str(preferred_language_file.read())

		# Setting texts
		if self.preferred_language == self.ENGLISH:
			self.set_presentation_screen_texts_in_english()
			self.set_tabs_texts_in_english()
			self.set_exit_screen_texts_in_english()

		elif self.preferred_language == self.SPANISH:
			self.set_presentation_screen_texts_in_spanish()
			self.set_tabs_texts_in_spanish()
			self.set_exit_screen_texts_in_spanish()

		elif self.preferred_language == self.FRENCH:
			self.set_presentation_screen_texts_in_french()
			self.set_tabs_texts_in_french()
			self.set_exit_screen_texts_in_french()


	def set_presentation_screen_texts_in_english(self):
		"""Sets values in english for the texts displayed in PresentationScreen
        """
		self.panel_title_text = "Marco's Music Player"
		self.welcome_message_text = "Press enter to start to start listening to music 🎵..."


	def set_presentation_screen_texts_in_spanish(self):
		"""Sets values in spanish for the texts displayed in PresentationScreen
        """
		self.panel_title_text = "El Reproductor De Música De Marco"
		self.welcome_message_text = "Presione enter para comenzar a escuchar música 🎵..."


	def set_presentation_screen_texts_in_french(self):
		"""Sets values in french for the texts displayed in PresentationScreen
        """
		self.panel_title_text = "Le Lecteur De Musique De Marco"
		self.welcome_message_text = "Appuyez Sur Entrée Pour Commencer à Écouter De La Musique 🎵..."


	def set_tabs_texts_in_english(self):
		"""Sets values in english for the texts of the tabs
		"""
		self.now_playing_tab_text = "🎧Now Playing🎧"
		self.tracks_tab_text = "📜Tracks📜"
		self.artists_tab_text = "🌟Artists🌟"
		self.albums_tab_text = "💿Albums💿"
		self.genres_tab_text = "🌛Genres🌜"
		self.settings_tab_text = "🔨Settings🔨"
		self.exit_tab_text = "🔱Exit🔱"


	def set_tabs_texts_in_spanish(self):
		"""Sets values in spanish for the texts of the tabs
		"""
		self.now_playing_tab_text = "🎧Reproduciendo🎧"
		self.tracks_tab_text = "📜Pistas📜"
		self.artists_tab_text = "🌟Artistas🌟"
		self.albums_tab_text = "💿Álbumes💿"
		self.genres_tab_text = "🌛Géneros🌜"
		self.settings_tab_text = "🔨Configuraciones🔨	"
		self.exit_tab_text = "🔱Salir🔱"


	def set_tabs_texts_in_french(self):
		"""Sets values in french for the texts of the tabs
		"""
		self.now_playing_tab_text = "🎧Écouter🎧"
		self.tracks_tab_text = "📜Liste Des Titres📜"
		self.artists_tab_text = "🌟Artistes🌟"
		self.albums_tab_text = "💿Albums💿"
		self.genres_tab_text = "🌛Genres🌜"
		self.settings_tab_text = "🔨Paramètres🔨"
		self.exit_tab_text = "🔱Sortir🔱"


	def set_exit_screen_texts_in_english(self):
		"""Sets values in english for the texts of the ExitScreen
		"""
		self.thank_you_text = "Thank You For Using"
		self.press_enter_to_finish_text = "Press Enter To Finish 👋..."


	def set_exit_screen_texts_in_spanish(self):
		"""Sets values in english for the texts of the ExitScreen
		"""
		self.thank_you_text = "Gracias Por Usar"
		self.press_enter_to_finish_text = "Presione Enter Para Finalizar 👋..."


	def set_exit_screen_texts_in_french(self):
		"""Sets values in english for the texts of the ExitScreen
		"""
		self.thank_you_text = "Merci D'avoir Utilisé"
		self.press_enter_to_finish_text = "Appuyez Sur Entrée Pour Terminer 👋..."