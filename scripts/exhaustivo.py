import os, subprocess, sys

# Formato de parametros que se espera recibir: 
#
#   pathEvidencia: evidenciasClonadasUSB
#   nombreEvidencia: nombre
#   pathResultado: resultadosUSB

def exhaustivo(pathEvidencia, nombreEvidencia, pathResultado):

    nombreEvidenciaDD = nombreEvidencia + '.dd'
    pathFinal = pathEvidencia + '/' +  nombreEvidenciaDD
    carpeta = pathResultado + '/' + nombreEvidencia

    nombreDatos = input("Introduzca el nombre de los archivos en los que quiere recibir los datos: ")
    creacionFichero = nombreDatos + '1.txt'
    # Creamos un .txt en el que almacenar los datos 
    f = open(creacionFichero, "w")
    f.close()
    # Guardamos el resultado del comando file en dicho archivo
    os.system('cd '+ pathEvidencia + ';file ' + nombreEvidenciaDD + ' > ' + '../'+ creacionFichero)
    fa = open(creacionFichero, "a")
    # Guardamos los resultados de la función fstat en el mismo archivo
    fd = os.open(pathFinal, os.O_RDONLY) 
    status = os.fstat(fd) 
    statusFinal = str(status)
    fa.write(statusFinal)
    os.close(fd) 
    fa.close()
    # Movemos el archivo a su carpeta correspondiente
    os.system('mv ' + creacionFichero + ' '+ carpeta)
    
    # Guardamos el resultado del comando fls en un archivo .fls
    os.system('fls -m / -rp -f fat32 ' + pathFinal + ' >  ' + nombreDatos + '.fls')
    os.system('cat ' + nombreDatos + '.fls > ' + nombreDatos +'.mac')
    # Guardamos el resultado del comando mactime en un archivo .mac y des pués lo convertimos en .mactime para poder visualizarlo
    os.system('mactime -b ' + nombreDatos + '.mac > ' + nombreDatos +'.mactime')
    os.system('mv ' + nombreDatos + '.mactime ' + carpeta)
    os.system('rm ' + nombreDatos + '.fls; rm ' + nombreDatos + '.mac')
    # Movemos ambos archivos a su carpeta correspondiente
    print('Se ha generado un informe con información sobre esta evidencia en la siguiente ruta: ')
    os.system('cd ' + carpeta + ';pwd')
