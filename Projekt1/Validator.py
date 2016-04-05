from Save import Save

class Validator:
	'''Klasa odpowiedzialna za sprawdzanie czy wprowadzane dane sa poprawne /niestety sprawdzane jest tylko czy sa one liczbami/
	'''
	@staticmethod
	def validate(data):
		'''Statyczna funkcja walidujaca sprawdzajaca j.w. Jesli walidacja danych przebega pomyslnie sa one przekazywane do metody 			klasy Save	
		@param data - lista danych
		'''		
		for i in data:
			temp_str = i.split(".")
			flag = False
			for j in temp_str:
				
				if(j.isdigit()):
					flag = True
				elif(j[0] == '-'):
					if(i[1:].isdigit()):
						flag = True
			if(flag == False):
				break
	
		if(flag == True):
			Save.save(data)
		

	
