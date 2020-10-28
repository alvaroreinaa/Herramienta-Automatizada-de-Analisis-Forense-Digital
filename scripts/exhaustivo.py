import os, subprocess, sys


#pathEvidencia: evidenciasClonadasUSB
#nombreEvidencia: pepe
#pathResultado: resultadosUSB
def exhaustivo(pathEvidencia, nombreEvidencia, pathResultado):

    nombreEvidenciaDD = nombreEvidencia + '.dd'
    pathFinal = pathEvidencia + '/' +  nombreEvidenciaDD
    carpeta = pathResultado + '/' + nombreEvidencia

    nombreDatos = input("Introduzca el nombre de los archivos en los que quiere recibir los datos: ")
    creacionFichero = nombreDatos + '1.txt'
    f = open(creacionFichero, "w")
    f.close()
    
    os.system('cd '+ pathEvidencia + ';file ' + nombreEvidenciaDD + ' > ' + '../'+ creacionFichero)
    fa = open(creacionFichero, "a")
    fd = os.open(pathFinal, os.O_RDONLY) 
    status = os.fstat(fd) 
    statusFinal = str(status)
    fa.write(statusFinal)
    os.close(fd) 
    fa.close()
    
    os.system('mv ' + creacionFichero + ' '+ carpeta)

   
    os.system('fls -m / -rp -f fat32 ' + pathFinal + ' >  ' + nombreDatos + '.fls')
    os.system('cat ' + nombreDatos + '.fls > ' + nombreDatos +'.mac')
    os.system('mactime -b ' + nombreDatos + '.mac > ' + nombreDatos +'.mactime')
    os.system('mv ' + nombreDatos + '.mactime ' + carpeta)
    os.system('rm ' + nombreDatos + '.fls; rm ' + nombreDatos + '.mac')
    print('Se ha generado un informe con información sobre esta evidencia en la siguiente ruta: ')
    os.system('cd ' + carpeta + ';pwd')
