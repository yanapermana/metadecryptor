from caesar3 import *
from pediaphone3 import *
from bacon3 import *
from morse3 import *
from transpose3 import *
from affine3 import *
from vigenere3 import *
from friedman3 import *
from reverse3 import *

class Classic3:
	def __init__(self):
		pass

	def reverses(self, cipher):
		print(reverse(cipher))

	def caesar(self, cipher):
		breakCaesar(cipher)

	def pediaphone(self, cipher):
		print(decryptPediaphone(cipher))

	def bacon(self, cipher):
		decryptBacon(cipher)

	def morse(self, cipher):
		print(decryptMorse(cipher))

	def transpose(self, cipher):
		breakTranspose(cipher)

	def affine(self, cipher):
		breakAffine(cipher)

	def vigenere(self, cipher):
		breakVigenere(cipher)

	def friedman(self, cipher):
		friedman_test(cipher)
