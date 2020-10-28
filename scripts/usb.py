import os, subprocess, sys
from scripts import exhaustivo

def usb():
    usbEleccion = input("\nElija de entre las siguientes acciones:\n   1. Clonar USB \n   2. Analizar USB\n   3. Formatear USB \n\n   >")
    
    if (usbEleccion == '3'):
        print("Estos son los USB contectados al equipo:")
        os.system('lsblk | grep sdb')
        lugarUSBForm = input("Indique la posición en la que se encuentra el USB que desea formatear (Ejemplo: sdb1, sb2, etc...): ")
        decision = input('¿Está seguro de que desea formatear el dispositivo? (Y/N)')
        if (decision is 'Y'):
            os.system('sudo dd if=/dev/zero of=/dev/' + lugarUSBForm +  'status=progress bs=1m')
        else:
            print('Ha decidido no formatear el USB')
            pass

    elif (usbEleccion== '1'):
        print("Estos son los USB conectados al equipo:")
        os.system('lsblk | grep sdb')
        lugarUSB = input("Indique la posición en la que se encuentra su dispositivo (Ejemplo: sdb1, sb2, etc...): ")
        nombreUSB = input("Indique qué nombre desea darle a la imagen: ")
        resultadosDir = './resultadosUSB' + nombreUSB

        if   os.path.isdir(resultadosDir):
            pass
        else:
            os.system('mkdir ./resultadosUSB/' + nombreUSB + '/')
            print("Sus resultados se encuentran en: ")
            os.system('cd ./resultadosUSB/' + nombreUSB + ';pwd')

        nombreUSBFinal = nombreUSB + '.dd'
        print("Creando imagen del USB.")
        os.system('sudo dd if=/dev/' + lugarUSB + ' of=' + nombreUSBFinal + ' status=progress bs=512'+ ';mv ' + nombreUSBFinal + ' ./evidenciasClonadasUSB')
        os.system('cd evidenciasClonadasUSB; md5sum ' + nombreUSBFinal)
        print("Imagen creada")
    
    elif (usbEleccion == '2'):
        print('Estos son los clonados de USB disponibles para analizar:')
        os.system('cd evidenciasClonadasUSB;ls')
        USBAnalisis = input('Elija el nombre del usb que desea analizar: ')
        nombreUSBCarpeta = USBAnalisis.split(".")[0]
        resultadosDirUSB = './resultadosUSB/' + nombreUSBCarpeta
        if  os.path.isdir(resultadosDirUSB):
            pass
        else:
            os.system('mkdir ./resultadosUSB/' + nombreUSBCarpeta + '/')
            print("Sus resultados se encuentran en: ")
            os.system('cd ./resultadosUSB/' + nombreUSBCarpeta + ';pwd')

        pathEvidenciaUSB = 'evidenciasClonadasUSB'
        resultadosCarpetaUSB = 'resultadosUSB'
        exhaustivo.exhaustivo(pathEvidenciaUSB, nombreUSBCarpeta,resultadosCarpetaUSB)
        
'''
        print('Información disponible sobre el USB que ha elegido: \n')
        os.system('cd evidenciasClonadasUSB;file ' + USBAnalisis)
        pathUSB = './evidenciasClonadasUSB/' + USBAnalisis 
        print('\n')
        fd = os.open(pathUSB, os.O_RDONLY) 
        status = os.fstat(fd) 
        print(status) 
        os.close(fd) 
        nombreDatosUSB = input("Introduzca el nombre del archivo en el que quiere recibir los datos: ")
        os.system('fls -m / -rp -f fat32 ' + pathUSB + ' >  ' + nombreDatosUSB + '.fls')
        os.system('cat ' + nombreDatosUSB + '.fls > ' + nombreDatosUSB +'.mac')
        os.system('mactime -b ' + nombreDatosUSB + '.mac > ' + nombreDatosUSB +'.mactime')
        os.system('mv ' + nombreDatosUSB + '.mactime resultados/' + nombreUSBCarpeta)
        os.system('rm ' + nombreDatosUSB + '.fls; rm ' + nombreDatosUSB + '.mac')
        print('Se ha generado un informe con información sobre esta evidencia en la siguiente ruta: ')
        os.system('cd resultados/' + nombreUSBCarpeta + ';pwd')

        '''