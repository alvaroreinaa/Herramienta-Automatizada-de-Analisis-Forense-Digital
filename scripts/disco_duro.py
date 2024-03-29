import os, subprocess, sys
from scripts import foremost, exhaustivo

# Función que lista de manera recursiva todos los archivos existentes (tanto visibles como ocultos) de la imagen montada
def listar_archivos_existentes_ocultos(pathResultado, nombreEvidencia):
    print("Generando listado de los archivos existentes (tanto visibles como ocultos) de la evidencia en su carpeta de resultados")
    os.system('ls -R -A -l /mnt/tmp 2>/dev/null > listado_archivos.txt; mv listado_archivos.txt ' + pathResultado + nombreEvidencia + '/')
    print("Listado finalizado. El resultado se encuentra en el fichero listado_archivos.txt\n")
    
# Función que desmonta el disco duro una vez haya terminado el análisis
def desmontar_disco():
    os.system('sudo umount /mnt/tmp')
    print("Disco desmontado. Análisis finalizado")

# Función principal 
def disco_duro(pathClonacion, nombreEvidencia):
    # Antes de montar el disco duro, comprobamos que existe el directorio de montaje temporal
    os.makedirs('/mnt/tmp', exist_ok=True)
    print('\nSus disco duro se encuentra montado en la siguiente ruta: ')
    os.system('cd /mnt/tmp;pwd')

    # Una vez comprobado esto, lo montamos en él
    os.system('sudo mount ' +  pathClonacion + ' /mnt/tmp')

    # El path de donde se va a guardar los resultados de los discos duros
    pathResultado = './resultados/'

    # Hasta que el usuario no seleccione finalizar el análisis, continuamos preguntando acciones
    while (True):
        tipoAccion = int(input("Indique el tipo de acccion a realizar:\n"
                    "1. Recuperar archivos eliminados.\n"
                    "2. Analizar disco.\n"
                    "3. Listar archivos existentes y ocultos.\n"
                    "4. Finalizar el análisis.\n"))

        if (tipoAccion == 1):
            foremost.recuperar_archivos_eliminados(pathClonacion, nombreEvidencia, pathResultado)
        elif (tipoAccion == 2):
            pathEvidencia = "evidenciasClonadas"
            exhaustivo.exhaustivo(pathEvidencia, nombreEvidencia, pathResultado)
        elif (tipoAccion == 3):
            listar_archivos_existentes_ocultos(pathResultado, nombreEvidencia)
        elif (tipoAccion == 4):
            desmontar_disco()
            sys.exit()
        else:
            print("Error: No ha elegido ningun tipo de acción válida\n")
 
 

