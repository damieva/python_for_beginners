# Conjunto de datos sin índice, solo para acceder, agregar o quitar datos

colors = {'Red', 'Green', 'Blue'}
print(type(colors))

# Buscar:
print('Red' in colors)

# Añadir:
colors.add('Yellow')
print(colors)

# Eliminar:
colors.remove('Red')
print(colors)

# Limpiamos el set:
colors.clear()
print(colors)

# Eliminamos el set
del colors