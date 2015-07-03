from pollard_rho3 import *
from euler3 import *
from fermat3 import *
from trial_division3 import *
from vfactor3 import *
from dasilva3 import *

class Factor3:
	def __init__(self):
		pass

	def pollard_rhos(self, N):
		return pollard_rho(N)

	def eulers(self, N):
		return euler(N, euler_phi_desc(N))

	def fermats(self, N):
		return fermat(N)

	def trials(self, N):
		return trial_division(N)

	def vfactors(self, N):
		return vfactor(N)

	def dasilvas(self, N):
		return dasilva(N)