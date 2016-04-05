class Save:
	'''Klasa odpowiedzialna za zapis otrzymanych danych do pliku o nazwie 'data.txt'
	'''
	@staticmethod
	def save(data):
		sfile = open ('data.txt', 'a')
		sfile.write(data[0] + ',' + data[1] + ',' + data[2] + ',' + data[3] + ',' + data[4] + ',' + data[5] + ',' + data[6]+'\n')
		sfile.close

	
