import os, subprocess, sys

# Función que recupera de manera personalizadas ciertos tipos de archivos de Foremost
def recuperacion_personalizada():
    tiposDeArchivos = ['gif','jpg','png','bmp','avi','mov','mpg','doc','docx','xls','xlsx','ppt','pptx','html','pdf','mp4','wav','wmv','exe','ole','zip','rar','cpp']
    extensionesUsuario = []

    # Hasta que el usuario no introduzca '0' para salir o introduzca alguna extensión válida para analizar
    seleccionUsuario = input("Introduzca las extensiones que desea recuperar (introduzca 0 para terminar): ")
    while (seleccionUsuario != '0' or len(extensionesUsuario) == 0):
        # Si la extensión introducida está aceptada por Foremost, la almacenamos
        if (seleccionUsuario in tiposDeArchivos):
            extensionesUsuario.append(seleccionUsuario)
            print("Extensión válida")
        # Si todavía no ha introducido ninguna extensión válida y quiere salir, se lo denegamos
        elif (seleccionUsuario == '0' and len(extensionesUsuario) == 0):
            print("Debe introducir al menos una extensión")
        else: 
            print("Extensión no soportada")
        seleccionUsuario = input("Introduzca las extensiones que desea recuperar (introduzca 0 para terminar): ")

    # Convertimos la lista a un string aceptado por Foremost
    extensionesUsuario = ','.join(extensionesUsuario) 

    return extensionesUsuario
    
    
# Función que recupera los archivos eliminados del disco duro y los almacena en una carpeta resultado
def recuperar_archivos_eliminados(pathClonacion, nombreEvidencia, pathResultado):

    # Le ofrecemos diferentes tipos de recuperación al usuario para que elija a su gusto
    tipoRecuperacion = int(input('Seleccione el tipo de recuperación que desea realizar:\n'
                                  '1. Recuperacion total\n'
                                  '2. Recuperar archivos gráficos (gif,jpg,png,bmp)\n'
                                  '3. Recuperar archivos de animación (avi,mov,mpg)\n'
                                  '4. Recuperar archivos Microsoft Office (doc,docx,xls,xlsx,ppt,pptx)\n'
                                  '5. Recuperar HTML y Adobe PDF (html,pdf)\n'
                                  '6. Recuperar archivos de sonido (mp4,wav,wmv)\n'
                                  '7. Recuperar otro tipo de archivos adicionales (exe,ole,zip,rar,cpp)\n'
                                  '8. Recuperar archivos de manera personalizada\n'))

    # Según el tipo que haya elegido, lo llevamos a cabo 
    if (tipoRecuperacion >= 1 and tipoRecuperacion <= 8):
        if (tipoRecuperacion == 1):
            print("\nEstas recuperando todos los archivos eliminados: ")
            os.system('foremost -v ' + pathClonacion + ' -o ' + pathResultado + nombreEvidencia + '/ResultadosRecuperacion/ > /dev/null')
        elif (tipoRecuperacion == 2):
            extensionesGraficos = 'gif,jpg,png,bmp'
            print("\nEstas recuperando todos los archivos gráficos: ")
            os.system('foremost -v ' + pathClonacion + ' -t ' + extensionesGraficos + ' -o ' + pathResultado + nombreEvidencia + '/ResultadosRecuperacion/ > /dev/null')
        elif (tipoRecuperacion == 3):
            extensionesAnimados = 'avi,mov,mpg'
            print("\nEstas recuperando todos los archivos animados: ")
            os.system('foremost -v ' + pathClonacion + ' -t ' + extensionesAnimados + ' -o ' + pathResultado + nombreEvidencia + '/ResultadosRecuperacion/ > /dev/null')
        elif (tipoRecuperacion == 4):
            extensionesOffice = 'doc,docx,xls,xlsx,ppt,pptx'
            print("\nEstas recuperando todos los archivos Microsoft Office: ")
            os.system('foremost -v ' + pathClonacion + ' -t ' + extensionesOffice + ' -o ' + pathResultado + nombreEvidencia + '/ResultadosRecuperacion/ > /dev/null')
        elif (tipoRecuperacion == 5):
            extensionesHTML_PDF = 'pdf,html'
            print("\nEstas recuperando todos los archivos HTML/PDF: ")
            os.system('foremost -v ' + pathClonacion + ' -t ' + extensionesHTML_PDF + ' -o ' + pathResultado + nombreEvidencia + '/ResultadosRecuperacion/ > /dev/null')
        elif (tipoRecuperacion == 6):
            extensionesSonido = 'mp4,wav,wmv'
            print("\nEstas recuperando todos los archivos de sonido: ")
            os.system('foremost -v ' + pathClonacion + ' -t ' + extensionesSonido + ' -o ' + pathResultado + nombreEvidencia + '/ResultadosRecuperacion/ > /dev/null')
        elif (tipoRecuperacion == 7):
            extensionesAdicionales = 'exe,ole,zip,rar,cpp'
            print("\nEstas recuperando todos los archivos adicionales: ")
            os.system('foremost -v ' + pathClonacion + ' -t ' + extensionesAdicionales + ' -o ' + pathResultado + nombreEvidencia + '/ResultadosRecuperacion/ > /dev/null')
        elif (tipoRecuperacion == 8):
            extensionesUsuario = recuperacion_personalizada()
            print("\nEstas recuperando todos los archivos personalizados: ")
            os.system('foremost -v ' + pathClonacion + ' -t ' + extensionesUsuario + ' -o ' + pathResultado + nombreEvidencia + '/ResultadosRecuperacion/ > /dev/null')

        print("Tus archivos recuperados se encuentran en la siguiente carpeta:")
        os.system('cd ' + pathResultado + nombreEvidencia + '/ResultadosRecuperacion/;pwd')
        print("\n")
    else:
        print("Has seleccionado un tipo de recuperación incorrecta.")
