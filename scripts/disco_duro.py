import os, subprocess, sys

# Función que recupera los archivos eliminados del disco y los recupera en una carpeta
def recuperar_archivos_eliminados(pathClonacion):
    print("Estas recuperando los archivos eliminados: ")
    os.system('foremost -v ' + pathClonacion + ' -o ./ResultadosRecuperacion')
    print("Tus archivos recuperados se encuentran en la siguiente carpeta: ResultadosRecuperados")

# Función que lista de manera recursiva todos los archivos existentes (tanto visibles como ocultos) de la imagen montada
def listar_archivos_existentes_ocultos():
    print("Listado de los archivos existentes (tanto visibles como ocultos) del disco montado: ")

    files = [os.path.join(dp, f) for dp, dn, filenames in os.walk('/mnt/tmp') for f in filenames]
    print(files)

# Función que desmonta el disco duro una vez haya terminado el análisis
def desmontar_disco():
    os.system('sudo umount /mnt/tmp')
    print("Disco desmontado. Análisis finalizado")

# Función principal 
def disco_duro(pathClonacion):
    # Antes de montar el disco duro, comprobamos que existe el directorio de montaje temporal
    if os.path.isdir('/mnt/tmp'):
        pass
    else:
        os.system('mkdir /mnt/tmp')
    
    print('Sus disco duro se encuentra montado en la siguiente ruta: ')
    os.system('cd /mnt/tmp;pwd')

    # Una vez comprobado esto, lo montamos en el directorio temporal
    os.system('sudo mount ' +  pathClonacion + ' /mnt/tmp')

    # Preguntamos al usuario que tipo de accion desea llevar a cabo
    tipoEvidencia = int(input("Indique el tipo de acccion a realizar:\n"
                          "1. Recuperar archivos eliminados.\n"
                          "2. Listar archivos existentes y ocultos.\n"
                          "3. Finalizar el análisis.\n"))

    while (True):
        if (tipoEvidencia == 1):
            recuperar_archivos_eliminados(pathClonacion)
        elif (tipoEvidencia == 2):
            listar_archivos_existentes_ocultos()
        elif (tipoEvidencia == 3):
            desmontar_disco()
            break
        else:
            print("Error: No ha elegido ningun tipo de acción válida")
        tipoEvidencia = int(input("Indique el tipo de acccion a realizar:\n"
                            "1. Recuperar archivos eliminados.\n"
                            "2. Listar archivos existentes y ocultos.\n"
                            "3. Finalizar el análisis.\n"))
 

