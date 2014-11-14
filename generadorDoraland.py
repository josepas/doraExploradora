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

def CrearArchivoContenido(ruta, contenido):
    archivo = open(ruta, 'w', 0)
    archivo.write(texto)

DirBasura("Doraland", 0)

#####     Lago Dubi      #####

# Creo el dir Lago Dubi
DirBasura("Doraland/LagoDubi", 0)
sitio1 = "Doraland/LagoDubi"

# Pregunta 1.1
texto = "skjan looiac fretsec botas juhytiga weyiro reparar miuolis potroski\n"
CrearArchivoContenido("Doraland/LagoDubi/extranjero", texto)

texto = "En el archivo plano_barco se encuentra el plano del barco y en el archivo barco esta el actual del barco. Comparalos y di que esta mal\n"
CrearArchivoContenido("Doraland/LagoDubi/reparar", texto)

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

DirBasura("Doraland/LagoDubi/chikundubi", 0)


#####     Monte Sino      #####

# Creo el dir Monte Sino
DirBasura("Doraland/ElMonteSino", 600)
site2 = "Doraland/ElMonteSino/"

# Pregunta 2.1
CrearArchivo(site2 + "camino", 601)
os.system('echo "N1d0P00k33" >> ' + site2 + 'camino')
for i in range(602):
	os.system('echo "' + crap.pop().strip() + '" >> Doraland/ElMonteSino/camino')

DirBasura(site2 + "N1d0P00k33", 200)

# Pregunta 2.2
os.system('echo "Sabias que... cantamos la cancion del zorro el dia de cumpleanos de cada preparador?" >> ' + site2 + 'N1d0P00k33/webo')

# Pregunta 2.3
DirBasura(site2 + "aqui", 0)
DirBasura(site2 + "aqui/se", 200)
DirBasura(site2 + "aqui/se/encuentra", 200)
CrearArchivo(site2 + "aqui/se/encuentra/Pookee", 0)

# Pregunta 2.4
for i in range(1111):
	CrearArchivo(site2 + "N1d0P00k33/huevo" + str(i), 0)
	if i != 744:
		os.system('echo "pookee" >> ' + site2 + 'N1d0P00k33/huevo' + str(i))
	else:
		os.system('echo "intruso" >> ' + site2 + 'N1d0P00k33/huevo' + str(i))

# Pregunta 2.5
DirBasura(site2 + "cayendo", 0)
CrearArchivo(site2 + "aqui/se/encuentra/nidoDeAvispas", 0)
for i in range(2500):
	if i != 893:
		os.system("ln -s aquiNoEsta " + site2 + "cayendo/avispa" + str(i) )
	else:
		os.system('echo "/Doraland/ElMonteSino/aqui/se/encuentra/nidoDeAvispas" >> ' + site2 + 'cayendo/avispa893')


#####     Desierto del Charara      #####
DirBasura('Doraland/DesiertoDelCharara',0)
site3='Doraland/DesiertoDelCharara/'

# Pregunta 3.1
pass

# Pregunta 3.2
DirBasura(site3 + 'Piramide_POMAC',0)

DirBasura(site3 + 'Piramide_POMAC/ComidaPodrida', 25)


temporal = [randint(11, 7684) for x in range(1000)]
i = len(temporal)
while i > 1:
	os.system('echo "'+ str( temporal.pop() ) + '" >> ' + site3 + 'Piramide_POMAC/NeveraLLena')
	i -= 1

temporal = [randint(11, 7684) for x in range(1000)]
i = len(temporal)
while i > 1:
	os.system('echo "'+ str( temporal.pop() ) + '" >> ' + site3 + 'Piramide_POMAC/MicroondasSucio')
	i -= 1

# Pregunta 3.3
DirBasura(site3 + 'Piramide_Salas', 0)

os.system('mkdir --mode=777 ' + site3 + 'Piramide_Salas/SalaA')
os.system('mkdir --mode=777 ' + site3 + 'Piramide_Salas/SalaE')
os.system('mkdir --mode=777 ' + site3 + 'Piramide_Salas/SalaF')
os.system('mkdir --mode=777 ' + site3 + 'Piramide_Salas/SalaET')


os.system('echo "Para Sala A: " >> ' + site3 + 'Piramide_Salas/Instrucciones')
os.system('echo "Que el dueno tenga permisos de ejecucion, lectura y modificacion" >> ' + site3 + 'Piramide_Salas/Instrucciones')
os.system('echo "Que el grupo tenga solo Lectura y modificacion " >> ' + site3 + 'Piramide_Salas/Instrucciones')
os.system('echo "Todos los demas solo lectura\n" >> ' + site3 + 'Piramide_Salas/Instrucciones')

os.system('echo "Para Sala E: " >> ' + site3 + 'Piramide_Salas/Instrucciones')
os.system('echo "Que el dueno tenga todos los permisos" >> ' + site3 + 'Piramide_Salas/Instrucciones')
os.system('echo "Que los demas tengan ejecucion\n" >> ' + site3 + 'Piramide_Salas/Instrucciones')

os.system('echo "Para Sala F: " >> ' + site3 + 'Piramide_Salas/Instrucciones')
os.system('echo "Que el dueno y el grupo tengan permisos de lectura y modificacion" >> ' + site3 + 'Piramide_Salas/Instrucciones')
os.system('echo "Los demas solo lectura\n" >> ' + site3 + 'Piramide_Salas/Instrucciones')

os.system('echo "Para Sala ET: " >> ' + site3 + 'Piramide_Salas/Instrucciones')
os.system('echo "Sala ET esta en la mierda, estara cerrada para todos" >> ' + site3 + 'Piramide_Salas/Instrucciones')

os.system('chmod 111 ' + site3 + 'Piramide_Salas/Instrucciones')

# Pregunta 3.4
DirBasura(site3 + 'Piramide_Taquilla', 0)

cadena = ''
for i in range(12):
	cadena += crap.pop().strip()

os.system('echo "' + cadena + '" >> ' + site3 + 'Piramide_Taquilla/JeroglificosJP')

# Pregunta 3.5
pass

# Pregunta 3.6
DirBasura(site3 + 'TUTANKAMIN', 0)
lista = ['.aqui', '.todo', '.estaba', '.oculto', '.jejeps']

for i in lista:
	CrearArchivo(site3 + 'TUTANKAMIN/' + i, 0)
DirBasura(site3 + 'TUTANKAMIN/.PuertaSecreta', 0)

lista = ['Sacar', 'la', 'segunda', 'columna', 'de', 'este', 'archivo']

for i in lista:
	os.system('echo "' + i + '" >> ' + site3 + 'TUTANKAMIN/.jejeps')

# Pregunta 3.7
pass

# Pregunta 3.8
for i in range(50):
	for j in range(50):
		CrearArchivo(site3 + 'TUTANKAMIN/.PuertaSecreta/soldado' + str(i) + '*' + str(j), 0)

os.chmod(site3 + 'TUTANKAMIN/.PuertaSecreta', 0111)
# Pregunta 4
DirBasura('Doraland/CuevaDelChaMAC', 0)








































