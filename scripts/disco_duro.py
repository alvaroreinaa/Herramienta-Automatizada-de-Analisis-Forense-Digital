import os, subprocess, sys
from scripts import foremost

# Función que lista de manera recursiva todos los archivos existentes (tanto visibles como ocultos) de la imagen montada
def listar_archivos_existentes_ocultos():
    print("Listado de los archivos existentes (tanto visibles como ocultos) del disco montado: ")
    os.system('cd /mnt/tmp; ls -R -a')
    print("\n")
    
# Función que desmonta el disco duro una vez haya terminado el análisis
def desmontar_disco():
    os.system('sudo umount /mnt/tmp')
    print("Disco desmontado. Análisis finalizado")

# Función principal 
def disco_duro(pathClonacion, nombreEvidencia):
    # Antes de montar el disco duro, comprobamos que existe el directorio de montaje temporal
    if os.path.isdir('/mnt/tmp'):
        pass
    else:
        os.system('mkdir /mnt/tmp')
    
    print('\nSus disco duro se encuentra montado en la siguiente ruta: ')
    os.system('cd /mnt/tmp;pwd')

    # Una vez comprobado esto, lo montamos en él
    os.system('sudo mount ' +  pathClonacion + ' /mnt/tmp')

    # El path de donde se va a guardar los resultados de los discos duros
    pathResultado = './resultados/'

    # Preguntamos al usuario que tipo de accion desea llevar a cabo
    tipoAccion = int(input("Indique el tipo de acccion a realizar:\n"
                          "1. Recuperar archivos eliminados.\n"
                          "2. Listar archivos existentes y ocultos.\n"
                          "3. Finalizar el análisis.\n"))

    
    # Hasta que el usuario no seleccione finalizar el análisis, continuamos preguntando acciones
    while (True):
        if (tipoAccion == 1):
            foremost.recuperar_archivos_eliminados(pathClonacion, nombreEvidencia, pathResultado)
        elif (tipoAccion == 2):
            listar_archivos_existentes_ocultos()
        elif (tipoAccion == 3):
            desmontar_disco()
            sys.exit()
        else:
            print("Error: No ha elegido ningun tipo de acción válida\n")
        tipoAccion = int(input("Indique el tipo de acccion a realizar:\n"
                            "1. Recuperar archivos eliminados.\n"
                            "2. Listar archivos existentes y ocultos.\n"
                            "3. Finalizar el análisis.\n"))
 

