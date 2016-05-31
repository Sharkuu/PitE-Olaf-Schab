import unittest
from zadanie import *


class TestClass(unittest.TestCase):
    def setUp(self):
        self.reader = InputReader()
        self.prime = Primary(10)
        self.pascal = Pascal_Triangle(8)
        self.montecarlo = montecarlo()
        self.monte_use = monte_use()

##################################################################################################################
    def test_inputFloat(self):
        self.assertFalse(self.reader.CheckIfIsInt(7.0))
    
    #sys.exit powienien byc w innym miejscu, lub nie powinen byc wcale
    def test_inputReturnVal(self):
        self.assertFalse(self.reader.returnValue(7.0))

    def test_inputReturnValTriangle(self):
        self.assertEqual(self.reader.triangle,self.reader.returnValue(2))

    def test_inputReturnValPrimal(self):
        self.assertEqual(self.reader.primal,self.reader.returnValue(1))
###################################################################################################################
    def test_prime(self):
        self.assertEqual(10, self.prime.number)

    def test_primeIsPrime(self):
        self.assertEqual(True, self.prime.isPrime(3))

    def test_primeNext(self):
        self.assertEqual(self.prime.x+1, self.prime.__next__())
##################################################################################################################
    def test_pascalInit(self):
        self.assertEqual(8, self.pascal.rows)
    #????
    #def test_pascalNext(self):
        #self.assertEqual(, self.test_pascal_next())
##################################################################################################################
    def test_montecarloLessThan1(self):
        self.assertLessEqual(self.montecarlo.__next__(), 1.0)

    def test_montecarloGreaterThan0(self):
        self.assertGreaterEqual(self.montecarlo.__next__(), 0.0)
##################################################################################################################
    def test_monte_useFunc(self):
        self.assertEqual(sin(0.5), self.monte_use.func(0.5))

if __name__ == '__main__':
    unittest.main()
