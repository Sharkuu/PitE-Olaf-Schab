class DataLoader:	
	@staticmethod
	def read(name):
		data = []       
		try:

			num_lines = sum(1 for line in open(name))
			file =  open(name, 'rb')
			for line in file:
				#line = line.split('\n')
				line = line[:-1]
				line = line.split(',')
				data.append(line)			
            
		except:
			print "ERROR"
		return data
