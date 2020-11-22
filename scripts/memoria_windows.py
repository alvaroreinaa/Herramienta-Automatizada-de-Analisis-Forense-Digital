import os, subprocess, sys
from multiprocessing import Pool
from functools import partial

# Función que imprime el path donde se encuentran los resultados
def path_resultados(pathResultados):
    print("Sus resultados se encuentran en: ")
    os.system('cd ' + pathResultados + ';pwd')

# Función que ejecuta los comandos según el tipo de análisis que se haya seleccionado
def analisis_memoria_windows(pathClonacion, nombreEvidencia, perfilImagen, pathResultados, comandos):
    # Comprobamos que la carpeta específica donde se almacenan los resultados de este tipo de análisis existe
    os.makedirs(pathResultados, exist_ok=True)

    # Para cada comando de este análisis, guardamos su resultado en un fichero .txt en la carpeta anterior
    os.system('volatility -f ' + pathClonacion + ' --profile=' + perfilImagen + ' ' + comandos + ' > ' + comandos + '.txt')
    os.system('mv ' + comandos + '.txt ' + pathResultados)

def memoria_windows(pathClonacion, nombreEvidencia, perfilImagen):
    # Hasta que el usuario no seleccione finalizar el análisis, continuamos preguntando acciones
    while (True):
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

        # Vamos a hacer uso de multiprocessing para poder paralelizar la ejecución de la función que ejecuta los comandos de volatility.
        # Distribuimos los múltiples comandos de cada tipo de análisis en diferentes procesos para agilizar el análisis.
        # Lo llevamos a cabo debido a que no necesitamos que termine la ejecucción del anterior comando para llevar a cabo los siguientes.
        pool = Pool()
        # Almacenamos los parámetros que no son iteriables en los procesos
        function = partial(analisis_memoria_windows, pathClonacion, nombreEvidencia, perfilImagen)
        
        if (tipoAccion == 1):
            #comandos = ['pstree','psscan','psxview','dlllist','handles','getsids','privs','envars','verinfo']
            comandos = ['pstree','psscan','dlllist']
            pathResultados = './resultados/' + nombreEvidencia + '/AnalisisProcesosDLLs/'
            print("Realizando análisis de procesos y DLLs...")
            function = partial(function, pathResultados)                                    # Almacenamos un parámetro no iterable más
            pool.map(function,comandos)                                                     # Ejecutamos los procesos para cada comando de manera paralela
            path_resultados(pathResultados)                                                 # Mostramos el path donde se han almacenado los resultados
        elif (tipoAccion == 2):
            #comandos = ['memmap','vadinfo', 'vadtree']
            comandos = ['memmap','vadinfo']
            pathResultados = './resultados/' + nombreEvidencia + '/AnalisisProcesosMemoria/'
            print("Realizando análisis de procesos de memoria...")
            function = partial(function, pathResultados)                                    # Almacenamos un parámetro no iterable más
            pool.map(function,comandos)                                                     # Ejecutamos los procesos para cada comando de manera paralela
            path_resultados(pathResultados)                                                 # Mostramos el path donde se han almacenado los resultados
        elif (tipoAccion == 3):
            #comandos = ['modules','modscan', 'ssdt', 'driverscan', 'filescan', 'mutantscan', 'symlinkscan', 'thredscan', 'unloadedmodules']
            comandos = ['modules','modscan','unloadedmodules']
            pathResultados = './resultados/' + nombreEvidencia + '/AnalisisObjetosMemoriaKernel/'
            print("Realizando análisis de objetos y memoria del kernel...")
            function = partial(function, pathResultados)                                    # Almacenamos un parámetro no iterable más
            pool.map(function,comandos)                                                     # Ejecutamos los procesos para cada comando de manera paralela
            path_resultados(pathResultados)                                                 # Mostramos el path donde se han almacenado los resultados
        elif (tipoAccion == 4):
            comandos = ['netscan']
            pathResultados = './resultados/' + nombreEvidencia + '/AnalisisRedes/'
            print("Realizando análisis de redes...")
            function = partial(function, pathResultados)                                    # Almacenamos un parámetro no iterable más
            pool.map(function,comandos)                                                     # Ejecutamos los procesos para cada comando de manera paralela
            path_resultados(pathResultados)                                                 # Mostramos el path donde se han almacenado los resultados
        elif (tipoAccion == 5):
            #comandos = ['hivelist','printkey'] 
            comandos = ['hivelist']
            pathResultados = './resultados/' + nombreEvidencia + '/AnalisisRegistros/'
            print("Realizando análisis de registros...")
            function = partial(function, pathResultados)                                    # Almacenamos un parámetro no iterable más
            pool.map(function,comandos)                                                     # Ejecutamos los procesos para cada comando de manera paralela
            path_resultados(pathResultados)                                                 # Mostramos el path donde se han almacenado los resultados
        elif (tipoAccion == 6):
            #comandos = ['mbrparser','mftparser']
            comandos = ['mbrparser']
            pathResultados = './resultados/' + nombreEvidencia + '/AnalisisSistemaArchivos/'
            print("Realizando análisis del sistema de archivos...")
            function = partial(function, pathResultados)                                    # Almacenamos un parámetro no iterable más
            pool.map(function,comandos)                                                     # Ejecutamos los procesos para cada comando de manera paralela
            path_resultados(pathResultados)                                                 # Mostramos el path donde se han almacenado los resultados
        elif (tipoAccion == 7):
            print("Abriendo consola interactiva volshell...")
            os.system('volatility -f ' + pathClonacion + ' --profile=' + perfilImagen + ' volshell')
        elif (tipoAccion == 8):
            sys.exit()
        else:
            print("Error: No ha elegido ningun tipo de acción válida\n")
        
        # Cerramos y terminamos los procesos del pool
        pool.close()
        pool.join()