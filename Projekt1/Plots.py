import matplotlib.pyplot as plt
import matplotlib as mpl
from Fixer import Fixer


class Plots:
	'''Klasa budujaca wykresy
	Wszystkie metody dzialaja na tej samej zasadzie - z otrzymanych danych wybierane sa te ktore maja byc zaprezentowane na wykresie a 		nastepnie wykres jest budowany
	@param data - lista danych
	@return f - figura potrzebna do budowy wykresu w GUI
	'''
	def altitude(self, data):
		f = plt.figure()
		time = []
		altitude = []
		for i in data:
			time.append(i[0])
			altitude.append(i[3])
        	plt.plot(time, altitude)
        	plt.xlabel('czas [s]')
        	plt.ylabel('wysokosc [m n.p.m]')
        	plt.title('Zmiany wysokosci')
        	plt.grid(True)
            	#plt.show()
        	plt.close()
		return f

	def pitch(self, data):
		f = plt.figure()
		time = []
		pitch = []
		for i in data:
			time.append(i[0])
			pitch.append(i[5])
       
        	plt.plot(time, pitch)
        	plt.xlabel('time [s]')
        	plt.ylabel('kat wznoszenia')
        	plt.title('Zmiany kata wznoszenia')
        	plt.grid(True)
        	#plt.show()
        	plt.close()
		return f
	def distance(self, data):
		f = plt.figure()
		time = []
		for i in data:
			time.append(i[0])
       
		dist = Fixer.fixDistance(data)
        	plt.plot(time, dist)
        	plt.xlabel('time [s]')
        	plt.ylabel('Dystans [m]')
        	plt.title('Przebyty dystans')
        	plt.grid(True)
        	#plt.show()
        	plt.close()
		return f
	
	def speed(self, data):
		f = plt.figure()
		time = []
		for i in data:
			time.append(i[0])
       		
		speed = Fixer.prepareSpeed(data)
		plt.plot(time, speed)
        	plt.xlabel('time [s]')
        	plt.ylabel('Predkosc [km/h]')
        	plt.title('Predkosc')
        	plt.grid(True)
        	#plt.show()
        	plt.close()
		return f
	def roll(self, data):
		f = plt.figure()
		time = []
		roll = []
		for i in data:
			time.append(i[0])
			roll.append(i[4])
       		
		
		plt.plot(time, roll)
        	plt.xlabel('time [s]')
        	plt.ylabel('Przechyl boczny ')
        	plt.title('Przechyl')
        	plt.grid(True)
        	#plt.show()
        	plt.close()
		return f















     
