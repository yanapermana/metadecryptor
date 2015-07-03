from lib3 import *

def LSB(decimal):
	if bin(decimal)[-1:] == '1':
		return "odd"
	else:
		return "even"

def vfactor(N):
	root = int(floor(sqrt(N)))
	if LSB(root) == 'even':
		root = root - 1
	y = root
	x = root + 2
	m = x*y

	while m!=N:
		if m<N:
			x += 2
		else:
			y -= 2
		m = x*y

	return x, y

if __name__ == '__main__':
	N = 4183
	print(vfactor(N))

	'''
	(89, 47)
	'''