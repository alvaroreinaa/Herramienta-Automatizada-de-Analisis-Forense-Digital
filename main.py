import os, subprocess, sys
from scripts import memoria, usb

# Cuando se ejecuta el programa por primera vez, se crea la carpeta de evidencias
if os.path.isdir('./evidencias'):
    pass
else:
    os.system('mkdir evidencias')
    print('Introduzca sus evidencias en la siguiente ruta: ')
    os.system('cd evidencias;pwd')

# Cuando se ejecuta el programa por primera vez, se crea la carpeta de evidencias clonados
if os.path.isdir('./evidenciasClonadas'):
    pass
else:
    os.system('mkdir evidenciasClonadas')
    print('Sus evidencia clonada se encuentran en la siguiente ruta: ')
    os.system('cd evidenciasClonadas;pwd')

# Preguntamos al usuario que tipo de evidencia desaea clonar
tipoEvidencia = input("Indique el tipo de evidencia (0 = memoria, 1 = USB): ")
while (tipoEvidencia is not '0') and (tipoEvidencia is not '1'):
    print(tipoEvidencia)
    print("Error: No ha elegido ningun tipo de evidencia valida")
    tipoEvidencia = input("Indique el tipo de evidencia (0 = memoria, 1 = USB): ")
 

if (tipoEvidencia is '0'):
    memoria.memoria()
elif (tipoEvidencia is '1'):
    usb.usb()
else:
    print("ERROR")
