# Proyecto Ciberseguridad
_Herramienta de automatización de análisis forense destinada a ser ejecutada en sistemas operativos Ubuntu._

### Pre-requisitos 📋
Para el correcto funcionamiento de la herramienta se necesitará una serie de programas y paquetes ya instalados en el equipo:

```
Foremost
Volatility
Sleuthkit
dd
Tshark 
```
_Durante la instalación de tshark, llegará un punto que la barra no parpadee, ahí tendrá que presionar enter y espacio para que la instalación continue_

Si no están instalados, se le instalarán cuando ejecute la herramienta y no los detecte en el sistema. En este proceso le pedirá la contraseña del usuario del equipo, por lo que no se preocupe.

### Ejecución ⚙️
Para ejecutar la herramienta tendremos que posicionarnos dentro de la carpeta una vez hayamos descargado/clonado el repositorio y ejecutar:

```
python3 main.py
```
_Es imprescindible que se ejecute con python3 o superior ya que si no caerá en error la ejecucción. Si no tiene instalado python en su equipo, ejecute el siguiente comando:_

```
sudo apt-get install python3
```

Tras la ejecución, veremos que se han creado una serie de carpetas. Estas poseen nombres autodescriptivos para que el usuario sepa cual es la finalidad de cada una. **_Bajo ningún concepto deben moverse del directorio en el que se han creado, ya que si no el programa las duplicará y podría caer en error._**

### Funcionamiento :mag_right:
La herramienta realiza diferentes análisis según el tipo de evidencia que se indique. Estas son las siguientes:

1. Análisis de memoria (Windows).
2. Análisis de discos duros o dispositivos de almacenamiento (Tanto Windows como Linux).
3. Análisis de dispositivos USB.
4. Análisis de capturas de red.

Cada una de ellas posee determinadas acciones de análisis para extraer información acerca de la evidencia:

**1. Análisis de memoria**

Lo realizamos a través de Volatility. Tipos de análisis y comandos que se llevan a cabo por sistema operativo:
* **_Windows_**
    * **Análisis de procesos y DLLs:** _pstree,psscan,psxview,dlllist,handles,getsids,privs,envars,verinfo_
    * **Análisis de procesos de memoria:** _memmap,vadinfo,vadtree_
    * **Análisis de objetos y memoria del kernel:** _modules,modscan,ssdt,driverscan,filescan,mutantscan,symlinkscan,thredscan,unloadedmodules_
    * **Análisis de redes:** _netscan_
    * **Análisis de registros:** _hivelist,printkey_
    * **Análisis del sistema de archivos:** _hivelist,printkey_
    * **Consola interactiva Volshell:** _volshell_

* **_Linux_**
    - _Proximamente_

**2. Análisis de discos duros o dispositivos de almacenamiento**

Tipos de análisis y comandos que se llevan a cabo:
* **Recuperar archivos eliminados:** _A través de Foremost_
* **Analizar disco:** _A través de Sleuthkit_
* **Listar archivos existentes y ocultos:** _A través de sentencias Bash_

**3. Dispositivos USB**

Tipos de análisis y comandos que se llevan a cabo:
* **Clonar USB conectado al equipo:** _A través de dd_
* **Analizar USB:** _A través de Sleuthkit_
* **Formatear USB:** _A través de dd_

**4. Capturas de red**
Tipos de análisis y comandos que se llevan a cabo:
* **Analizar captura:** _A través de comandos de tshark_
* **Recuperación de archivos enviados por distintos protocolos:** _A través de comandos de tshark_
* **Extracción de contraseñas por protocolo HTTP:** _A través de comandos de tshark_
* **Búsqueda personalizada (Próximamente)**

### Construido con 🛠️
Los lenguajes de programación y herramientas que hemos usado para llevarlo a cabo son:
* [Python](https://es.python.org/) - Lenguaje de programación.
* [Bash](https://es.wikipedia.org/wiki/Bash) - Lenguaje de ordenes.
* [Foremost](https://github.com/jonstewart/foremost) - Programa de Linux para recuperar archivos.
* [Volatility](https://github.com/volatilityfoundation/volatility) - Framework de análisis de memoria.
* [Sleuthkit](https://www.sleuthkit.org/) - Software para extraer datos de unidades de disco y otros dispositivos de almacenamiento.
* [dd](https://es.wikipedia.org/wiki/Dd_(Unix)) - Programa de Linux para clonar evidencias.
* [Tshark](https://www.wireshark.org/docs/man-pages/tshark.html) - Analizador de protocolos de red.

### Autores ✒️
* <a href="https://github.com/ElPertejo"> Ricardo Santos Pertejo </a><br>
* <a href="https://github.com/AlphaQueens">Álvaro Reina Abascal</a><br>
