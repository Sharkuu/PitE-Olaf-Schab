import csv

class ReadCSV:	
	@staticmethod
	def read(name):
		       
		try:
			file =  open(name, 'rb')
			data = csv.reader(file, delimiter=',')
            		
		except:
			print "ERROR"
		return data
			
		
      
