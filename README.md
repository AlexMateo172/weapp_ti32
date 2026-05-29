# weapp_ti32
## 1. Crear un ambiente virtual.(Vitual Envoiremnt)

Crear un virtual envoroment para instalar las librerias necesarias en python

````shell

python3 -m venv .venv 
````

 ## 2.  Iniciar el virtual enviroment para instalar las liberias necesarias  para el proyect

 Iniciar el virtual envirament para instalar las librerias necesarias para el proyecto

 ````shell
 source .venv/bin/activate
 ````

 ## 3 Actulizar **PIP**
 }Actualizar el instador de paquetes de Python

 ````shell
 pip install --upgrape pip
````

## 4 Instalar el micro-framewrok **web..py##}

Instalar el *micro-framework* **web.py** para la utilizando python

````shell

 pip install web.py
````

## 5 Crear el archivo **requiremens.txt**

crear el archivo **requierements.txt con la lista de lad librerias


````shell
pip frezze > requierements.txt
````

## 6 Crea el archivo **runtime.txt** con la version de python

````shell
python3 -v > runtime.txt
````

## 7 Crear el archivo **.gitmore**

Crearr el archivo  nuevo **.gitmore** para indicar las carpetas y archivos que o se van a sincroinixar con el repositortio 

````shell
*.pyc
_pycache_/
.venv
````
## 8  Indexar las Carpetas y archivos

    Indexar las carpetas y archivos creados o modificafo

    ````shell
    git add .
    ````

 ## 9 Crear el punto de control **commmit**

    Crear el puerto de control con los cambios realizados del projecto

    `````shell
    git commit
    `````
## 10 Sincronizar los cambios del repositorio

````shell
git push -u origin main
````