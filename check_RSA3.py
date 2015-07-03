import os, sys
from math import *
from gmpy import *

def nbit(N):
    return int(log(N, 2)) + 1 

def check_RSA(target):
	os.system('timeout 5s openssl s_client -connect %s:443 | openssl x509 -pubkey -noout > pubkey.pem' % target)
	os.system('openssl rsa -in pubkey.pem -pubin -text -modulus > pubkeyAnalyze.pem')
	os.system('cat pubkeyAnalyze.pem | grep Modulus > Moduli.txt')
	os.system('cat pubkeyAnalyze.pem | grep Exponen > Exponen.txt')
	os.system("cat Moduli.txt | sed 's/^........//' > result")
	os.system("cat Exponen.txt | awk '{print $2}' >> result")
	os.system('rm *.pem')
	os.system('rm *.txt')
	os.system("sed -i '1d' result")

	files = open('result')
	elements = []
	for line in files:
		elements.append(line.rstrip())
	files.close()

	N = int(elements[0], 16)
	e = int(elements[1])
	k_N = nbit(N)
	k_e = nbit(e)

	print('\nSite: %s' % target)
	if e > N:
		print('Status: Beware => Exponent Too Big')
	elif e < 65537:
		print('Status: Beware => Exponent Too Small')
	elif k_N < 2048:
		print('Status: Beware => Modulus Too Small')
	elif k_N > 16384:
		print('Status: Beware => Modulus Too Big')
	elif k_N == 3072 and k_e < 64:
		print('Status: Beware => Exponent must be 64 bit')
	else:
		print("Status: It's OK")

if __name__ == '__main__':
	target = sys.argv[1]
	check_RSA(target)