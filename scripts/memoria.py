import os, subprocess, sys
from scripts import memoria_windows


def memoria(pathClonacion, nombreEvidencia):
    # Obtenemos el perfil de la memoria para poder llevar a cabo el análisis y guardamos el resultado en un fichero
    print("Obteniendo perfil de la memoria...(Esto puede tardar varios minutos)")
    os.system('volatility -f ' + pathClonacion + ' imageinfo > imageinfo.txt')

    # Filtramos el dato que estamos buscando en dicho fichero
    perfilImagen = subprocess.getoutput("awk '/Suggested/ { print }' imageinfo.txt | awk 'NF>1{print $NF}' | sed 's/)//'")

    # Indicamos la ruta del resultado al usuario y el nombre de su perfil
    os.system('mv imageinfo.txt ./resultados/' + nombreEvidencia + '/') 
    print("La información de su imagen se ha guardado en: ./resultados/" + nombreEvidencia + "/imageinfo.txt")  
    print("El perfil de su imagen es: " + perfilImagen)
    #perfilImagen = 'Win10x64_15063'
    
    # Analizamos el perfil para saber de que sistema operativo proviene la memoria para poder ejecutar unos comandos u otros
    if ('Win' in perfilImagen):
        memoria_windows.memoria_windows(pathClonacion, nombreEvidencia, perfilImagen)
    else:
        pass

    
 
