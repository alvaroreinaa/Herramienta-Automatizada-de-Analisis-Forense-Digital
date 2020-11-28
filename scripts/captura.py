import os, subprocess, sys

# pathClonacion = ./evidenciasClonadas/captura1.pcap
# nombreEvidencia = captura1.pcap
def captura(pathClonacion, nombreEvidencia):

    nombreCaptura = nombreEvidencia + '.pcap'
    while (True):
        tipoAnalisis = int(input("\nIndique el tipo de análisis que desea realizar: \n\n\t1. Extracción completa\n\t2. Extracción de archivos\n\t3. Extracción de consultas DNS con dirección IP de respuesta y hora de la petición\n\t4. Búsqueda (No funcional)\n\t5. Información sobre la captura de red\n\t6. Extracción de contraseñas\n\t7. Terminar extracción \n\n  > "))
        if (tipoAnalisis == 1):

            # Este comando imprime todo el contenido de la captura seleccionada y crea un fichero con los resultados
            os.system('cd evidenciasClonadas; tshark -r ' + nombreCaptura + '> ../resultados/'+ nombreEvidencia+ '/Completa.txt')
            print('El archivo "Completa.txt" con la información se encuentra en la ruta: \n')
            os.system('cd resultados/' + nombreEvidencia +'; pwd')
            print('\n')

        elif (tipoAnalisis == 2):
            tipoExtraccion = int(input('Elija el protocolo del cual desea extraer archivos: \n\n\t 1. SMB \n\t 2. HTTP \n\t 3. FTP \n\t 4. IMF\n\t 5. Todos los anteriores \n\n > '))

            if(tipoExtraccion == 1):
                carpetaSMB = '../resultados/' + nombreEvidencia + '/ArchivosRecuperadosSMB'
                # Este comando recupera todos los archivos transferidos por protocolo SMB y los almacena en una carpeta con su nombre
                os.system('cd evidenciasClonadas; tshark -nr '+ nombreCaptura +' --export-objects smb,' + carpetaSMB + '>/dev/null')
                print('Los archivos recuperados se encuentran en la ruta: \n')
                os.system('cd resultados/' + nombreEvidencia +'/ArchivosRecuperadosSMB; pwd')
                print('\n')

            elif(tipoExtraccion == 2):
                carpetaHTTP = '../resultados/' + nombreEvidencia + '/ArchivosRecuperadosHTTP'
                # Este comando recupera todos los archivos transferidos por protocolo HTTP y los almacena en una carpeta con su nombre
                os.system('cd evidenciasClonadas; tshark -nr '+ nombreCaptura +' --export-objects http,' + carpetaHTTP + '>/dev/null')
                print('Los archivos recuperados se encuentran en la ruta: \n')
                os.system('cd resultados/' + nombreEvidencia +'/ArchivosRecuperadosHTTP; pwd')
                print('\n')

            elif(tipoExtraccion == 3):
                carpetaTFTP = '../resultados/' + nombreEvidencia + '/ArchivosRecuperadosTFTP'
                # Este comando recupera todos los archivos transferidos por protocolo FTP y los almacena en una carpeta con su nombre
                os.system('cd evidenciasClonadas; tshark -nr '+ nombreCaptura +' --export-objects tftp,' + carpetaTFTP + '>/dev/null')
                print('Los archivos recuperados se encuentran en la ruta: \n')
                os.system('cd resultados/' + nombreEvidencia +'/ArchivosRecuperadosFTP; pwd')
                print('\n')

            elif(tipoExtraccion == 4):
                carpetaIMF = '../resultados/' + nombreEvidencia + '/ArchivosRecuperadosIMF'
                # Este comando recupera todos los archivos transferidos por protocolo IMF y los almacena en una carpeta con su nombre
                os.system('cd evidenciasClonadas; tshark -nr '+ nombreCaptura +' --export-objects imf,' + carpetaIMF + '>/dev/null')
                print('Los archivos recuperados se encuentran en la ruta: \n')
                os.system('cd resultados/' + nombreEvidencia +'/ArchivosRecuperadosIMF; pwd')
                print('\n')

            if(tipoExtraccion == 5):
                # Estos comandos recuperan todos los archivos transferidos por los protocolos admitidos y los almacena en una carpeta con su nombre
                carpetaSMB = '../resultados/' + nombreEvidencia + '/ArchivosRecuperadosSMB'
                os.system('cd evidenciasClonadas; tshark -nr '+ nombreCaptura +' --export-objects smb,' + carpetaSMB + '>/dev/null')
                carpetaHTTP = '../resultados/' + nombreEvidencia + '/ArchivosRecuperadosHTTP'
                os.system('cd evidenciasClonadas; tshark -nr '+ nombreCaptura +' --export-objects http,' + carpetaHTTP + '>/dev/null')
                carpetaTFTP = '../resultados/' + nombreEvidencia + '/ArchivosRecuperadosTFTP'
                os.system('cd evidenciasClonadas; tshark -nr '+ nombreCaptura +' --export-objects tftp,' + carpetaTFTP + '>/dev/null')
                carpetaIMF = '../resultados/' + nombreEvidencia + '/ArchivosRecuperadosIMF'
                os.system('cd evidenciasClonadas; tshark -nr '+ nombreCaptura +' --export-objects imf,' + carpetaIMF + '>/dev/null')
                print('Los archivos recuperados se encuentran en la ruta: \n')
                os.system('cd resultados/' + nombreEvidencia + '; pwd')
                print('\n')

        elif (tipoAnalisis == 3):
            # Este comando recupera tanto la consulta del DNS como la dirección de respuesta y la almacena en un fichero
            os.system('cd evidenciasClonadas; tshark -r ' + nombreCaptura + ' -n -T fields -e frame.time -e ip.src -e ip.dst -e dns.qry.name -e dns.a > ../resultados/'+ nombreEvidencia + '/DNS.txt')
            print('El archivo "DNS.txt" con la información se encuentra en la ruta: \n')
            os.system('cd resultados/' + nombreEvidencia +'; pwd')
            print('\n')

        elif(tipoAnalisis == 4):
            busqueda = input('Introduzca la palabra por la que quiere filtrar: ')
            os.system('cd evidenciasClonadas; tshark -r' + nombreCaptura + ' -T fields -e ip.src -e ip.dst  http.host contains ' + busqueda)

        elif(tipoAnalisis == 5):
            # Este comando recupera información sobre la propia captura y la guarda en un fichero
            os.system('cd evidenciasClonadas; capinfos ' + nombreCaptura + '> ../resultados/'+ nombreEvidencia + '/InformacionCaptura.txt')
            print('El archivo "InformacionCaptura.txt" con la información se encuentra en la ruta: \n')
            os.system('cd resultados/' + nombreEvidencia +'; pwd')
            print('\n')
        
        elif(tipoAnalisis == 6):
            #Este comando recupera las contraseñas que se hayan pasado por protocolo HTTP, en caso de que las haya
            os.system('cd evidenciasClonadas;tshark -r'+ nombreCaptura +' -Y \'http.request.method == POST and tcp contains "password"\' | grep password > ../resultados/'+ nombreEvidencia + '/Passwords.txt')
            print('El archivo "Passwords.txt" con la información se encuentra en la ruta: \n')
            os.system('cd resultados/' + nombreEvidencia +'; pwd')
            print('\n')

        elif (tipoAnalisis == 7):
            # Si el usuario elige esta opción, sale del bucle del programa
            sys.exit()
        else:

            print ('El comando introducido no es válido. \n')
