import os, subprocess, sys
from scripts import usb, clonacion_evidencia, crear_carpetas, instalar_programas

# Creamos las carpetas inciales necesarias (en caso de ser la primera ejecución del programa)
crear_carpetas.crear_carpetas_iniciales()
# Instalamos los programas necesarios (en caso de que no estén instalados)
instalar_programas.instalar_programas()


# Preguntamos al usuario que tipo de evidencia desea clonar
tipoEvidencia = int(input("Indique el tipo de evidencia (0 = Memoria, 1 = Disco Duro, 2 = USB, 3 = Captura de red): "))
while (tipoEvidencia != 0) and (tipoEvidencia != 1) and (tipoEvidencia != 2) and (tipoEvidencia != 3):
    print("Error: No ha elegido ningun tipo de evidencia valida")
    tipoEvidencia = int(input("Indique el tipo de evidencia (0 = Memoria, 1 = Disco Duro, 2 = USB, 3 = Captura de red): "))
 
# Según el tipo, realizamos las acciones pertinentes
if (tipoEvidencia == 0 or tipoEvidencia == 1 or tipoEvidencia == 3):
    clonacion_evidencia.clonacion_evidencia(tipoEvidencia)
elif (tipoEvidencia == 2):
    usb.usb()
else:
    print("FATAL ERROR")
