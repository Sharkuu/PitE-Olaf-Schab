#!/usr/bin/env python
i = 1
class InputReader:
	"""
	Klasa ktorej zadaniem jest pobieranie od uzytkownika wspolczynnikow rownania i zapisywanie ich
	:param tab: tablica do ktorej zapisywane sa odpowiednie wspolczynniki
        """
	def __init__(self,tab):
		global i
		if i%3 == 1:
			tab[0] = float(raw_input('Podaj wsp przy x rownania '))
			i = i+1
		if i%3 == 2:
			tab[1] = float(raw_input('Podaj wsp przy y rownania '))
			i = i+1
		if i%3 == 0:
			tab[2] = float(raw_input('Podaj wyraz wolny '))
			i = i+1
			
class InputValidator:
	"""
	Klasa ktorej zadaniem jest kontrola wprowadzanych danych - w razie podania wartosci nie bedacej
	liczba uzytkownik wpisuje jeszcze raz wspolczynniki
	:param tab: tablica do ktorej zapisywane sa odpowiednie wspolczynniki
	:param txt: tekst informujacy do ktorego rownania wpisujemy wspolczynniki
        """
	def __init__(self,tab,txt):
		print txt	
		try:
			InputReader(tab)
		except ValueError:			
			print 'Wystapil blad - to nie liczba'
			InputValidator(tab,txt)


class Solver:	
	"""
	Klasa ktorej zadaniem jest rozwiazanie rownania
        """
	"""
	Konstruktor wyliczajacy wyznaczniki
	:param tab1: tablica do ktorej zapisywane sa odpowiednie wspolczynniki pierwszego rownania
	:param tab2: tablica do ktorej zapisywane sa odpowiednie wspolczynniki 2 rownania
	:param out: tablica w ktorej bedzie zapisany wynik
        """
	def __init__(self,tab1,tab2,out):
	
		wg = tab1[0]*tab2[1] - tab1[1]*tab2[0]
		wx = tab1[2]*tab2[1] - tab1[1]*tab2[2]
		wy = tab1[0]*tab2[2] - tab1[2]*tab2[0]
		self.solve(wg,wx,wy,out)


	"""
	Funkcja rozwiazujaca uklad rownan
	:param wg: wyznacznik glowny rownania
	:param wx: wyznacznik x rownania
	:param wy: wyznacznik y rownania
	:param out: tablica w ktorej bedzie zapisany wynik
        """
	def solve(self,wg,wx,wy,out):
		if wg == 0.0 and wx == 0.0 and wy == 0.0:
			print 'Uklad rownan nieoznaczony(nieskonczenie wiele rozwiazan)'
			return 0 
		if wg == 0.0 and wx != 0.0 and wy != 0.0:
			print 'Uklad rownan sprzeczny'
			return 0 
		x = float(wx/wg)
		y = float(wy/wg)
		out = [x,y]
		print 'Rozwiazaniem ukladu jest para liczb x,y '+ str(out)


class ApplicationMgr:
	"""
	Klasa ktorej zadaniem jest kontrola wprowadzanych danych - w razie podania wartosci nie bedacej
	liczba uzytkownik wpisuje jeszcze raz wspolczynniki
	:param tab: tablica do ktorej zapisywane sa odpowiednie wspolczynniki
	:param txt: tekst informujacy do ktorego rownania wpisujemy wspolczynniki
        """
	tab1 = [0,0,0]
	tab2 = [0,0,0]
	out = [0,0]
	def __init__(self):
		
		InputValidator(self.tab1,'Rownanie 1 ')
		InputValidator(self.tab2,'Rownanie 2 ')
		Solver(self.tab1,self.tab2,self.out)
		

ApplicationMgr()
