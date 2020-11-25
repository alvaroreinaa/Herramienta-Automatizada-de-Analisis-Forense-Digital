import os, subprocess, sys
from shutil import which
import apt

def instalar_programas():
    programas = ['foremost','volatility','dd']
 
    # Para comprobar si los tres programas que necesitamos están instalados, llevamos a cabo esto
    for programa in programas:
        if which(programa) is None:
            print("Instalando " + programa + "...")
            os.system('sudo apt-get install ' + programa + ' -y  > /dev/null')
        else:
            pass
    
    # Para comprobar si el paquete sleuthkit que necesitamos está instalado, llevamos a cabo esto
    cache = apt.Cache()

    if cache['sleuthkit'].is_installed:
        pass
    else:
        print("Instalando sleuthkit...")
        os.system('sudo apt-get install sleuthkit -y  > /dev/null')