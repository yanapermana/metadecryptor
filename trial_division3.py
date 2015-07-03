from lib3 import *

def trial_division(N):
	root = int(ceil(sqrt(N)))
	stop, p = False, root
	while stop == False:
		if N % p == 0 or p < 2:
			return p, int(N/p)
			stop = True
		p -= 1

if __name__ == '__main__':
	N = 80780754611
	trial_division(N)
	print('trial_division (p, q):', trial_division(N))

	'''
	trial_division (p, q): (123457, 654323)
	'''