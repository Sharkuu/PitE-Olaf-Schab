from ReadCSV import ReadCSV
from Buffer import Buffer
from DataLoader import DataLoader
from Fixer import Fixer
from Plots import Plots
import os

if os.path.exists('data.txt'):
    os.remove('data.txt')
upload_data = []
data = []
line = 1
rfile = ReadCSV.read('test.csv')
for row in rfile:
			if(line == 1):
				line = line+1
				continue
			upload_data.append(row)

Fixer.fixTimeAndAlt(upload_data)
buff = Buffer()
for i in upload_data:
	buff.sendToBuffer(i)
	buff.sendData()

data = (DataLoader.read('data.txt'))
plots = Plots()
plots.altitude(data)
plots.pitch(data)
plots.distance(data)
plots.speed(data)
plots.roll(data)
