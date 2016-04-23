import matplotlib.pyplot as plt

'''
Klasa zarzadzajaca wyswietlaniem wykresow
'''

class Plotter:
	def make_plot(self, data, info = 'points'):
		if (info =='points'): 
			plt.plot(data[0], data[1],'bo', label = 'Generated data')
		elif (info == 'fit'):
			plt.plot(data[0], data[1], 'r', label = 'Fitted',linewidth=4.0, alpha = 0.8)
		elif (info == 'fun'):
			plt.plot(data[0], data[1], 'g', label = 'Original function',linewidth=4.0)
		plt.grid()
		plt.legend(loc='upper right', shadow=True)
	def draw_plot(self):
		plt.show()



