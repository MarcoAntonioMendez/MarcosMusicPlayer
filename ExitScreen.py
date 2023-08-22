from rich.panel import Panel
from rich.console import Console
from rich import box
from TextManager import TextManager
from InputListener import InputListener
import keyboard
import sys

class ExitScreen:
	"""Class for the exit screen.

	This class is in charge of:
    	1. Saying goodbye to the user.


    Attributes:
    	console (Console): A console object to print stuff to the terminal.
    	textManager (TextManager): A TextManager object to get all texts for this screen.
	"""

	def __init__(self, console: Console, textManager: TextManager, inputListener: InputListener):
		self.console = console
		self.textManager = textManager
		self.inputListener = inputListener

		self.user_has_pressed_enter = False


	def start(self):
		while(not self.user_has_pressed_enter):
			self.console.clear()

			# Getting the goodbye message text
			thank_you_text = self.textManager.thank_you_text
			software_text = self.textManager.panel_title_text
			press_enter_to_finish_text = self.textManager.press_enter_to_finish_text

			# Building welcome message so it can fit inside the panel
			line_jumps = round(self.console.size.height/2)-5
			spaces_for_thank_you = (round(self.console.size.width/2)-2) - round(len(thank_you_text)/2)
			spaces_for_software_title = (round(self.console.size.width/2)-2) - round(len(software_text)/2)
			spaces_press_enter_to_finish = (round(self.console.size.width/2)-2) - round(len(press_enter_to_finish_text)/2)
			goodbye_message = ""


			# Adding line jumps to put message in center
			for i in range(line_jumps):
				goodbye_message += "\n"
			
			# Adding some spaces to put message in center
			for i in range(spaces_for_thank_you):
				goodbye_message += " "
			goodbye_message += "[white]" + thank_you_text + "[/white]"
			goodbye_message += "\n\n\n"



			# Adding some spaces to put message in center
			for i in range(spaces_for_software_title):
				goodbye_message += " "
			goodbye_message += "[white]" + software_text + "[/white]"
			goodbye_message += "\n\n\n"


			# Adding some spaces to put message in center
			for i in range(spaces_press_enter_to_finish):
				goodbye_message += " "
			goodbye_message += "[white]" + press_enter_to_finish_text + "[/white]"


			# Adding line jumps to put message in center
			for i in range(line_jumps):
				goodbye_message += "\n"


			# Creating and displaying panel
			panel = Panel(goodbye_message, style="rgb(103,29,163)", box=box.DOUBLE)
			self.console.print(panel)

			# Listening for key presses
			self.on_key_pressed(self.inputListener.listen_for_key_press())



	def on_key_pressed(self, key: int):
		"""
		This method will check when user presses enter.

		Args:
			key (int): The key that was pressed.
		"""
		if key == self.inputListener.KEY_ENTER:
			self.user_has_pressed_enter = True