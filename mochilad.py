import os
import sys

if os.geteuid() != 0:
    print("Debes correr este script como root, genio.")
    sys.exit(1)

# Paths de la tarea
path_general = "/home/invitado/Tarea3"
mochila      = path_general + "/mochila"
lago_dubi    = path_general + "/LagoDubi"
monte_sino   = path_general + "/ElMonteSino"
desierto_sc  = path_general + "/DesiertoDelCharara"
cueva_chamac = path_general + "/CuevaDelChaMAC"
command = "ls " + mochila
bools = [True, True, True]

paths = [ path_general, lago_dubi, monte_sino, desierto_sc, cueva_chamac ]

item_lago    = None
item_monte    = None
item_desierto = None

# Verifica si la mochila existe, si no existe la crea
if not os.path.exists(mochila):
    print("No crearon la mochila, genios.")
    os.makedirs(mochila)

# Verifica si los paths existen y que tengan los permisos correctos en un
# principio
for path in paths:
    if not os.path.exists(path):
        os.makedirs(path, 0000)
    elif str(oct(os.stat(path)[0])) != '040000':
        os.chmod(path, 0000)

contenido = open("contenido_mochila.txt")

for item in contenido:
    if item[:2] == "#1":
        item_lago = contenido.next()
    elif item[:2] == "#2":
        item_monte = contenido.next()
    elif item[:2] == "#3":
        item_desierto = contenido.next()


while(True):

    ls = os.popen(command).read()
    ls.split('\n')

    if item_lago in ls and bools[0]:
        print("Felicidades")
        os.chmod(monte_sino, 0755)
        bools[0] = False
    if item_monte in ls and bools[1]:
        print("Felicidades")
        os.chmod(desierto_sc, 0755)
        bools[1] = False
    if item_desierto in ls and bools[2]:
        print("Felicidades")
        os.chmod(cueva_chamac, 0755)
        bools[2] = False

