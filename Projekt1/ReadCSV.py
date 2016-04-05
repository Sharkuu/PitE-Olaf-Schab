import csv

class ReadCSV:	
	'''Klasa sluzaca do odczytywania danych wprowadzanych  z pliku csv'''
	@staticmethod
	def read(name):
		'''Statyczna funkcja sluzaca do odczytywanie plikow csv o podanej nazwie
		@param name - nazwa pliku
		@return dane zapisane w pliku
		'''
		       
		try:
			file =  open(name, 'rb')
			data = csv.reader(file, delimiter=',')
            		
		except:
			print "ERROR"
		return data
			
		
      
