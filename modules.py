# Reutilizar código

# 3 types:
    # Own modules: nuestros propios módulos
    # Thirty party modules: librerías que descargamos de internet, typeando pip modules en Google vemos los módulos creados por terceros (pypi.org)
    # Python modules: modulos que nos proporcina python, se pueden investigar typeando pytho module index en Google

import datetime

print(datetime.date.today())
print(datetime.timedelta(minutes=70))


# Con el from nos ahorramos el incluir la librería cada vez que queremos utilizar el método
from datetime import timedelta, date

print(timedelta(minutes=70))
print(date.today())

# Importamos nuestro propio módulo:
import fmath

fmath.add(1, 2)
fmath.substract(2,1)


from fmath import add, substract

add(1,2)
substract(2,1)


# Utilizando modulo colorama, instalado con pip:

from colorama import Fore, Style

print(Fore.RED + "Hello World")
print(Fore.BLUE + "Hello World")
print(Fore.YELLOW + "Hello World")

