import os, subprocess, sys
from shutil import which
import apt

programas = ['foremost','volatility','dd', 'sleuthkit']

# Para comprobar si los tres programas que necesitamos están instalados, llevamos a cabo esto
for programa in programas:
    if which(programa) is None:
        print("Instalando " + programa + "...")
    else:
        pass


cache = apt.Cache()

if cache['sleuthkit'].is_installed:
    print("No Instalar")
else:
    print("Instalar")


    





