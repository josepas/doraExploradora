import sys
import os
import random
from random import randint
from random import choice

# Obtengo en crap palabras random
f = open('/etc/dictionaries-common/words','r') 
crap = f.readlines()
f.close()

random.shuffle(crap)

# Crea la ruta y le mete n archivos y n carpetas
def DirBasura(ruta, n):
	if not os.path.exists(ruta):
		os.mkdir(ruta)

	for i in range(int(n)):
		os.mkdir(ruta + '/' + crap.pop().strip() )
		archivo = open(ruta + '/' + crap.pop().strip() , 'w', 0) 

# Crea archivo con N lineas basura
def CrearArchivo(ruta, n):
	archivo = open(ruta, 'w', 0) 
	for i in range(int(n)):
		archivo.write(crap.pop().strip() + '\n')

DirBasura("Doraland", 0)

#####     Lago Dubi      #####

# Creo el dir Lago Dubi
DirBasura("Doraland/LagoDubi", 300)
sitio1 = "Doraland/LagoDubi"

# Pregunta 1.1
pass

# Pregunta 1.2
CrearArchivo("Doraland/LagoDubi/barco", 30)
os.system("cp Doraland/LagoDubi/barco Doraland/LagoDubi/plano_barco")
os.system('echo "fisura en el casco" >> Doraland/LagoDubi/barco')


# Pregunta 1.3 y 1.5

DirBasura("Doraland/LagoDubi/superficie", 10)
DirBasura("Doraland/LagoDubi/superficie/fondo", 100)
DirBasura("Doraland/LagoDubi/superficie/fondo/MAS_AL_FONDO", 10)

# Pregunta 1.4
pass

# Pregunta 1.6
pass

# Pregunta 1.7

for i in range(30):
	CrearArchivo("Doraland/LagoDubi/superficie/fondo/dubdub" + crap.pop().strip() , 0)
	CrearArchivo("Doraland/LagoDubi/superficie/fondo/dubdub" + str(i*13), 0)

DirBasura("Doraland/LagoDubi/Chikundubi", 0)


#####     Monte Sino      #####

# Creo el dir Monte Sino
DirBasura("Doraland/MonteSino", 600)
site2 = "Doraland/MonteSino/"

# Pregunta 2.1
CrearArchivo(site2 + "camino", 601)
os.system('echo "N1d0P00k33" >> ' + site2 + 'camino')
for i in range(602):
	os.system('echo "' + crap.pop().strip() + '" >> Doraland/MonteSino/camino')

DirBasura(site2 + "N1d0P00k33", 200)

# Pregunta 2.2
os.system('echo "Sabias que... cantamos la cancion del zorro el dia de cumpleanos de cada preparador?" >> ' + site2 + 'N1d0P00k33/webo')
os.system('chmod 000 ' + site2 + 'N1d0P00k33/webo')

# Pregunta 2.3
DirBasura(site2 + "aqui", 0)
DirBasura(site2 + "aqui/se", 200)
DirBasura(site2 + "aqui/se/encuentra", 200)
CrearArchivo(site2 + "aqui/se/encuentra/Pookee", 0)

# Pregunta 2.4
DirBasura(site2 + "nido", 0)
for i in range(1111):
	CrearArchivo(site2 + "nido/huevo" + str(i), 0)
	if i != 744:
		os.system('echo "pookee" >> ' + site2 + 'nido/huevo' + str(i))
	else:
		os.system('echo "intruso" >> ' + site2 + 'nido/huevo' + str(i))

# Pregunta 2.5
DirBasura(site2 + "cayendo", 0)
CrearArchivo(site2 + "aqui/se/encuentra/nidoDeAvispas", 0)
for i in range(2500):
	if i != 893:
		os.system("ln -s aquiNoEsta " + site2 + "cayendo/avispa" + str(i) )
	else:
		os.system('echo "/Doraland/MonteSino/aqui/se/encuentra/nidoDeAvispas" >> ' + site2 + 'cayendo/avispa893')





































