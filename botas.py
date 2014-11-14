
import sys
import os

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
        print preg[1]
        conseguido = True

if not conseguido : 
    print "No tengo consejos para esta pregunta" 


os.system('chmod 000 botas.py')

os.system('echo botas se fue por tu preguntadera')

os.system('./quitarbotas.sh &') 

