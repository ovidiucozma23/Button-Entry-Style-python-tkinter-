#################################################
#	Filename: main.py
#	Author: Ovidiu
#	Date: 2023-10-23
#################################################
import tkinter as tk
from tkinter import ttk
from buttons import *
from inputs import *

class Window(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title('Buttons And Inputs')
		self.geometry('750x500+100+100')

		self.create_buttons()
		self.create_inputs()

	def create_buttons(self):
		# Create Buttons
		blue_button = BlueButton(self, 'command') # Put name function without punctuation mark ('')
		green_button = GreenButton(self, 'command') # Put name function without punctuation mark ('')
		yellow_button = YellowButton(self, 'command') # Put name function without punctuation mark ('')
		orange_button = OrangeButton(self, 'command') # Put name function without punctuation mark ('')
		indigo_button = IndigoButton(self, 'command') # Put name function without punctuation mark ('')
		purple_button = PurpleButton(self, 'command') # Put name function without punctuation mark ('')
		pink_button = PinkButton(self, 'command') # Put name function without punctuation mark ('')
		red_button = RedButton(self, 'command') # Put name function without punctuation mark ('')
		cyan_button = CyanButton(self, 'command') # Put name function without punctuation mark ('')
		teal_button = TealButton(self, 'command') # Put name function without punctuation mark ('')
		black_button = BlackButton(self, 'command') # Put name function without punctuation mark ('')
		gray_button = GrayButton(self, 'command') # Put name function without punctuation mark ('')
		white_button = WhiteButton(self, 'command') # Put name function without punctuation mark ('')

		# Show Buttons
		blue_button.place(x = 10, y = 10, width = 130, height = 35)
		green_button.place(x = 150, y = 10, width = 130, height = 35)
		yellow_button.place(x = 290, y = 10, width = 130, height = 35)
		orange_button.place(x = 430, y = 10, width = 130, height = 35)
		indigo_button.place(x = 570, y = 10, width = 130, height = 35)

		purple_button.place(x = 10, y = 55, width = 130, height = 35)
		pink_button.place(x = 150, y = 55, width = 130, height = 35)
		red_button.place(x = 290, y = 55, width = 130, height = 35)
		cyan_button.place(x = 430, y = 55, width = 130, height = 35)
		teal_button.place(x = 570, y = 55, width = 130, height = 35)

		black_button.place(x = 10, y = 100, width = 130, height = 35)
		gray_button.place(x = 150, y = 100, width = 130, height = 35)
		white_button.place(x = 290, y = 100, width = 130, height = 35)

	def create_inputs(self):
		self.input_value = tk.StringVar() # this must be different for each input
		# Create Inputs
		blue_input = BlueInput(self, self.input_value)
		green_input = GreenInput(self, self.input_value)
		red_input = RedInput(self, self.input_value)
		white_input = WhiteInput(self, self.input_value)
		yellow_input = YellowInput(self, self.input_value)
		orange_input = OrangeInput(self, self.input_value)
		purple_input = PurpleInput(self, self.input_value)
		cyan_input = CyanInput(self, self.input_value)
		teal_input = TealInput(self, self.input_value)
		gray_input = GrayInput(self, self.input_value)
		black_input = BlackInput(self, self.input_value)

		# Show Inputs
		blue_input.place(x = 10, y = 150, width = 200, height = 30)
		green_input.place(x = 10, y = 190, width = 200, height = 30)
		red_input.place(x = 10, y = 230, width = 200, height = 30)
		white_input.place(x = 10, y = 270, width = 200, height = 30)
		yellow_input.place(x = 10, y = 310, width = 200, height = 30)
		orange_input.place(x = 10, y = 350, width = 200, height = 30)
		purple_input.place(x = 10, y = 390, width = 200, height = 30)

		cyan_input.place(x = 220, y = 150, width = 200, height = 30)
		teal_input.place(x = 220, y = 190, width = 200, height = 30)
		gray_input.place(x = 220, y = 230, width = 200, height = 30)
		black_input.place(x = 220, y = 270, width = 200, height = 30)


	def run(self):
		self.mainloop()

if __name__ == '__main__':
	app = Window()
	app.run()

