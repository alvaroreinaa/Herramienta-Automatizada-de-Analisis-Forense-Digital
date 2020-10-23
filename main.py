import os, subprocess, sys
from scripts import usb, clonacion_evidencia

# Cuando se ejecuta el programa por primera vez, se crea la carpeta de evidencias
if os.path.isdir('./evidencias'):
    pass
else:
    os.system('mkdir evidencias')
    print('Introduzca sus evidencias en la siguiente ruta: ')
    os.system('cd evidencias;pwd')

# Cuando se ejecuta el programa por primera vez, se crea la carpeta de evidencias clonadas
if os.path.isdir('./evidenciasClonadas'):
    pass
else:
    os.system('mkdir evidenciasClonadas')
    print('Sus evidencia clonada se encuentran en la siguiente ruta: ')
    os.system('cd evidenciasClonadas;pwd')

# Preguntamos al usuario que tipo de evidencia desea clonar
tipoEvidencia = input("Indique el tipo de evidencia (0 = Memoria, 1 = Disco Duro, 2 = USB): ")
while (tipoEvidencia !='0') and (tipoEvidencia !='1') and (tipoEvidencia !='2'):
    print("Error: No ha elegido ningun tipo de evidencia valida")
    tipoEvidencia = input("Indique el tipo de evidencia (0 = Memoria, 1 = Disco Duro, 2 = USB): ")
 
# Según el tipo, realizamos las acciones pertinentes
if (tipoEvidencia == '0' or tipoEvidencia == '1'):
    clonacion_evidencia.clonacion_evidencia(tipoEvidencia)
elif (tipoEvidencia == '2'):
    usb.usb()
else:
    print("FATAL ERROR")
