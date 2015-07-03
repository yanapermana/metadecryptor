import base64, binascii

class Encoding3:
	def __init__(self):
		pass

	def b642asc(self,b64):
		try:
			return (binascii.a2b_base64(b64)).decode()
		except:
			return None

	def hex2asc(self,hexa):
		try:
			return (binascii.a2b_hex(hexa)).decode()
		except:
			return None