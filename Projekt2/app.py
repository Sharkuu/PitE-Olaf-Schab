from DataGen import DataGen
from Plotter import Plotter
from Fitter import Fitter
from StatAnalyser import StatAnalyser
import math

def sin(x, amplituda):
	data = []
	for i in x:
		data.append(amplituda*math.sin(i))
	return data
d = DataGen()
print '****************************Funkcja sinus*****************************'

while True:
	std = raw_input('Aby uruchomic program z danymi domyslnymi nacisnij 1\nJesli chcesz wprowadzic wlasne dane nacisnij ENTER \n')
	if ( std == ''):
		try:
			okr = int(raw_input("Wprowadz ilosc okresow funkcji sin(PELNE OKRESY) \n"))
    			pom_okr = float(raw_input("Wprowadz ilosc przeprowadzonych pomiarow \n"))
    			dl_f = float(raw_input("Wprowadz dlugosc fali \n"))
			if (pom_okr<dl_f):
				raise ValueError 
    			zak = float(raw_input("Wprowadz wartosc zaklocen\n"))
    			am = float(raw_input("Wprowadz amplitude\n"))
    			przes = float(raw_input("Wprowadz przesuniecie\n"))
			d.setData(okr,przes,dl_f,pom_okr,am,zak)
			break
		except ValueError:
			print 'Wprowadzono niepoprawne dane - sprobuj jeszcze raz \n'
	elif(std== str(1)):
			break
	


if (d.getNoise()>=2.5):
	print 'Uwaga! Wybrano wartosc zaklocen: '+ str(d.getNoise())	+'. Moze to spowodowac bledy rozwiazania'
#storage  = d.getData()
data = d.generateData(math.sin)
f = Fitter()
fit_data = f.fit(sin, data,[1])
fit = [data[0], fit_data]
chi = StatAnalyser.chi2(data[1], fit_data)
chi_norm = StatAnalyser.chi2Norm(chi, data[1])
print 'Test Pearsona (chi^2) = '+ str(chi) + ' wartosc chi2 znormalizowana: '+str(chi_norm)

plot = Plotter()
plot.make_plot(data)
plot.make_plot([data[0],sin(data[0],d.getAmp())], 'fun')
plot.make_plot(fit,'fit')
plot.draw_plot()


print '**********************************************************************'


