import os

def crear_carpetas_iniciales():
    # Cuando se ejecuta el programa por primera vez, se crea la carpeta de evidencias
    if os.path.isdir('./evidencias'):
        pass
    else:
        os.system('mkdir evidencias')
        print('Introduzca sus evidencias en la siguiente ruta: ')
        os.system('cd evidencias;pwd')

    # Cuando se ejecuta el programa por primera vez, se crea la carpeta de evidencias clonadas
    if os.path.isdir('./evidenciasClonadas'):
        pass
    else:
        os.system('mkdir evidenciasClonadas')
        print('Sus evidencias clonadas se encuentran en la siguiente ruta: ')
        os.system('cd evidenciasClonadas;pwd')

    # Cuando se ejecuta el programa por primera vez, se crea la carpeta de evidencias clonadas USB
    if os.path.isdir('./evidenciasClonadasUSB'):
        pass
    else:
        os.system('mkdir evidenciasClonadasUSB')
        print('Sus evidencias clonadas de USB se encuentran en la siguiente ruta: ')
        os.system('cd evidenciasClonadasUSB;pwd')

    # Cuando se ejecuta el programa por primera vez, se crea la carpeta de resultados
    if os.path.isdir('./resultados'):
        pass
    else:
        os.system('mkdir resultados')
        print('Sus resultados se encuentran en la siguiente ruta: ')
        os.system('cd resultados;pwd')

    # Cuando se ejecuta el programa por primera vez, se crea la carpeta de resultados USB
    if os.path.isdir('./resultadosUSB'):
        pass
    else:
        os.system('mkdir resultadosUSB')
        print('Sus resultados de USB se encuentran en la siguiente ruta: ')
        os.system('cd resultadosUSB;pwd')
        
    print('\n')