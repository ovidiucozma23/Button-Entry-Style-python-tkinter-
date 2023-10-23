#################################################
#	Filename: inputs.py (File with inputs classes)
#	Author: Ovidiu
#	Date: 2023-10-23
#################################################
import tkinter as tk
from tkinter import ttk

# Blue Input
class BlueInput(tk.Entry):

	__BACKGROUND = '#69a4fa'
	__FOREGROUND = '#ffffff'
	__HIGHLIGHTBACKGROUND = '#0d6efd'
	__HIGHLIGHTCOLOR = '#0000ff'

	def __init__(self, parent, input_value):
		super().__init__(parent,
			background = self.__BACKGROUND,
			foreground = self.__FOREGROUND,
			textvariable = input_value,
			border = 2,
			font = ('Segoe UI', 10),
			justify = 'left',
			relief = 'flat',
			show = '',
			highlightthickness = 2,
			highlightbackground = self.__HIGHLIGHTBACKGROUND,
			highlightcolor = self.__HIGHLIGHTCOLOR)

# Green Input
class GreenInput(tk.Entry):

	__BACKGROUND = '#59ff59'
	__FOREGROUND = '#000000'
	__HIGHLIGHTBACKGROUND = '#25cc25'
	__HIGHLIGHTCOLOR = '#006e00'

	def __init__(self, parent, input_value):
		super().__init__(parent,
			background = self.__BACKGROUND,
			foreground = self.__FOREGROUND,
			textvariable = input_value,
			border = 2,
			font = ('Segoe UI', 10),
			justify = 'left',
			relief = 'flat',
			show = '',
			highlightthickness = 2,
			highlightbackground = self.__HIGHLIGHTBACKGROUND,
			highlightcolor = self.__HIGHLIGHTCOLOR)

# Red Input
class RedInput(tk.Entry):

	__BACKGROUND = '#ff3636'
	__FOREGROUND = '#ffffff'
	__HIGHLIGHTBACKGROUND = '#d12121'
	__HIGHLIGHTCOLOR = '#8a0000'
	
	def __init__(self, parent, input_value):
		super().__init__(parent,
			background = self.__BACKGROUND,
			foreground = self.__FOREGROUND,
			textvariable = input_value,
			border = 2,
			font = ('Segoe UI', 10),
			justify = 'left',
			relief = 'flat',
			show = '',
			highlightthickness = 2,
			highlightbackground = self.__HIGHLIGHTBACKGROUND,
			highlightcolor = self.__HIGHLIGHTCOLOR)

# White Input
class WhiteInput(tk.Entry):

	__BACKGROUND = '#ffffff'
	__FOREGROUND = '#000000'
	__HIGHLIGHTBACKGROUND = '#a6a6a6'
	__HIGHLIGHTCOLOR = '#6e6d6d'
	
	def __init__(self, parent, input_value):
		super().__init__(parent,
			background = self.__BACKGROUND,
			foreground = self.__FOREGROUND,
			textvariable = input_value,
			border = 2,
			font = ('Segoe UI', 10),
			justify = 'left',
			relief = 'flat',
			show = '',
			highlightthickness = 2,
			highlightbackground = self.__HIGHLIGHTBACKGROUND,
			highlightcolor = self.__HIGHLIGHTCOLOR)

# Yellow Input
class YellowInput(tk.Entry):

	__BACKGROUND = '#fcce3f'
	__FOREGROUND = '#000000'
	__HIGHLIGHTBACKGROUND = '#d1a008'
	__HIGHLIGHTCOLOR = '#a37b02'
	
	def __init__(self, parent, input_value):
		super().__init__(parent,
			background = self.__BACKGROUND,
			foreground = self.__FOREGROUND,
			textvariable = input_value,
			border = 2,
			font = ('Segoe UI', 10),
			justify = 'left',
			relief = 'flat',
			show = '',
			highlightthickness = 2,
			highlightbackground = self.__HIGHLIGHTBACKGROUND,
			highlightcolor = self.__HIGHLIGHTCOLOR)

# Orange Input
class OrangeInput(tk.Entry):

	__BACKGROUND = '#ffad69'
	__FOREGROUND = '#000000'
	__HIGHLIGHTBACKGROUND = '#e36902'
	__HIGHLIGHTCOLOR = '#9c4700'
	
	def __init__(self, parent, input_value):
		super().__init__(parent,
			background = self.__BACKGROUND,
			foreground = self.__FOREGROUND,
			textvariable = input_value,
			border = 2,
			font = ('Segoe UI', 10),
			justify = 'left',
			relief = 'flat',
			show = '',
			highlightthickness = 2,
			highlightbackground = self.__HIGHLIGHTBACKGROUND,
			highlightcolor = self.__HIGHLIGHTCOLOR)

# Purple Input
class PurpleInput(tk.Entry):

	__BACKGROUND = '#9b5eff'
	__FOREGROUND = '#ffffff'
	__HIGHLIGHTBACKGROUND = '#6e14ff'
	__HIGHLIGHTCOLOR = '#2e0178'
	
	def __init__(self, parent, input_value):
		super().__init__(parent,
			background = self.__BACKGROUND,
			foreground = self.__FOREGROUND,
			textvariable = input_value,
			border = 2,
			font = ('Segoe UI', 10),
			justify = 'left',
			relief = 'flat',
			show = '',
			highlightthickness = 2,
			highlightbackground = self.__HIGHLIGHTBACKGROUND,
			highlightcolor = self.__HIGHLIGHTCOLOR)

# Cyan Input
class CyanInput(tk.Entry):

	__BACKGROUND = '#3ddfff'
	__FOREGROUND = '#000000'
	__HIGHLIGHTBACKGROUND = '#04a0bf'
	__HIGHLIGHTCOLOR = '#01667a'
	
	def __init__(self, parent, input_value):
		super().__init__(parent,
			background = self.__BACKGROUND,
			foreground = self.__FOREGROUND,
			textvariable = input_value,
			border = 2,
			font = ('Segoe UI', 10),
			justify = 'left',
			relief = 'flat',
			show = '',
			highlightthickness = 2,
			highlightbackground = self.__HIGHLIGHTBACKGROUND,
			highlightcolor = self.__HIGHLIGHTCOLOR)

# Purple Input
class PurpleInput(tk.Entry):

	__BACKGROUND = '#9b5eff'
	__FOREGROUND = '#ffffff'
	__HIGHLIGHTBACKGROUND = '#6e14ff'
	__HIGHLIGHTCOLOR = '#2e0178'
	
	def __init__(self, parent, input_value):
		super().__init__(parent,
			background = self.__BACKGROUND,
			foreground = self.__FOREGROUND,
			textvariable = input_value,
			border = 2,
			font = ('Segoe UI', 10),
			justify = 'left',
			relief = 'flat',
			show = '',
			highlightthickness = 2,
			highlightbackground = self.__HIGHLIGHTBACKGROUND,
			highlightcolor = self.__HIGHLIGHTCOLOR)

# Teal Input
class TealInput(tk.Entry):

	__BACKGROUND = '#2ee6af'
	__FOREGROUND = '#000000'
	__HIGHLIGHTBACKGROUND = '#00966a'
	__HIGHLIGHTCOLOR = '#006144'
	
	def __init__(self, parent, input_value):
		super().__init__(parent,
			background = self.__BACKGROUND,
			foreground = self.__FOREGROUND,
			textvariable = input_value,
			border = 2,
			font = ('Segoe UI', 10),
			justify = 'left',
			relief = 'flat',
			show = '',
			highlightthickness = 2,
			highlightbackground = self.__HIGHLIGHTBACKGROUND,
			highlightcolor = self.__HIGHLIGHTCOLOR)

# Gray Input
class GrayInput(tk.Entry):

	__BACKGROUND = '#adadad'
	__FOREGROUND = '#000000'
	__HIGHLIGHTBACKGROUND = '#4f4f4f'
	__HIGHLIGHTCOLOR = '#000000'
	
	def __init__(self, parent, input_value):
		super().__init__(parent,
			background = self.__BACKGROUND,
			foreground = self.__FOREGROUND,
			textvariable = input_value,
			border = 2,
			font = ('Segoe UI', 10),
			justify = 'left',
			relief = 'flat',
			show = '',
			highlightthickness = 2,
			highlightbackground = self.__HIGHLIGHTBACKGROUND,
			highlightcolor = self.__HIGHLIGHTCOLOR)

# Black Input
class BlackInput(tk.Entry):

	__BACKGROUND = '#000000'
	__FOREGROUND = '#ffffff'
	__HIGHLIGHTBACKGROUND = '#353635'
	__HIGHLIGHTCOLOR = '#ffffff'
	
	def __init__(self, parent, input_value):
		super().__init__(parent,
			background = self.__BACKGROUND,
			foreground = self.__FOREGROUND,
			textvariable = input_value,
			border = 2,
			font = ('Segoe UI', 10),
			justify = 'left',
			relief = 'flat',
			show = '',
			highlightthickness = 2,
			highlightbackground = self.__HIGHLIGHTBACKGROUND,
			highlightcolor = self.__HIGHLIGHTCOLOR)