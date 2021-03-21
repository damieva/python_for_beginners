# Creación de listas:
demoList = [1, 'denis', 1.4, True, [1, 2, 'sanchez']]

numberList = list((1, 2, 3, 4)) # Pasamos como argumento una tupla
print(numberList)

r = list(range(1, 10)) # Utilizamos la función range
print(r)

colors = ['red', 'blue', 'green']
print(type(colors))

print(dir(colors))
print(len(colors)) 
print(colors[1])

# Buscar elemento:
print('green' in colors) # Nos devuelve el índice
print(colors.index('blue'))  # IDEM
print(colors.count('green')) # Numero de veces se repite el elemento 'yellow'

# Modificar elemento:
colors[1] = 'yellow'
print(colors)

# Añadir elemento:
colors.append('violet') # Solo 1 elemento
colors.extend(['blue', 'brown']) # Varios elementos
colors.insert(1, 'black') # Insertar en una posición concreta
print(colors)

# Eliminar elementos:
colors.pop() # Eliminamos el último
colors.pop(0) # Eliminamos un elemento pasandole el índice por parámetro
colors.remove('green') # Elminamos el elemento concreto que le indicamos
print(colors)

# Ordenar:
colors.sort()
colors.sort(reverse=True)
print(colors)

# Limiamos lista:
colors.clear()
print(colors)