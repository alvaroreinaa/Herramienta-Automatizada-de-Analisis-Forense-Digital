import os, subprocess, sys
from scripts import disco_duro, memoria

def clonacion_evidencia(tipoEvidencia):
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

    # Almacenamos el path de la clonación
    nombreClonacion = nombreEvidencia.split(".")[0] + ".img"
    pathClonacion = './evidenciasClonadas/' + nombreClonacion
    
    # Si no existe la evidencia, la creamos. En caso contrario alertamos al usuario
    if not os.path.isfile(pathClonacion):
        print('sudo dd if=' + pathEvidencia + ' of=' + nombreClonacion + ' status=progress' + ';mv ' + nombreClonacion + ' ./evidenciasClonadas')
        os.system('sudo dd if=' + pathEvidencia + ' of=' + nombreClonacion + ' status=progress' + ';mv ' + nombreClonacion + ' ./evidenciasClonadas')
        print("Su evidencia se encuentra en: " + pathClonacion)
    else:
        print("Evidencia ya existente")
        """ Esto tenemos que poner algo para que vuelva al paso anterior ya que existe la evidencia y no debería dejarle continuar """

    #Dependiendo del tipo de evidencia, se realizan unas determinadas acciones
    if (tipoEvidencia == '0'):
        memoria.memoria()
    elif (tipoEvidencia == '1'):
        disco_duro.disco_duro(pathClonacion)
    else:
        print("FATAL ERROR")

    