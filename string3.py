from gather3 import *

class String3:
	def __init__(self):
		pass

	def digits(self, filename):
		print(gather_digit(filename))

	def lowers(self, filename):
		print(gather_lower(filename))

	def uppers(self, filename):
		print(gather_upper(filename))

	def upperdigits(self, filename):
		print(gather_upper_digit(filename))

	def lowerdigits(self, filename):
		print(gather_lower_digit(filename))