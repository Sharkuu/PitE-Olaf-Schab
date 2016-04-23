import numpy as np

'''
Klasa posiadajaca statyczne metody wykonujace test chi2 oraz normalizujace chi2
'''
class StatAnalyser:
	@staticmethod
	def chi2(o, e):
		chi = 0.
		for i in range(len(o)):
			chi =chi +((o[i] -e[i])/np.std(e))**2
	
        	return chi
	@staticmethod
	def chi2Norm(chi, o, swoboda = 1):
		return float(chi)/float(len(o)-swoboda)

