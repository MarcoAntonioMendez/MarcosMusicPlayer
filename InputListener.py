import keyboard
import pyautogui

class InputListener:
	"""This class is in charge of recognizing which keys the user presses.

	This class can:
		1. Wait for the user to press a key and then return the key code for such key.
		2. Detect if the terminal is in focus or not.


	Attributes:
		KEY_RIGHT (int): Key code for the right arrow key.
		KEY_LEFT (int): Key code for the left arrow key.
		KEY_UP (int): Key code for the up arrow key.
		KEY_DOWN (int): Key code for the down arrow key.
		KEY_ENTER (int): Key code for the enter key.

		program_title (str): title of the terminal where the program is being executed.
	"""

	def __init__(self):
		"""Initialize a InputListener instance.
		"""
		# Setting the constants for the keys
		self.KEY_RIGHT = 77
		self.KEY_LEFT = 75
		self.KEY_UP = 72
		self.KEY_DOWN = 80
		self.KEY_ENTER = 28

		# Getting console title
		self.program_title = pyautogui.getActiveWindow().title


	def listen_for_key_press(self):
		"""
		Waits for the user to press any key, then checks if the terminal is in focus so the value of the key can be returned. 

		Returns:
			event.scan_code (int): The code for the key that was pressed (if comparison is true).
							(int): The value of -1 (if comparison is false).
		"""
		event = keyboard.read_event()  # Wait for any key press
		if event.event_type == keyboard.KEY_DOWN and self.is_program_in_focus():
			return event.scan_code
		else:
			return -1


	def is_program_in_focus(self):
		"""
		Detects if the terminal where the program is executed is on focus.

		Returns:
			(bool): Weather the terminal is in focus or not.
		"""
		active_window = pyautogui.getActiveWindow()
		return active_window.title == self.program_title