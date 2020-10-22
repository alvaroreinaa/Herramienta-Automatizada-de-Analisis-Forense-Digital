import os, subprocess, sys
 
def memoria():
    # Listamos el directorio de evidencias
    print("Evidencias: ")
    os.system('cd evidencias;ls')
 
    # Le pedimos el nombre de la evidencia
    nombreEvidencia = input("Introduzca el nombre de la evidencia: ")
    pathEvidencia = './evidencias/' + nombreEvidencia
 
    # Comprobamos que la evidencia existe
    while(not os.path.isfile(pathEvidencia)):
        print("Archivo no encontrado")
        nombreEvidencia = input("Introduzca el nombre de la evidencia: ")
        pathEvidencia = './evidencias/' + nombreEvidencia
 
    # Cuando se ejecuta el programa por primera vez, se crea la carpeta de evidencias clonados
    if os.path.isdir('./evidenciasClonadas'):
        pass
    else:
        os.system('mkdir evidenciasClonadas')
        print('Sus evidencia clonada se encuentran en la siguiente ruta: ')
        os.system('cd evidenciasClonadas;pwd')
 

    nombreClonacion = nombreEvidencia.split(".")[0] + ".img"
    pathClonacion = './evidenciasClonadas/ + nombreClonacion
 
    if not os.path.isfile(pathClonacion):
        os.system('sudo dd if=' + pathEvidencia + ' of=' + nombreClonacion + ';mv ' + nombreClonacion + ' ./evidenciasClonadas')
    else:
        print("Archivo existente")
 
 
 
def usb():
      if os.path.isdir('./evidenciasClonadas'):
        pass
    else:
        os.system('mkdir evidenciasClonadas')
        print('Sus evidencias clonada se encuentran en la siguiente ruta: ')
        os.system('cd evidenciasClonadas;pwd')

    print("Estos son los USB contectados al equipo:")
    os.system('lsblk | grep sdb')
    lugarUSB = input("Indique la posición en la que se encuentra su dispositivo (Ejemplo: sdb1, sb2, etc...): ")
    nombreUSB = input("Indique qué nombre desea darle a la imagen: ")
    nombreUSBFinal = nombreUSB + '.img'
    print("Creando imagen del USB.")
    os.system('sudo dd if=/dev/' + lugarUSB + ' of=' + nombreUSBFinal + ' status=progress'+ ';mv ' + nombreUSBFinal + ' ./evidenciasClonadas')
    print("Imagen creada")

 
# Cuando se ejecuta el programa por primera vez, se crea la carpeta de evidencias
if os.path.isdir('./evidencias'):
    pass
else:
    os.system('mkdir evidencias')
    print('Introduzca sus evidencias en la siguiente ruta: ')
    os.system('cd evidencias;pwd')
    sys.exit(0)
 
# Preguntamos al usuario que tipo de evidencia desaea clonar
tipoEvidencia = input("Indique el tipo de evidencia (0 = memoria, 1 = USB): ")
while (tipoEvidencia is not '0') and (tipoEvidencia is not '1'):
    print(tipoEvidencia)
    print("Error: No ha elegido ningun tipo de evidencia valida")
    tipoEvidencia = input("Indique el tipo de evidencia (0 = memoria, 1 = USB): ")
 

if (tipoEvidencia is '0'):
    memoria()
elif (tipoEvidencia is '1'):
    usb()
else:
    print("ERROR")

