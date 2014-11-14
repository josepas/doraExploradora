
import sys
import os
import signal
import time
import subprocess

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


if (npreg != "lohicimos") : 
    
    conseguido = False
    

    #Buscar linea  del consejo
    for line in f:    
        preg =line.split()
        if (preg[0] == npreg) :  
            print "Consejo: \n"
            s = "" 
            for string in preg[1:]:
                s +=" "+ string
            print s + "\n" 
            conseguido = True

    if not conseguido : 
        print "No tengo consejos para esta pregunta \n\n" 
    
        print "botas se fue por tu preguntadera \n"

        #Agarra la senal de ^C ^\  
        signal.signal(signal.SIGINT, receive_signal)
        signal.signal(signal.SIGQUIT, receive_signal)

        #Dormir durante 5 minutos
        suficiente = 0
        while (suficiente < 300 ) :
            print 'Paseando...'
            time.sleep(2)
            suficiente += 2
else:
    print "Blah\n"
    os.system( "bash Zorro.sh" ) 
    #subprocess.call("./Zorro.sh",shell=True) 




