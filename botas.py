
import sys
import os
import signal
import time

def receive_signal(signum, stack):
    print '-----> No puedes matar a boticas tontito :) \n'
 

usage = " Es necesario darle un solo argumento a botas, y debe ser "
usage += "del estilo :\n [1-4].[1-9]  \n"


if (len(sys.argv) == 2 ):
    npreg =sys.argv[1]
else:
    print usage 
    exit(1)



f = open('tips.txt','r') 

    
conseguido = False

for line in f:    
    preg =line.split()
    if (preg[0] == npreg) :  
        print "Consejo: \n"
        print preg[1]
        print "\n"
        conseguido = True


if not conseguido : 
        print "No tengo consejos para esta pregunta \n\n" 
    
print "botas se fue por tu preguntadera \n"

signal.signal(signal.SIGINT, receive_signal)
signal.signal(signal.SIGQUIT, receive_signal)

suficiente = 0
while (suficiente < 300 ) :
    print 'Paseando...'
    time.sleep(2)
    suficiente += 2




