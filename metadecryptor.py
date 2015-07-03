import os, sys

from encoding3 import *
from classic3 import *
from factor3 import *
from string3 import *
from modern3 import *
from converter3 import *

encoding = Encoding3()
classic = Classic3()
factor = Factor3()
string = String3()
modern = Modern3()
converter = Converter3()

def greeting():
	print("""
             _            _                            _             
  /\/\   ___| |_ __ _  __| | ___  ___ _ __ _   _ _ __ | |_ ___  _ __  v1.0
 /    \ / _ \ __/ _` |/ _` |/ _ \/ __| '__| | | | '_ \| __/ _ \| '__|
/ /\/\ \  __/ || (_| | (_| |  __/ (__| |  | |_| | |_) | || (_) | |   
\/    \/\___|\__\__,_|\__,_|\___|\___|_|   \__, | .__/ \__\___/|_|   
                                           |___/|_|                  
                                           """)

def author():
	print("""\nby Yana Permana @yansen1204 <kumpoter@gmail.com>\n""")	

def helps():
	print("""Core Commands
=============

\tCommand\t\tDescription
\t-------\t\t-----------
\t-h\t\tHelp
\t-author\t\tAuthor
\t-credit\t\tCredits
\t-hex\t\tDecode hexadecimal
\t-b64\t\tDecode base64
\t-caesar\t\tBreak caesar cipher
\t-vigenere\tBreak vigenere cipher
\t-affine\t\tBreak affine cipher
\t-reverse\tDecrypt reverse cipher
\t-bacon\t\tDecrypt bacon cipher
\t-morse\t\tDecrypt morse cipher
\t-pediaphone\tDecrypt pediaphone cipher
\t-transpose\tDecrypt transpose cipher
\t-friedman\tIs monoalpabetical or polyalphabetical?

Factoring Modulus
==================

\tCommand\t\tDescription
\t-------\t\t-----------
\t-prho\t\tPollard rho
\t-euler\t\tEuler
\t-fermat\t\tFermat
\t-trial\t\tTrial division
\t-vfactor\tV Factor
\t-dasilva\tDa Silva

Strings
==================

\tCommand\t\tDescription
\t-------\t\t-----------
\t-digit\t\tGather Digit 
\t-lower\t\tGather Lowercase
\t-upper\t\tGather Uppercase
\t-upperdigit\tGather Uppercase and Digit
\t-lowerdigit\tGather Lowercase and Digit

Modern
==================

\tCommand\t\tDescription
\t-------\t\t-----------
\t-checkRSA\tIs your RSA is secure?

Converter 
==================

\tCommand\t\tDescription
\t-------\t\t-----------
\t-alpha2num\tConvert alphabet to number
\t-num2alpha\tConvert number to alphabet
""");

def credit():
	print("""
Thanks to 
=============

\tNo.\t\tName
\t-------\t\t-----------
\t1\t\tAl Sweigart
\t2\t\tSteven D'Aprano
\t3\t\tRidwan Fajar S.
""");

def main():
	greeting()
	try:
		if sys.argv[1] == '-h':
			helps()
		elif sys.argv[1] == '-author':
			author()
		elif sys.argv[1] == '-credit':
			credit()
		elif sys.argv[1] == '-b64':
			if sys.argv[2] != '':
				print(encoding.b642asc(sys.argv[2]))
		elif sys.argv[1] == '-hex':
			if sys.argv[2] != '':
				print(encoding.hex2asc(sys.argv[2]))
		elif sys.argv[1] == '-caesar':
			if sys.argv[2] != '':
				classic.caesar(sys.argv[2])
		elif sys.argv[1] == '-pediaphone':
			if sys.argv[2] != '':
				classic.pediaphone(sys.argv[2])
		elif sys.argv[1] == '-reverse':
			if sys.argv[2] != '':
				classic.reverses(sys.argv[2])
		elif sys.argv[1] == '-bacon':
			if sys.argv[2] != '':
				classic.bacon(sys.argv[2])
		elif sys.argv[1] == '-morse':
			if sys.argv[2] != '':
				classic.morse(sys.argv[2])
		elif sys.argv[1] == '-transpose':
			if sys.argv[2] != '':
				classic.transpose(sys.argv[2])
		elif sys.argv[1] == '-affine':
			if sys.argv[2] != '':
				classic.affine(sys.argv[2])
		elif sys.argv[1] == '-vigenere':
			if sys.argv[2] != '':
				classic.vigenere(sys.argv[2])
		elif sys.argv[1] == '-friedman':
			if sys.argv[2] != '':
				classic.friedman(sys.argv[2])
		elif sys.argv[1] == '-prho':
			if sys.argv[2] != '':
				print('(p, q):', factor.pollard_rhos(int(sys.argv[2])))
		elif sys.argv[1] == '-euler':
			if sys.argv[2] != '':
				print('(p, q):', factor.eulers(int(sys.argv[2])))
		elif sys.argv[1] == '-fermat':
			if sys.argv[2] != '':
				print('(p, q):', factor.fermats(int(sys.argv[2])))
		elif sys.argv[1] == '-trial':
			if sys.argv[2] != '':
				print('(p, q):', factor.trials(int(sys.argv[2])))
		elif sys.argv[1] == '-vfactor':
			if sys.argv[2] != '':
				print('(p, q):', factor.vfactors(int(sys.argv[2])))
		elif sys.argv[1] == '-dasilva':
			if sys.argv[2] != '':
				print('(p, q):', factor.dasilvas(int(sys.argv[2])))
		elif sys.argv[1] == '-digit':
			if sys.argv[2] != '':
				string.digits(sys.argv[2])
		elif sys.argv[1] == '-lower':
			if sys.argv[2] != '':
				string.lowers(sys.argv[2])
		elif sys.argv[1] == '-upper':
			if sys.argv[2] != '':
				string.uppers(sys.argv[2])
		elif sys.argv[1] == '-upperdigit':
			if sys.argv[2] != '':
				string.upperdigits(sys.argv[2])
		elif sys.argv[1] == '-lowerdigit':
			if sys.argv[2] != '':
				string.lowerdigits(sys.argv[2])
		elif sys.argv[1] == '-checkRSA':
			if sys.argv[2] != '':
				modern.check_RSAs(sys.argv[2])
		elif sys.argv[1] == '-alpha2num':
			if sys.argv[2] != '':
				converter.alphabet_to_numbers(sys.argv[2])
		elif sys.argv[1] == '-num2alpha':
			if sys.argv[2] != '':
				converter.number_to_alphabets(sys.argv[2])
		else:
			helps()
	except:
		helps()

if __name__ == '__main__':
	main()
