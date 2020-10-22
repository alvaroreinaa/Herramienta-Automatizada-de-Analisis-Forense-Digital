import os, subprocess, sys

def usb():
    print("Estos son los USB contectados al equipo:")
    os.system('lsblk | grep sdb')
    lugarUSB = input("Indique la posición en la que se encuentra su dispositivo (Ejemplo: sdb1, sb2, etc...): ")
    nombreUSB = input("Indique qué nombre desea darle a la imagen: ")
    nombreUSBFinal = nombreUSB + '.img'
    print("Creando imagen del USB.")
    os.system('sudo dd if=/dev/' + lugarUSB + ' of=' + nombreUSBFinal + ' status=progress'+ ';mv ' + nombreUSBFinal + ' ./evidenciasClonadas')
    print("Imagen creada")