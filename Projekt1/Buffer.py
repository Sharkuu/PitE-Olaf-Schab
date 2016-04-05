from Validator import Validator


class Buffer:

	'''Klasa reprezentujaca bufor - jego zadaniem jest przyjmowanie po jednej 'porcji' danych. Po ich otrzymaniu zapisuje je w liscie i 		wysyla do walidacji.
	'''
	def __init__(self):
		'''Kontruktor ustawiajacy przetrzymywane wartosci na 0 oraz ich dostepnosc na false
		'''
        	self.time = [0, False]
        	self.longitude = [0, False]
        	self.latitude = [0, False]
        	self.altitude = [0, False]
        	self.roll = [0, False]
        	self.pitch = [0, False]
        	self.heading = [0, False]
		
	
	def sendToBuffer(self,data):
		'''Funkcja zapisujaca dane oraz informacje o jej otrzymaniu
		@param data - lista danych do zapisania
		'''		
		self.time = [data[0], True]
        	self.longitude = [data[1], True]
        	self.latitude = [data[2], True]
        	self.altitude = [data[3], True]
        	self.roll = [data[4], True]
        	self.pitch = [data[5], True]
        	self.heading = [data[6], True]
	
	def isReady(self):
		'''Funkcja sprawdzajaca czy wszystkie otrzymane dane zostaly zapisane[zapisuje je do jednej listy]
		@return bool zwraca False jesli choc jedna wartosc nie zostala zapisana
		''' 
		ready = True
		all = [self.time, self.longitude, self.latitude, self.altitude, self.roll, self.pitch, self.heading]
		for ite in all:
			if (ite[1] == False):
				ready = False
				break
		return ready

	def sendData(self):
		'''Funkcja wysylajaca przechowywane dane w buforze do walidacji i ustawiajaca flagi na false'''
		if self.isReady():
			Validator.validate([self.time[0], self.longitude[0], self.latitude[0], self.altitude[0], self.roll[0], self.pitch[0], self.heading[0]])
		self.time = [0, False]
        	self.longitude = [0, False]
        	self.latitude = [0, False]
        	self.altitude = [0, False]
        	self.roll = [0, False]
        	self.pitch = [0, False]
        	self.heading = [0, False]
