def alphabet_to_number(word):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	number = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26'
	array_alphabet = list(alphabet)
	array_number = number.split(' ')
	converted_word = []
	for letter in word:
		for n in range(0, len(array_number), 1):
			if letter == array_alphabet[n]:
				converted_word.append(array_number[n])
				converted_word.append(' ')
	del converted_word[-1]
	return ''.join(converted_word)

def number_to_alphabet(numbers):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	number = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26'
	array_number = number.split(' ')
	array_alphabet = list(alphabet)
	numbers = numbers.split(' ')
	converted_numbers = []
	for num in numbers:
		for n in range(0, len(array_alphabet), 1):
			if int(num) > 26:
				num = str(int(num) - 26)
			else:
				if num == array_number[n]:
					converted_numbers.append(array_alphabet[n])
					converted_numbers.append(' ')
	del converted_numbers[-1]
	return ''.join(converted_numbers)

if __name__ == '__main__':
	# define var
	plaintext = 'math'
	# test alphabet to number	
	print(alphabet_to_number(plaintext))
	# test number to alphabet
	plaintext_number = '13 1 20 8'
	print(number_to_alphabet(plaintext_number))