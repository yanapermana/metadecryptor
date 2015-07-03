from lib3 import *

def euler_phi_asc(n):
	amount = 0
	for k in range(1, n+1, 1):
		if gcd(n, k) == 1:
			amount += 1
	return amount

def euler_phi_desc(n):
	amount = 0
	for k in range(n, 0, -1):
		if gcd(n, k) == 1:
	            amount += 1
	return amount

def euler(N, et):
	p = ((N-et+1)-(sqrt((N-et+1)**2 - 4*et)))/(2)
	p = next(primes_above(int(p)))
	return p, int(N/p)

if __name__ == '__main__':
	N = 4183
	print('euler_phi (p, q):', euler(N, euler_phi_desc(N)))

	'''
	euler_phi (p, q): (47, 89)
	python3 euler3.py  0,07s user 0,00s system 98% cpu 0,079 total
	'''