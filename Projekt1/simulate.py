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
                #print 'h ' + str(plane.height)+ ' vel '+str(plane.velocity) +' slope '+str(plane.slope)+'    '+ str(time.time()-plane.start)
                fopen.write(str(plane.height)+ ' '+str(plane.velocity) +' '+str(plane.slope)+' '+ str(time.time()-plane.start)+'\n')
                time.sleep(1)
            plane.started = True
            print 'Samolot wzbija sie w powietrze'
            #WZNOSZENIE I LOT
            while plane.height< 10000.0:
                if plane.velocity<plane.max_velocity:
                    plane.velocity = plane.velocity + 0.5*(time.time()-plane.start)
                if angle>plane.slope and plane.height <7000.0:
                    plane.slope +=0.01
                    reached = time.time()
                if plane.height >7000.0 and plane.slope>0.0:
                    plane.slope -=0.1
                    if plane.slope <0.0:
                            plane.slope = 0.0
                plane.height = plane.height + plane.velocity*(time.time()-plane.start)*math.sin(math.radians(plane.slope))
                #print 'h ' + str(plane.height)+ ' vel '+str(plane.velocity) +' slope '+str(plane.slope)+'    '+ str(time.time()-plane.start)
                fopen.write(str(plane.height)+ ' '+str(plane.velocity) +' '+str(plane.slope)+' '+ str(time.time()-plane.start)+'\n')
                time.sleep(1)
                if (time.time()-reached)>30.0:
                    break
            print 'Samolot podchodzi do ladowania'
            #LADOWANIE
            while plane.velocity>1.0:
                if plane.velocity>350.0:
                    plane.velocity = plane.velocity + (-0.08)*(time.time()-plane.start)
                if plane.height >3000.0:
                    plane.slope -=0.01
                if plane.height <=3000.0 :
                    plane.slope +=0.01
                    if plane.slope >0:
                        plane.slope = 0
                plane.height = plane.height + plane.velocity*(time.time()-plane.start)*math.sin(math.radians(plane.slope))
                if plane.height<0:
                    plane.height = 0
                    plane.slope = 0
                if plane.height == 0:
                    plane.velocity = plane.velocity - 0.3*(time.time()-plane.start)
                if plane.velocity<0.0:
                    plane.velocity = 0
                #print 'h ' + str(plane.height)+ ' vel '+str(plane.velocity) +' slope '+str(plane.slope)+'    '+ str(time.time()-plane.start)
                fopen.write(str(plane.height)+ ' '+str(plane.velocity) +' '+str(plane.slope)+' '+ str(time.time()-plane.start)+'\n')
                time.sleep(1)
            
            print 'Samolot wyladowal'
            #print 'h ' + str(plane.height)+ ' vel '+str(plane.velocity) +' slope '+str(plane.slope)+'    '+ str(time.time()-plane.start)
            fopen.write(str(plane.height)+ ' '+str(plane.velocity) +' '+str(plane.slope)+' '+ str(time.time()-plane.start)+'\n')
            isFlying = False
            fopen.close()

