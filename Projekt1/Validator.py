from Save import Save

class Validator:
	@staticmethod
	def validate(data):
		
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
		

	
