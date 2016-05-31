#!/usr/bin/env python3.4
from math import acos
from math import sin
from math import pi
import sys

#Klasa odpowiedzialna za wczytywanie danych:
# - zakres poszukiwan liczby pierwszej
# - wysokosc trojkata pascala
class InputReader:
	def __init__(self):
		self.primal = None
		self.triangle = None

	def Initiate(self):
		a,b = None, None
		print('Program wczytuje tylko liczby naturalne wieksze lub rowne 1 !')
		print('----------------')
		while self.CheckIfIsInt(a):
			a = input('Podaj zakres szukania liczb pierwszych \n')

		while self.CheckIfIsInt(b):
			b = input('Podaj wysokosc trojkata pascala a \n')

		self.primal = int(a)
		self.triangle = int(b)

	#Funkcja sprawdzajaca, czy wprowadzana wartosc jest intem oraz czy nie jest mniejsza od 1
	def CheckIfIsInt(self,value):
		if value is None:
			return 1
		else:
			try:
				val = int(value)
				if int(value) < 1:
					print("Podana liczba musi byc wieksza lub rowna 1")
					return 1
			except ValueError:
				print("Wprowadzona wartosc nie jest liczba naturalna. Sprobuj jeszcze raz.")
				return 1
		return 0

	def returnValue(self,value):
		if value == 1:
			return self.primal
		if value == 2:
			return self.triangle
		else:
			print('Blad aplikacji')
			sys.exit(0)
			return 0

# Wypisuje liczby pierwsze z danego zakresu
class Primary:
	def __init__(self,number):
		self.x=1
		self.number = number;

	def isPrime(self,n):
		return n > 1 and all(n%i for i in range(2,n))

	def __iter__(self):
		return self

	def __next__(self):
		self.x+=1
		while(self.isPrime(self.x)==False):
			self.x+=1
		if self.x > self.number:
			raise StopIteration
		return self.x

#Wypisuje trojkat pascala dla zadanej ilosci rzędow
class Pascal_Triangle:
	def __init__(self,rows):
		self.row=[1.0]
		self.n=0
		self.rows = rows

	def __iter__(self):
		return self

	def __next__(self):
		line = [1.0]
		for k in range(self.n):
			line.append(line[k] * (self.n-k) / (k+1))
		self.n+=1
		if self.n>self.rows:
			raise StopIteration
		return line


#Zwraca losowe liczby od 0 do 1
class montecarlo:
	def __init__(self):
		self.a=44485709377909
		self.m=2**48
		self.c = 0
		self.x=1
		self.n=0.0

	def __iter__(self):
		return self

	def __next__(self):
		self.x=(self.a * self.x + self.c)%self.m
		self.n+=1
		return self.x/self.m


#Obliczanie całki metodą montecarlo
class monte_use:
	def __init__(self):
			TOL = 1e-7
			c=0
			n=1
			mc = montecarlo()

			integra=100
			while abs(2-integra) > TOL:
				x = next(mc)*pi
				y = next(mc)
				if 0<y<=self.func(x):
					c+=1
				if 0>y>=self.func(x):
					c-=1
				integra = pi*(c/n)
				n+=1
			print('\nWynik obliczania calki')
			print(integra)
			print('\nIlosc iteracji, potrzebnych do obliczenia')
			print(n)

	#Funkcja, ktora obliczamy
	def func(self,x):
		return sin(x)

# Klasa wywolujaca poszczegolne zadania
class Manager:
	def __init__(self):
		inputt = InputReader()
		try:
			inputt.Initiate()

		except KeyboardInterrupt:
			print('\nAplikacja zatrzymana przez uzytkownika')
			sys.exit(0)

		print('ZADANIE 1')
		it1 = Primary(inputt.returnValue(1))

		print ('Liczby pierwsze z zadanego zakresu:')

		for i in it1:
			print(i)
		print ('--------------')

		print('ZADANIE 2')
		print('Trojkat pascala:')
		pas = Pascal_Triangle(inputt.returnValue(2))
		for i in pas:
			print(i)
		print ('--------------')

		print('ZADANIE 3')
		print('Monte Carlo:')
		monte_use()

Manager()
