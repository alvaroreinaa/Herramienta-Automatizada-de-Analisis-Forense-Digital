import os, subprocess, sys
from scripts import disco_duro, memoria

def clonacion_evidencia(tipoEvidencia):
    # Si existe alguna evidencia dentro del directorio le alertamos al usuario
    if not os.listdir('./evidencias/'):
        print("La carpeta no contiene evidencias. Por favor, introduzca una para utilizar el programa.")
        sys.exit()

    # Listamos las evidencias según el tipo que se ha indicado
    print("Evidencias: ")
    if (tipoEvidencia == 0):
        os.system('cd evidencias;ls | grep ".mem"')
    elif (tipoEvidencia == 1):
        os.system('cd evidencias;ls | grep ".img\|.001"')    
 
    # Le pedimos el nombre de la evidencia
    nombreEvidencia = input("Introduzca el nombre de la evidencia: ")
    pathEvidencia = './evidencias/' + nombreEvidencia
 
    # Comprobamos que la evidencia existe
    while(not os.path.isfile(pathEvidencia)):
        print("Evidencia no encontrada")
        nombreEvidencia = input("Introduzca el nombre de la evidencia: ")
        pathEvidencia = './evidencias/' + nombreEvidencia

    # Según el tipo de evidencia, tendrá una extensión u otra
    if (tipoEvidencia == 0):
        nombreClonacion = nombreEvidencia.split(".")[0] + ".mem"
    elif (tipoEvidencia == 1):
        nombreClonacion = nombreEvidencia.split(".")[0] + ".dd"
    # Almacenamos el path de la clonación
    pathClonacion = './evidenciasClonadas/' + nombreClonacion
    
    # Booleano para controlar el bucle 
    existe = os.path.isfile(pathClonacion)

    # Si la evidencia clonada ya existe, le damos dos opciones al usuario: Eliminar y crear una nueva o continuar con la existente
    while (existe):
        print("Evidencia clonada ya existente.")
        print("Introduzca 0 si desea eliminarla y crear una nueva (también se eliminará su carpeta de resultados)")
        print("Introduzca 1 se desea continuar con la existente")
        seleccionUsuario = int(input())
        if (seleccionUsuario == 0):
            os.system('rm ' + pathClonacion + ';rm -r ./resultados/' + nombreEvidencia.split(".")[0])
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
    
    # Si no existe su respectiva carpeta de resultados, la creamos
    pathResultado = './resultados/' + nombreEvidencia.split(".")[0] + '/'
    if not os.path.isdir(pathResultado):       
        os.system('mkdir ' + pathResultado)
        print("Sus resultados se encuentran en: ")
        os.system('cd ' + pathResultado + ';pwd')

    #Dependiendo del tipo de evidencia, se realizan unas determinadas acciones
    if (tipoEvidencia == 0):
        memoria.memoria()
    elif (tipoEvidencia == 1):
        disco_duro.disco_duro(pathClonacion, nombreEvidencia.split(".")[0])
    else:
        print("FATAL ERROR")

    