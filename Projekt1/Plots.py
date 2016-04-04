import matplotlib.pyplot as plt
import matplotlib as mpl



class Plots:

	def altitude_time(self, data):
		time = []
		altitude = []
		for i in data:
			time.append(i[0])
			altitude.append(i[3])
        	plt.plot(time, altitude)
        	plt.xlabel('czas (s)')
        	plt.ylabel('wysokosc (m n.p.m)')
        	plt.title('Zmiany wysokosci')
        	plt.grid(True)
            	plt.show()
        	plt.close()

