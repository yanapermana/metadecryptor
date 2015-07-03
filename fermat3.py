from lib3 import *

def fermat(N):
	stop, a = False, int(ceil(sqrt(N)))
	while stop == False:
		bsquare = a*a - N
		if is_square(bsquare):
			b = sqrt(bsquare)
			p = a - b
			q = a + b 
			if p != 1 and p != N:
				return p, q 
				stop = True
		if a == N:
			stop = True
		a += 1

if __name__ == '__main__':
	N = 360942546576826817
	print('fermat (p, q):', fermat(N))