import math
import random

'''
Klasa majaca generowac dane dla funkcji sinus z wykorzystaniem podanych argumentow oraz symulowac bledy pomiarowe
'''
class DataGen:
	def __init__(self):
	        self.okresy = 2
        	self.przesuniecie = 0
        	self.dl_fali = 100
        	self.il_pomiarow = 50000
        	self.amplituda = 2
        	self.zaklucenia = 0.69
		self.pomiar_okres = int(self.il_pomiarow / self.dl_fali)


	#def getData(self):
		#return [self.okresy, self.przesuniecie, self.dl_fali, self.il_pomiarow, self.amplituda,self.zaklucenia]
 
	def getAmp(self):
		return self.amplituda
	def getOffset(self):
		return self.przesuniecie
	def getNoise(self):
		return self.zaklucenia
	def setData(self,okr,przes,dl_f,il_pom,am,zak):
		self.okresy = okr
        	self.przesuniecie = przes
        	self.dl_fali = dl_f
        	self.il_pomiarow = il_pom
        	self.amplituda = am
        	self.zaklucenia = zak
		self.pomiar_okres = int(self.il_pomiarow / self.dl_fali)

	'''
	Funkcja symulujaca wystepowanie bledow pomiarowych
	return: blad generowany pseudolosowo z podanego wczesniej zakresu
	'''
	def zakl(self):
        	return random.uniform(float(-self.zaklucenia),float(self.zaklucenia))

	'''
	FUnkcja generujaca dane
	param func: funkcja z ktorej dane maja byc generowane
	''' 
	def generateData(self, func):
		data_x = []
		data_y = []
		self.genOnePeriod(data_x)
		data_x = self.genAll(data_x)
		for x in (data_x):
			data_y.append(float(self.amplituda) * func(x+self.zakl())+self.zakl())
		data = [data_x,data_y]
		return data

	'''
	Funkcja generjaca skladowe x dla jednego okresu funkcji sin
	'''
	def genOnePeriod(self,data_x):
		for i in range(self.pomiar_okres):
			data_x.append((2.0*math.pi*float(self.dl_fali)*(float(i % self.pomiar_okres)/float(self.il_pomiarow)) + self.przesuniecie))
		
	

	'''
	Funkcja generujaca skladowe x dla funkcji sin
	param data_x: wartosci x dla 1 okresu sin
	return: wartosci x dla calego sinusa	
	'''
	def genAll(self,data_x):
		data_x_out = []
		for i in range(len(data_x)*self.okresy):			
			data_x_out.append(data_x[i % self.pomiar_okres]+(i/self.pomiar_okres)*2.0*math.pi)
		return data_x_out



