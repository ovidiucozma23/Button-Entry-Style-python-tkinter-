#################################################
#	Filename: buttons.py (File with buttons classes)
#	Author: Ovidiu
#	Date: 2023-10-23
#################################################
import tkinter as tk
from tkinter import ttk

# Blue Button
class BlueButton(tk.Button):

	__BACKGROUND = '#0d6efd'
	__ACTIVEBACKGROUND = '#3084ff'
	__FOREGROUND = '#ffffff'
	__ACTIVEFOREGROUND = '#ffffff'
	__DISABLEDBACKGROUND = '#9e9e9e'

	def __init__(self, parent, action):
		super().__init__(parent,
			text = 'Primary Button',
			cursor = 'hand2',
			font = ('Segoe UI', 9),
			border = 2,
			relief = 'flat',
			background = self.__BACKGROUND,
			activebackground = self.__ACTIVEBACKGROUND,
			foreground = self.__FOREGROUND,
			activeforeground = self.__ACTIVEFOREGROUND,
			disabledforeground = self.__DISABLEDBACKGROUND,
			justify = 'center',
			padx = 0,
			pady = 0,
			state = 'normal',
			underline = -1,
			width = 0,
			wraplength = 0,
			command = action)

		self.bind('<Enter>', self.__on_hover)
		self.bind('<Leave>', self.__on_leave)

	def __on_hover(self, event):
		if self['state'] == 'normal':
			self['background'] = self.__ACTIVEBACKGROUND

	def __on_leave(self, event):
		self['background'] = self.__BACKGROUND

# Green Button
class GreenButton(tk.Button):

	__BACKGROUND = '#198754'
	__ACTIVEBACKGROUND = '#20ab6b'
	__FOREGROUND = '#ffffff'
	__ACTIVEFOREGROUND = '#ffffff'
	__DISABLEDBACKGROUND = '#9e9e9e'

	def __init__(self, parent, action):
		super().__init__(parent,
			text = 'Blue Button',
			cursor = 'hand2',
			font = ('Segoe UI', 9),
			border = 0,
			relief = 'flat',
			background = self.__BACKGROUND,
			activebackground = self.__ACTIVEBACKGROUND,
			foreground = self.__FOREGROUND,
			activeforeground = self.__ACTIVEFOREGROUND,
			disabledforeground = self.__DISABLEDBACKGROUND,
			justify = 'center',
			padx = 0,
			pady = 0,
			state = 'normal',
			underline = -1,
			width = 0,
			wraplength = 0,
			command = action)

		self.bind('<Enter>', self.__on_hover)
		self.bind('<Leave>', self.__on_leave)

	def __on_hover(self, event):
		if self['state'] == 'normal':
			self['background'] = self.__ACTIVEBACKGROUND

	def __on_leave(self, event):
		self['background'] = self.__BACKGROUND

# Green Button
class GreenButton(tk.Button):

	__BACKGROUND = '#198754'
	__ACTIVEBACKGROUND = '#20ab6b'
	__FOREGROUND = '#ffffff'
	__ACTIVEFOREGROUND = '#ffffff'
	__DISABLEDBACKGROUND = '#9e9e9e'

	def __init__(self, parent, action):
		super().__init__(parent,
			text = 'Green Button',
			cursor = 'hand2',
			font = ('Segoe UI', 9),
			border = 0,
			relief = 'flat',
			background = self.__BACKGROUND,
			activebackground = self.__ACTIVEBACKGROUND,
			foreground = self.__FOREGROUND,
			activeforeground = self.__ACTIVEFOREGROUND,
			disabledforeground = self.__DISABLEDBACKGROUND,
			justify = 'center',
			padx = 0,
			pady = 0,
			state = 'normal',
			underline = -1,
			width = 0,
			wraplength = 0,
			command = action)

		self.bind('<Enter>', self.__on_hover)
		self.bind('<Leave>', self.__on_leave)

	def __on_hover(self, event):
		if self['state'] == 'normal':
			self['background'] = self.__ACTIVEBACKGROUND

	def __on_leave(self, event):
		self['background'] = self.__BACKGROUND

# Yellow Button
class YellowButton(tk.Button):

	__BACKGROUND = '#fcbf05'
	__ACTIVEBACKGROUND = '#ffd963'
	__FOREGROUND = '#000000'
	__ACTIVEFOREGROUND = '#000000'
	__DISABLEDBACKGROUND = '#9e9e9e'

	def __init__(self, parent, action):
		super().__init__(parent,
			text = 'Yellow Button',
			cursor = 'hand2',
			font = ('Segoe UI', 9),
			border = 0,
			relief = 'flat',
			background = self.__BACKGROUND,
			activebackground = self.__ACTIVEBACKGROUND,
			foreground = self.__FOREGROUND,
			activeforeground = self.__ACTIVEFOREGROUND,
			disabledforeground = self.__DISABLEDBACKGROUND,
			justify = 'center',
			padx = 0,
			pady = 0,
			state = 'normal',
			underline = -1,
			width = 0,
			wraplength = 0,
			command = action)

		self.bind('<Enter>', self.__on_hover)
		self.bind('<Leave>', self.__on_leave)

	def __on_hover(self, event):
		if self['state'] == 'normal':
			self['background'] = self.__ACTIVEBACKGROUND

	def __on_leave(self, event):
		self['background'] = self.__BACKGROUND

# Orange Button
class OrangeButton(tk.Button):

	__BACKGROUND = '#fd7e14'
	__ACTIVEBACKGROUND = '#faa761'
	__FOREGROUND = '#000000'
	__ACTIVEFOREGROUND = '#000000'
	__DISABLEDBACKGROUND = '#9e9e9e'

	def __init__(self, parent, action):
		super().__init__(parent,
			text = 'Orange Button',
			cursor = 'hand2',
			font = ('Segoe UI', 9),
			border = 0,
			relief = 'flat',
			background = self.__BACKGROUND,
			activebackground = self.__ACTIVEBACKGROUND,
			foreground = self.__FOREGROUND,
			activeforeground = self.__ACTIVEFOREGROUND,
			disabledforeground = self.__DISABLEDBACKGROUND,
			justify = 'center',
			padx = 0,
			pady = 0,
			state = 'normal',
			underline = -1,
			width = 0,
			wraplength = 0,
			command = action)

		self.bind('<Enter>', self.__on_hover)
		self.bind('<Leave>', self.__on_leave)

	def __on_hover(self, event):
		if self['state'] == 'normal':
			self['background'] = self.__ACTIVEBACKGROUND

	def __on_leave(self, event):
		self['background'] = self.__BACKGROUND

# Indigo Button
class IndigoButton(tk.Button):

	__BACKGROUND = '#6610f2'
	__ACTIVEBACKGROUND = '#8945f7'
	__FOREGROUND = '#ffffff'
	__ACTIVEFOREGROUND = '#ffffff'
	__DISABLEDBACKGROUND = '#9e9e9e'

	def __init__(self, parent, action):
		super().__init__(parent,
			text = 'Indigo Button',
			cursor = 'hand2',
			font = ('Segoe UI', 9),
			border = 0,
			relief = 'flat',
			background = self.__BACKGROUND,
			activebackground = self.__ACTIVEBACKGROUND,
			foreground = self.__FOREGROUND,
			activeforeground = self.__ACTIVEFOREGROUND,
			disabledforeground = self.__DISABLEDBACKGROUND,
			justify = 'center',
			padx = 0,
			pady = 0,
			state = 'normal',
			underline = -1,
			width = 0,
			wraplength = 0,
			command = action)

		self.bind('<Enter>', self.__on_hover)
		self.bind('<Leave>', self.__on_leave)

	def __on_hover(self, event):
		if self['state'] == 'normal':
			self['background'] = self.__ACTIVEBACKGROUND

	def __on_leave(self, event):
		self['background'] = self.__BACKGROUND

# Purple Button
class PurpleButton(tk.Button):

	__BACKGROUND = '#6f42c1'
	__ACTIVEBACKGROUND = '#905bf0'
	__FOREGROUND = '#ffffff'
	__ACTIVEFOREGROUND = '#ffffff'
	__DISABLEDBACKGROUND = '#9e9e9e'

	def __init__(self, parent, action):
		super().__init__(parent,
			text = 'Purple Button',
			cursor = 'hand2',
			font = ('Segoe UI', 9),
			border = 0,
			relief = 'flat',
			background = self.__BACKGROUND,
			activebackground = self.__ACTIVEBACKGROUND,
			foreground = self.__FOREGROUND,
			activeforeground = self.__ACTIVEFOREGROUND,
			disabledforeground = self.__DISABLEDBACKGROUND,
			justify = 'center',
			padx = 0,
			pady = 0,
			state = 'normal',
			underline = -1,
			width = 0,
			wraplength = 0,
			command = action)

		self.bind('<Enter>', self.__on_hover)
		self.bind('<Leave>', self.__on_leave)

	def __on_hover(self, event):
		self['background'] = self.__ACTIVEBACKGROUND

	def __on_leave(self, event):
		self['background'] = self.__BACKGROUND

# Pink Button
class PinkButton(tk.Button):

	__BACKGROUND = '#d63384'
	__ACTIVEBACKGROUND = '#fc5bab'
	__FOREGROUND = '#ffffff'
	__ACTIVEFOREGROUND = '#ffffff'
	__DISABLEDBACKGROUND = '#9e9e9e'

	def __init__(self, parent, action):
		super().__init__(parent,
			text = 'Pink Button',
			cursor = 'hand2',
			font = ('Segoe UI', 9),
			border = 0,
			relief = 'flat',
			background = self.__BACKGROUND,
			activebackground = self.__ACTIVEBACKGROUND,
			foreground = self.__FOREGROUND,
			activeforeground = self.__ACTIVEFOREGROUND,
			disabledforeground = self.__DISABLEDBACKGROUND,
			justify = 'center',
			padx = 0,
			pady = 0,
			state = 'normal',
			underline = -1,
			width = 0,
			wraplength = 0,
			command = action)

		self.bind('<Enter>', self.__on_hover)
		self.bind('<Leave>', self.__on_leave)

	def __on_hover(self, event):
		if self['state'] == 'normal':
			self['background'] = self.__ACTIVEBACKGROUND

	def __on_leave(self, event):
		self['background'] = self.__BACKGROUND

# Red Button
class RedButton(tk.Button):

	__BACKGROUND = '#dc3545'
	__ACTIVEBACKGROUND = '#ff5465'
	__FOREGROUND = '#ffffff'
	__ACTIVEFOREGROUND = '#ffffff'
	__DISABLEDBACKGROUND = '#9e9e9e'

	def __init__(self, parent, action):
		super().__init__(parent,
			text = 'Red Button',
			cursor = 'hand2',
			font = ('Segoe UI', 9),
			border = 0,
			relief = 'flat',
			background = self.__BACKGROUND,
			activebackground = self.__ACTIVEBACKGROUND,
			foreground = self.__FOREGROUND,
			activeforeground = self.__ACTIVEFOREGROUND,
			disabledforeground = self.__DISABLEDBACKGROUND,
			justify = 'center',
			padx = 0,
			pady = 0,
			state = 'normal',
			underline = -1,
			width = 0,
			wraplength = 0,
			command = action)

		self.bind('<Enter>', self.__on_hover)
		self.bind('<Leave>', self.__on_leave)

	def __on_hover(self, event):
		if self['state'] == 'normal':
			self['background'] = self.__ACTIVEBACKGROUND

	def __on_leave(self, event):
		self['background'] = self.__BACKGROUND

# Cyan Button
class CyanButton(tk.Button):

	__BACKGROUND = '#3bdeff'
	__ACTIVEBACKGROUND = '#02a8c9'
	__FOREGROUND = '#000000'
	__ACTIVEFOREGROUND = '#000000'
	__DISABLEDBACKGROUND = '#01667a'

	def __init__(self, parent, action):
		super().__init__(parent,
			text = 'Cyan Button',
			cursor = 'hand2',
			font = ('Segoe UI', 9),
			border = 0,
			relief = 'flat',
			background = self.__BACKGROUND,
			activebackground = self.__ACTIVEBACKGROUND,
			foreground = self.__FOREGROUND,
			activeforeground = self.__ACTIVEFOREGROUND,
			disabledforeground = self.__DISABLEDBACKGROUND,
			justify = 'center',
			padx = 0,
			pady = 0,
			state = 'normal',
			underline = -1,
			width = 0,
			wraplength = 0,
			command = action)

		self.bind('<Enter>', self.__on_hover)
		self.bind('<Leave>', self.__on_leave)

	def __on_hover(self, event):
		if self['state'] == 'normal':
			self['background'] = self.__ACTIVEBACKGROUND

	def __on_leave(self, event):
		self['background'] = self.__BACKGROUND

# Teal Button
class TealButton(tk.Button):

	__BACKGROUND = '#20c997'
	__ACTIVEBACKGROUND = '#37edb7'
	__FOREGROUND = '#000000'
	__ACTIVEFOREGROUND = '#000000'
	__DISABLEDBACKGROUND = '#9e9e9e'

	def __init__(self, parent, action):
		super().__init__(parent,
			text = 'Teal Button',
			cursor = 'hand2',
			font = ('Segoe UI', 9),
			border = 0,
			relief = 'flat',
			background = self.__BACKGROUND,
			activebackground = self.__ACTIVEBACKGROUND,
			foreground = self.__FOREGROUND,
			activeforeground = self.__ACTIVEFOREGROUND,
			disabledforeground = self.__DISABLEDBACKGROUND,
			justify = 'center',
			padx = 0,
			pady = 0,
			state = 'normal',
			underline = -1,
			width = 0,
			wraplength = 0,
			command = action)

		self.bind('<Enter>', self.__on_hover)
		self.bind('<Leave>', self.__on_leave)

	def __on_hover(self, event):
		if self['state'] == 'normal':
			self['background'] = self.__ACTIVEBACKGROUND

	def __on_leave(self, event):
		self['background'] = self.__BACKGROUND

# Black Button
class BlackButton(tk.Button):

	__BACKGROUND = '#000000'
	__ACTIVEBACKGROUND = '#545353'
	__FOREGROUND = '#ffffff'
	__ACTIVEFOREGROUND = '#ffffff'
	__DISABLEDBACKGROUND = '#9e9e9e'

	def __init__(self, parent, action):
		super().__init__(parent,
			text = 'Black Button',
			cursor = 'hand2',
			font = ('Segoe UI', 9),
			border = 0,
			relief = 'flat',
			background = self.__BACKGROUND,
			activebackground = self.__ACTIVEBACKGROUND,
			foreground = self.__FOREGROUND,
			activeforeground = self.__ACTIVEFOREGROUND,
			disabledforeground = self.__DISABLEDBACKGROUND,
			justify = 'center',
			padx = 0,
			pady = 0,
			state = 'normal',
			underline = -1,
			width = 0,
			wraplength = 0,
			command = action)

		self.bind('<Enter>', self.__on_hover)
		self.bind('<Leave>', self.__on_leave)

	def __on_hover(self, event):
		if self['state'] == 'normal':
			self['background'] = self.__ACTIVEBACKGROUND

	def __on_leave(self, event):
		self['background'] = self.__BACKGROUND

# Gray Button
class GrayButton(tk.Button):

	__BACKGROUND = '#4d4f52'
	__ACTIVEBACKGROUND = '#6a6c6e'
	__FOREGROUND = '#ffffff'
	__ACTIVEFOREGROUND = '#ffffff'
	__DISABLEDBACKGROUND = '#9e9e9e'

	def __init__(self, parent, action):
		super().__init__(parent,
			text = 'Gray Button',
			cursor = 'hand2',
			font = ('Segoe UI', 9),
			border = 0,
			relief = 'flat',
			background = self.__BACKGROUND,
			activebackground = self.__ACTIVEBACKGROUND,
			foreground = self.__FOREGROUND,
			activeforeground = self.__ACTIVEFOREGROUND,
			disabledforeground = self.__DISABLEDBACKGROUND,
			justify = 'center',
			padx = 0,
			pady = 0,
			state = 'normal',
			underline = -1,
			width = 0,
			wraplength = 0,
			command = action)

		self.bind('<Enter>', self.__on_hover)
		self.bind('<Leave>', self.__on_leave)

	def __on_hover(self, event):
		if self['state'] == 'normal':
			self['background'] = self.__ACTIVEBACKGROUND

	def __on_leave(self, event):
		self['background'] = self.__BACKGROUND

# White Button
class WhiteButton(tk.Button):

	__BACKGROUND = '#ffffff'
	__ACTIVEBACKGROUND = '#dee2e6'
	__FOREGROUND = '#000000'
	__ACTIVEFOREGROUND = '#000000'
	__DISABLEDBACKGROUND = '#9e9e9e'

	def __init__(self, parent, action):
		super().__init__(parent,
			text = 'Gray Button',
			cursor = 'hand2',
			font = ('Segoe UI', 9),
			border = 1,
			relief = 'solid',
			background = self.__BACKGROUND,
			activebackground = self.__ACTIVEBACKGROUND,
			foreground = self.__FOREGROUND,
			activeforeground = self.__ACTIVEFOREGROUND,
			disabledforeground = self.__DISABLEDBACKGROUND,
			justify = 'center',
			padx = 0,
			pady = 0,
			state = 'normal',
			underline = -1,
			width = 0,
			wraplength = 0,
			command = action)

		self.bind('<Enter>', self.__on_hover)
		self.bind('<Leave>', self.__on_leave)

	def __on_hover(self, event):
		if self['state'] == 'normal':
			self['background'] = self.__ACTIVEBACKGROUND

	def __on_leave(self, event):
		self['background'] = self.__BACKGROUND