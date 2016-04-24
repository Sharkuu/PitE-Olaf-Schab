import math
import random

'''
Klasa majaca generowac dane dla funkcji sinus z wykorzystaniem podanych argumentow oraz symulowac bledy pomiarowe
'''
class DataGen:
	def __init__(self):
        	self.przesuniecie = 0
        	self.okres = 4
        	self.il_pomiarow = 3000
        	self.amplituda = 2
        	self.zaklocenia = 0.69
		self.pomiar_okres = int(self.il_pomiarow / self.okres)
		


	#def getData(self):
		#return [self.okresy, self.przesuniecie, self.okres, self.il_pomiarow, self.amplituda,self.zaklocenia]
 
	def getAmp(self):
		return self.amplituda
	def getOffset(self):
		return self.przesuniecie
	def getNoise(self):
		return self.zaklocenia
	def setData(self,przes,okr,il_pom,am,zak):
		
        	self.przesuniecie = przes
        	self.okres = okr
        	self.il_pomiarow = il_pom
        	self.amplituda = am
        	self.zaklocenia = zak
		self.pomiar_okres = int(self.il_pomiarow / self.okres)
		

	'''
	Funkcja symulujaca wystepowanie bledow pomiarowych
	return: blad generowany pseudolosowo z podanego wczesniej zakresu
	'''
	def zakl(self):
        	return random.uniform(float(-self.zaklocenia),float(self.zaklocenia))

	'''
	FUnkcja generujaca dane
	param func: funkcja z ktorej dane maja byc generowane
	''' 
	def generateData(self, func):
		data_x = []
		data_y = []
		self.genX(data_x)
		
		for x in (data_x):
			data_y.append(float(self.amplituda) * func(x+self.zakl())+self.zakl())
		data = [data_x,data_y]
		return data

	'''
	Funkcja generjaca skladowe x funkcji sin
	'''
	def genX(self,data_x):
		for i in range(self.pomiar_okres*self.okres):
			data_x.append((2.0*math.pi*float(self.okres)*(float(i)/float(self.il_pomiarow)) + self.przesuniecie))
		
	

	


