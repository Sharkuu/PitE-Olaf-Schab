import simulate
import Plane
import sys
class App:
    def __init__(self):
        print '****************Flight recorder simulator****************'
        print '* Press 1 to simulate                                   *'
        print '* Press 2 to see results                                *'
        print '* Press \'q\' to exit                                   *'
        print '*********************************************************'
        while True:
            self.check(inp = raw_input())
    def check(self,inp):
        if inp == 'q':
            sys.exit()
        if inp == str(1):
            simulate.Simulate.fly(plane = Plane.Plane())
        
            
App()
            

