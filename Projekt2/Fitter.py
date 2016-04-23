from scipy.optimize import curve_fit
'''
Klasa fittujaca krzywa do danych
'''
class Fitter:
    
    def fit(self,func, data,par):
        params = curve_fit(func, data[0], data[1],par)
        o_data = func(data[0], *params[0])
        return o_data
