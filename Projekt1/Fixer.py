from fastnumbers import fast_real

class Fixer:
	
	@staticmethod
	def fixTimeAndAlt(data):
		start_time = fast_real(data[0][0])
		
		for i in data:
			
			i[0] = fast_real(i[0]) - start_time
			i[0] = str(i[0]) 
			i[3] = fast_real(i[3])*0.3048
			i[3] = str(i[3])
