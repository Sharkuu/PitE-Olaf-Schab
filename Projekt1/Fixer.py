from fastnumbers import fast_real
from fastnumbers import fast_float
import numpy as np
import math
class Fixer:
	'''Klasa odpowiedzialna za przeliczenia oraz odpowiednim ustawieniu niektorych danych
	'''
	@staticmethod
	def fixTimeAndAlt(data):
		'''Statyczna funkcja majaca na celu zamiane dlugosci wyrazonej w stopach na metry oraz ustawienie, aby czas liczony byl od 0s
		@param data - lista danych
		'''
		start_time = fast_real(data[0][0])
		
		for i in data:
			
			i[0] = fast_real(i[0]) - start_time
			i[0] = str(i[0]) 
			i[3] = fast_real(i[3])*0.3048
			i[3] = str(i[3])

	@staticmethod
	def fixDistance(data):
		'''Funkcja statyczna obliczajaca przebyty dystans na podstawie szerokosci i wysokosci geografizcnej
		@param data - lista danych
		@return dist - lista zawierajaca przebyty dystans 
		'''
		start_Lo = fast_real(data[0][1])
		start_La = fast_real(data[0][2])
		dist = []

		for i in data:
			dist.append(math.sqrt(math.pow(math.cos((math.pi*start_La)/180.0)*(fast_real(i[1])-start_Lo),2)+math.pow((fast_real(i[2])-start_La),2))*math.pi*(12756.274/360)*1000)
		return dist

	@staticmethod
	def prepareSpeed(data):
		'''Statyczna funkcja obliczajaca predkosc samolotu w danym czasie
		@param data - lista danch
		@result speed - lista zawierajaca predkosci
		'''
		dst = Fixer.fixDistance(data)
		speed = []
		s = fast_real(dst[0])
		for i in dst:
			dist = fast_real(i)-s
			speed.append(dist*3.6)
			s = i
		return speed

	
	
