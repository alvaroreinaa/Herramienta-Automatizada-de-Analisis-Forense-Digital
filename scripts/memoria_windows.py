import os, subprocess, sys

# Función que ejecuta los comandos según el tipo de análisis que se haya seleccionado
def analisis_memoria_windows(pathClonacion, nombreEvidencia, perfilImagen, comandos, pathResultados):
    # Comprobamos que la carpeta específica donde se almacenan los resultados de este tipo de análisis existe
    if os.path.isdir(pathResultados):
        pass
    else:
        os.system('mkdir ' + pathResultados)

    # Para cada comando de este análisis, guardamos su resultado en un fichero .txt en la carpeta anterior
    for comando in comandos:
        os.system('volatility -f ' + pathClonacion + ' --profile=' + perfilImagen + ' ' + comando + ' > ' + comando + '.txt')
        os.system('mv ' + comando + '.txt ' + pathResultados)
    
    print("Sus resultados se encuentran en: ")
    os.system('cd ' + pathResultados + ';pwd')

def memoria_windows(pathClonacion, nombreEvidencia, perfilImagen):
    # Preguntamos al usuario que tipo de accion desea llevar a cabo
    tipoAccion = int(input("\nIndique el tipo de acccion a realizar:\n"
                        "1. Análisis de procesos y DLLs.\n"
                        "2. Análisis de procesos de memoria.\n"
                        "3. Análisis de objetos y memoria del kernel.\n"
                        "4. Análisis de redes.\n"
                        "5. Análisis de registros.\n"
                        "6. Análisis del sistema de archivos.\n"
                        "7. Análisis personalizado.\n"
                        "8. Finalizar análisis.\n"))

    # Hasta que el usuario no seleccione finalizar el análisis, continuamos preguntando acciones
    while (True):
        if (tipoAccion == 1):
            comandos = ['pstree','psscan']
            pathResultados = './resultados/' + nombreEvidencia + '/AnalisisProcesosDLLs/'
            print("Realizando análisis de procesos y DLLs...")
            analisis_memoria(pathClonacion, nombreEvidencia, perfilImagen, comandos, pathResultados)
        elif (tipoAccion == 2):
            comandos = ['memmap','vadinfo']
            pathResultados = './resultados/' + nombreEvidencia + '/AnalisisProcesosMemoria/'
            print("Realizando análisis de procesos de memoria...")
            analisis_memoria(pathClonacion, nombreEvidencia, perfilImagen, comandos, pathResultados)
        elif (tipoAccion == 3):
            comandos = ['modules','modscan']
            pathResultados = './resultados/' + nombreEvidencia + '/AnalisisObjetosMemoriaKernel/'
            print("Realizando análisis de objetos y memoria del kernel...")
            analisis_memoria(pathClonacion, nombreEvidencia, perfilImagen, comandos, pathResultados)
        elif (tipoAccion == 4):
            comandos = ['netscan']
            pathResultados = './resultados/' + nombreEvidencia + '/AnalisisRedes/'
            print("Realizando análisis de redes...")
            analisis_memoria(pathClonacion, nombreEvidencia, perfilImagen, comandos, pathResultados)
        elif (tipoAccion == 5):
            comandos = ['hivelist','printkey']
            pathResultados = './resultados/' + nombreEvidencia + '/AnalisisRegistros/'
            print("Realizando análisis de registros...")
            analisis_memoria(pathClonacion, nombreEvidencia, perfilImagen, comandos, pathResultados)
        elif (tipoAccion == 6):
            comandos = ['mbrparser','mftparser']
            pathResultados = './resultados/' + nombreEvidencia + '/AnalisisSistemaArchivos/'
            print("Realizando análisis del sistema de archivos...")
            analisis_memoria(pathClonacion, nombreEvidencia, perfilImagen, comandos, pathResultados)
        elif (tipoAccion == 7):
            print("Abriendo consola interactiva volshell...")
            os.system('volatility -f ' + pathClonacion + ' --profile=' + perfilImagen + ' volshell')
        elif (tipoAccion == 8):
            sys.exit()
        else:
            print("Error: No ha elegido ningun tipo de acción válida\n")
    
        tipoAccion = int(input("\nIndique el tipo de acccion a realizar:\n"
                        "1. Análisis de procesos y DLLs.\n"
                        "2. Análisis de procesos de memoria.\n"
                        "3. Análisis de objetos y memoria del kernel.\n"
                        "4. Análisis de redes.\n"
                        "5. Análisis de registros.\n"
                        "6. Análisis del sistema de archivos.\n"
                        "7. Análisis personalizado.\n"
                        "8. Finalizar análisis.\n"))