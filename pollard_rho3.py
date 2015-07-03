from lib3 import *

def pollard_rho(N):
	x_fixed = 2
	cycle_size = 2
	x = 2
	p = 1

	while p == 1:
		for count in range(1, cycle_size ,1):
			x = (x*x + 1) % N
			p = gcd(x - x_fixed, N)
		cycle_size *= 2
		x_fixed = x

	return p, int(N/p)
	
if __name__ == '__main__':
	N = 5352499
	print('pollard_rho (p, q):', pollard_rho(N))
	
	'''
	pollard_rho (p, q): (1237, 4327)
	python yp_factor.py  0,04s user 0,00s system 97% cpu 0,043 total
	'''