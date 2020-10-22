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


    nombreClonacion = nombreEvidencia.split(".")[0] + ".img"
    pathClonacion = './evidenciasClonadas/' + nombreClonacion
    print(pathClonacion)
    
    if not os.path.isfile(pathClonacion):
        os.system('sudo dd if=' + pathEvidencia + ' of=' + nombreClonacion + ';mv ' + nombreClonacion + ' ./evidenciasClonadas')
    else:
        print("Archivo existente")
 