myStr = "Hello World"

# Obtención de propiedades y métodos
# print(dir(myStr))

# Método Upper: pasar el texto a mayúscula
print(myStr.upper())

# Método lower: pasar el texto a minúscula:
print(myStr.lower())

# Método swapcase: cambia mayúscula por minúscula y viceversa:
print(myStr.swapcase())

# Método capitalize: convertir la primera letra de cada palabra a mayúscula:
print(myStr.capitalize())

# Método replace: remplaza una cadena por otra
    # Método encadenado: el primer método nos devuelve un String y le aplicamos el segundo método upper()
print(myStr.replace("Hello", "Bye").upper())

# Método count: contar el número de veces que se repite una letra
print(myStr.count("l"))

# Método startwith(): la cadena empieza por ''
print(myStr.startswith("hola"))
print(myStr.startswith("Hello"))
print(myStr.startswith("Hello World"))

# Método endswith(): mi string termina por '':
print(myStr.endswith("World"))

# Método split: dividir, toma referencia de separador los espacios aunque le podemos indicar otra
    # La salida es una LISTA de Strings
print(myStr.split())
myStr2 = "Hello,World"
print(myStr2.split(','))

# Método find: buscar dentro de un String la posición de una letra
print(myStr.find('o'))

#Método lenght: longitud de la cadena (función que nos provee python, NO ES UN MÉTODO DEL STRING)
print(len(myStr))

# Método index: ver indice
print(myStr.index('e'))

# Métodos isnumeric, isalpha: vemos si el dato es numérico o alfanumérico
print(myStr.isnumeric())
print(myStr.isalpha())

# Ver el valor de una posición en el String:
print(myStr[4])
# También se puede obterner el valor de manera inversa
print(myStr[-1])

# Concatenar Strings:
name = "Denis"
print("My name is " + name)
# Utilizar vbles dentro de Strings:
print(f"My name is {name}")
print("My name is {0}".format(name))