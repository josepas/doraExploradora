import os




#Se crea la carpeta contenedora de todo

os.system('mkdir --mode=755 /home/invitado/Tarea3')
os.system('cp recursos/tips.txt /home/invitado/Tarea3')
os.system('cp botas.py  /home/invitado/Tarea3/')
os.system('cp quitarbotas.sh /home/invitado/Tarea3')

#Damos permisos solo de lectura y ejecucion 
os.system('chmod 555 /home/invitado/Tarea3/botas.py')
os.system('chmod 555 /home/invitado/Tarea3/tips.txt')

#Renombro archivos para que no esten a la vista 

os.system('mv /home/invitado/Tarea3/tips.txt /home/invitado/Tarea3/.tips.txt')
os.system('mv /home/invitado/Tarea3/botas.py /home/invitado/Tarea3/.botas.py')
os.system('mv /home/invitado/Tarea3/botas.py /home/invitado/Tarea3/.quitarbotas.sh')

#Se crea la mochila 

os.system('mkdir --mode=766 /home/invitado/Tarea3/mochila' ) 

#Se crea cada una de las localidades en el mundo de dora

os.system('mkdir --mode=000 /home/invitado/Tarea3/LagoDubi')
os.system('mkdir --mode=000 /home/invitado/Tarea3/ElMonteSino')
os.system('mkdir --mode=000 /home/invitado/Tarea3/DesiertoDelCharara')
os.system('mkdir --mode=000 /home/invitado/Tarea3/CuevaDelChaMAC')

print 'Se crean la mochila, localidades, Dir Raiz'

os.system('alias manpa=man')
os.system('alias botas="python botas.py"')

print 'Alias de manpa' 


