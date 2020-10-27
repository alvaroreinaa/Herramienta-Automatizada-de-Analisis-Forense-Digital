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
    nombreClonacion = nombreEvidencia.split(".")[0] + ".dd"
    pathClonacion = './evidenciasClonadas/' + nombreClonacion
    
    # Booleano para controlar el bucle 
    existe = os.path.isfile(pathClonacion)

    # Si la evidencia clonada ya existe, le damos dos opciones al usuario
    while (existe):
        print("Evidencia clonada ya existente.")
        print("Introduzca 0 si desea eliminarla y crear una nueva")
        print("Introduzca 1 se desea continuar con la existente")
        seleccionUsuario = int(input())
        if (seleccionUsuario == 0):
            os.system('rm ' + pathClonacion)
            existe = False
        elif (seleccionUsuario == 1):
            existe = False
        else:
            print("Opción inválida\n")

    # Si no existe la evidencia clonada, la clonamos.
    if not os.path.isfile(pathClonacion):
        print("\nClonando evidencia: ")
        os.system('sudo dd if=' + pathEvidencia + ' of=./evidenciasClonadas/' + nombreClonacion + ' status=progress')
        os.system('cd evidenciasClonadas; md5sum ' + nombreClonacion)        # Realizamos una copia del hash de la evidencia para evitar que se altere
        print("\nSu evidencia se encuentra en: " + pathClonacion)
        os.system('mkdir ./resultados/' + nombreEvidencia.split(".")[0] + '/')
        print("Sus resultados se encuentran en: ")
        os.system('cd ./resultados/' + nombreEvidencia.split(".")[0] + ';pwd')

        

    #Dependiendo del tipo de evidencia, se realizan unas determinadas acciones
    if (tipoEvidencia == '0'):
        memoria.memoria()
    elif (tipoEvidencia == '1'):
        disco_duro.disco_duro(pathClonacion, nombreEvidencia.split(".")[0])
    else:
        print("FATAL ERROR")

    