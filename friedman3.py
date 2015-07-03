# Author: Yana Permana

def friedman_test(cipher):
	cipher, letter, my_list, total_char = cipher.lower(), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], [], len(cipher)

	for i in range(26):
		x = 0
		for y in cipher:
			if y == letter[i]:
				x += 1
		my_list.append(x)

	n, i, j, sigma, sigmas, temp = len(my_list), 0, 0, 0, 0, ''

	for i in range(n, 0, -1):
		for j in range(0, n - 1, 1):
			if my_list[j] < my_list[j + 1]:
				temp = my_list[j]
				my_list[j] = my_list[j + 1]
				my_list[j + 1] = temp
				temp_letter = letter[j]
				letter[j] = letter[j + 1]
				letter[j + 1] = temp_letter
			
	print('Statistics:')
	print('i \tn \tn-1 \tn(n-1)')
	for i in range(0, n, 1):
		sigma += int(my_list[i])
		n_ = int(my_list[i]) - 1
		subs = n_ * int(my_list[i])
		sigmas += subs
		print(letter[i], ' \t', my_list[i], ' \t', n_ , ' \t', subs)
		

	print(' \t', sigma, ' \t', ' \t', sigmas)

	sigma = float(sigma)
	divisor = float((sigma)*(sigma-1))
	sigmas = float(sigmas)

	print('\nTotal character:', total_char)

	F = float(sigmas / divisor)
	print('F:', F)

	if F > 0.0385 and F < 0.065:
		print('Type: Poly-Alphabetical')
	else:
		print('Type: Mono-Alphabetical')

	I = (0.027 * sigma) / ( ((sigma-1) * F) - ((0.038 * sigma) + 0.065) )

	print('Key Length:', I,'~',round(I))
	key_length = round(I)
	
	if key_length == 5:
		print("Uses Kasiski Method")

if __name__ == '__main__':
	cipher = """qp tbtw, ixn sgjrgatvlt jwon lumi ftmc snfu, csh cuii gtkwb azoowaz... yws abkcp nca..."""
	friedman_test(cipher)