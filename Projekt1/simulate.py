import time
import math
#Airbus A380
angle = 12.5
class Simulate:
    @staticmethod
    def fly(plane):
        global angle
        fopen = open('results.txt','w')
        isFlying = True
        while isFlying:
            #START
            print 'Samolot nabiera predkosci'
            while plane.velocity<200.0:
                plane.velocity = plane.velocity + 1.4*(time.time()-plane.start)
                print 'h ' + str(plane.height)+ ' vel '+str(plane.velocity) +' slope '+str(plane.slope)+'    '+ str(time.time()-plane.start)
                fopen.write(str(plane.height)+ ' '+str(plane.velocity) +' '+str(plane.slope)+' '+ str(time.time()-plane.start)+'\n')
                time.sleep(1)
            plane.started = True
            print 'Samolot wzbija sie w powietrze'
            plane.startFly = time.time()
            #WZNOSZENIE I LOT
            while plane.height< 10000.0:
                if plane.velocity<plane.max_velocity:
                    plane.velocity = plane.velocity + 1.4*(time.time()-plane.startFly) 
                if angle>plane.slope and plane.height <5000.0:
                    plane.slope +=0.1                    
                if plane.height >5000.0:
                    plane.slope -=0.2
                    if plane.slope <=0.0:
                        plane.slope = 0
                #plane.height = plane.height + plane.velocity*(time.time()-plane.start)*math.sin(math.radians(plane.slope))- (1/2)*(9.81*math.pow(time.time()-plane.start,2))
                plane.height = plane.height + plane.velocity*math.sin(math.radians(plane.slope))
                print 'h ' + str(plane.height)+ ' vel '+str(plane.velocity) +' slope '+str(plane.slope)+'    '+ str(time.time()-plane.start)
                fopen.write(str(plane.height)+ ' '+str(plane.velocity) +' '+str(plane.slope)+' '+ str(time.time()-plane.start)+'\n')
                time.sleep(1)
                if (plane.slope == 0):
                    if (time.time()-plane.start)>160.0:
                        break
            print 'Samolot podchodzi do ladowania'
            plane.startLand= time.time()
            #LADOWANIE
            while plane.velocity>1.0:
                if plane.velocity>500.0 and plane.height>1000.0:
                    plane.velocity = plane.velocity + (-0.03)*(time.time()-plane.startLand)
                if plane.velocity>300.0 and plane.height>400.0 and plane.velocity<500.0 and plane.height<1000.0:
                    plane.velocity = plane.velocity + (-0.05)*(time.time()-plane.startLand)
                #if plane.velocity > 350.0 and plane.velocity<450.0 and plane.height>500:
                #    plane.velocity = plane.velocity + (-0.2)*(time.time()-plane.startLand)
                if plane.height>0:
                    plane.height = plane.height - plane.velocity*math.sin(math.radians(2))
                #plane.height = plane.height - (1/2)*(9.81*math.pow(time.time()-plane.start,2))
                if plane.height<0:
                    plane.height = 0
                    #plane.slope = 0
                if plane.height == 0:
                    plane.velocity = plane.velocity - 0.2*(time.time()-plane.startLand)
                    isFlying = False
                if plane.velocity<0.0:
                    plane.velocity = 0
                print 'h ' + str(plane.height)+ ' vel '+str(plane.velocity) +' slope '+str(plane.slope)+'    '+ str(time.time()-plane.start)
                fopen.write(str(plane.height)+ ' '+str(plane.velocity) +' '+str(plane.slope)+' '+ str(time.time()-plane.start)+'\n')
                time.sleep(1)
                
            
            print 'Samolot wyladowal'
            #print 'h ' + str(plane.height)+ ' vel '+str(plane.velocity) +' slope '+str(plane.slope)+'    '+ str(time.time()-plane.start)
            #fopen.write(str(plane.height)+ ' '+str(plane.velocity) +' '+str(plane.slope)+' '+ str(time.time()-plane.start)+'\n')
            
            fopen.close()

