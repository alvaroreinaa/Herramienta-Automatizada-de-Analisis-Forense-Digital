import os, subprocess, sys
from scripts import exhaustivo, foremost, disco_duro

# Función principal
def usb():
    usbEleccion = input("\nElija de entre las siguientes acciones:\n   1. Clonar USB \n   2. Analizar USB\n   3. Formatear USB \n\n   >")
    
    # Elección que nos permite formatear el USB
    if (usbEleccion == '3'):
        print("Estos son los USB conectados al equipo:")
        # Listamos los USB conectados en el momento de la ejecución
        os.system('lsblk | grep sdb')
        lugarUSBForm = input("Indique la posición en la que se encuentra el USB que desea formatear (Ejemplo: sdb1, sb2, etc...): ")
        decision = input('¿Está seguro de que desea formatear el dispositivo? (Y/N)')
        if (decision is 'Y'):
            os.system('sudo dd if=/dev/zero of=/dev/' + lugarUSBForm +  'status=progress bs=1m')
        else:
            print('Ha decidido no formatear el USB')
            pass

    # Elección que nos permite listar los USB clonados al equipo y hacer un clonado de estos
    elif (usbEleccion== '1'):
        print("Estos son los USB conectados al equipo:")
        # Listamos los USB conectados en el momento de la ejecución
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
        # Guardamos la imagen en la carpeta correspondiente
        os.system('sudo dd if=/dev/' + lugarUSB + ' of=' + nombreUSBFinal + ' status=progress bs=512'+ ';mv ' + nombreUSBFinal + ' ./evidenciasClonadasUSB')
        os.system('cd evidenciasClonadasUSB; md5sum ' + nombreUSBFinal)
        print("Imagen creada")
    
    # Elección que realizará un análisis del clonado de USB que elijamos
    elif (usbEleccion == '2'):
        print('Estos son los clonados de USB disponibles para analizar:')
        # Listamos todos los clonados de USB disponibles
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
        # Realizamos el análisis exhaustivo del USB
        exhaustivo.exhaustivo(pathEvidenciaUSB, nombreUSBCarpeta,resultadosCarpetaUSB)

        # Montamos el USB para extraer los archivos
        if os.path.isdir('/mnt/tmp'):
            pass
        else:
            os.system('mkdir /mnt/tmp')
        print('\nSu USB se encuentra montado en la siguiente ruta: ')
        os.system('cd /mnt/tmp;pwd')
        pathEvidenciaUSBForemost = './evidenciasClonadasUSB/' + nombreUSBCarpeta + '.dd'
        # Una vez comprobado esto, lo montamos en él
        os.system('sudo mount ' +  pathEvidenciaUSBForemost + ' /mnt/tmp')
        resultadosCarpetaUSBForemost = 'resultadosUSB/'

        #Realizamos las diversas acciones de recuperación y listado de archivos
        foremost.recuperar_archivos_eliminados(pathEvidenciaUSBForemost, nombreUSBCarpeta, resultadosCarpetaUSBForemost)
        disco_duro.listar_archivos_existentes_ocultos()
        disco_duro.desmontar_disco()
